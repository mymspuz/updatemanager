from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from organization.models import Organization
from database.models import Database
from version1c.models import Version1C


@login_required(login_url='login/')
def main(request, aid=0, bid=''):
    if aid:
        if set_actual(aid):
            return JsonResponse({'id': aid}, status=200)
        else:
            return JsonResponse({'errors': 'Not Found'}, status=404)
    if bid:
        if set_backup(bid):
            return JsonResponse({'id': bid}, status=200)
        else:
            return JsonResponse({'errors': 'Not Found'}, status=400)
    params = {
        'organizations': get_all_info_organization(),
        'segment': 'dashboard',
        'title': 'Dashboard',
    }
    return TemplateResponse(request, 'dashboard.html', params)


def get_all_info_organization():
    organization = Organization.objects.all()
    actual_versions = {}
    result = []
    for index, o in enumerate(organization):
        db = Database.objects.filter(organization_id=o.pk, is_active=True).select_related('version_id')
        if not db:
            continue
        result.append({'name': o.name, 'id': o.pk, 'status': '', 'db': []})
        for d in db:
            backup = True
            temp = get_backup_status(d.date_backup, d.check_backup)
            if not temp:
                backup = False
            if not d.name in actual_versions:
                actual_versions[d.name] = get_actual_version(d.version_id.config_id.pk, d.version_id.date)
            av = actual_versions.get(d.name)
            list_upd = list_upd_version(d.version_id, av.name)
            result[index]['db'].append({
                'model': d,
                'actual_v': av,
                'list_update': list_upd,
                'status': get_db_status(len(list_upd)),
                'db_backup': temp,
                'ple': check_platform(av, d)
            })
        result[index]['status'] = get_organization_status(result[index]['db'])
        result[index]['org_backup'] = backup
    return result


def get_backup_status(bdate, bcheck):
    if bcheck:
        if not bdate or date.today() > bdate + timedelta(days=7):
            return False
    return True


def get_db_status(count_upd):
    if count_upd == 1:
        return 'warning'
    elif count_upd > 1:
        return 'danger'
    return 'success'


def get_organization_status(dbs):
    result = {}
    platforms_error = 0
    for i in dbs:
        result[i['status']] = result.get(i['status'], 0) + 1
        platforms_error += i['ple']
    if platforms_error:
        result['primary'] = platforms_error
    return result


def check_platform(av, db):
    current_pl = db.platform_id.name.split('.')
    family_platform = False
    big_num_platform = False
    for i in av.platform_id.all():
        temp = i.name.split('.')
        if current_pl[0] == temp[0] and current_pl[1] == temp[1] and current_pl[2] == temp[2]:
            family_platform = True
            if int(current_pl[3]) >= int(temp[3]):
                break
        if not big_num_platform:
            big_num_platform = check_big_num_pl(current_pl, temp)
    else:
        if not family_platform and big_num_platform:
            return 0
        else:
            return 1
    return 0


def check_big_num_pl(c_pl, m_pl):
    for i in range(0, len(c_pl)):
        if int(c_pl[i]) == int(m_pl[i]):
            continue
        elif int(c_pl[i]) > int(m_pl[i]):
            return True
        else:
            return False


def get_actual_version(config, version):
    return Version1C.objects.filter(config_id=config, date__gte=version).order_by('date').last()


def list_upd_version(current_version, actual_version):
    list_version = Version1C.objects.filter(date__gt=current_version.date,
                                            config_id=current_version.config_id.pk).order_by('-date')
    result = []
    if list_version:
        temp = current_version.name
        while not actual_version in result:
            temp = get_last_versions(temp, list_version)
            result.append(temp)
    return result


def get_last_versions(version, list_version):
    for i in list_version:
        if version in i.connection:
            return i.name


def set_actual(aid):
    try:
        db = Database.objects.get(pk=aid)
        db.version_id = get_actual_version(db.version_id.config_id.pk, db.version_id.date)
        db.save()
        return aid
    except ObjectDoesNotExist:
        return False


def set_backup(bid):
    try:
        db = Database.objects.get(pk=int(bid[1:]))
        db.date_backup = date.today()
        db.save()
        return bid
    except ObjectDoesNotExist:
        return False

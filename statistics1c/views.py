from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from datetime import date
from django.db.models import Count
from django.db.models.functions import TruncMonth

from version1c.models import Version1C


@login_required(login_url='login/')
def main(request):
    params = {
        'chart_bar': get_chart_bar(date.today().year),
        'segment': 'statistics1c',
        'title': 'Statistics1C',
    }
    return TemplateResponse(request, 'statistics1c.html', params)


def get_chart_bar(year):
    m = Version1C.objects.filter(date__year=year).annotate(month=TruncMonth('date')).values('month').annotate(
        count=Count('pk')).order_by('month')
    chart_bar = {'labels': [], 'series': []}
    for i in m:
        chart_bar['labels'].append(i['month'].strftime("%B"))
        chart_bar['series'].append(i['count'])
    return chart_bar

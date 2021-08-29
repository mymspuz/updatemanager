from django.template.response import TemplateResponse


def page_not_found_view(request, exception):
    return TemplateResponse(request, '404.html', status=404)


def page_server_error_view(request):
    return TemplateResponse(request, '500.html', status=500)

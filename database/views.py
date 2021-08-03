from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from . models import Database


class DatabaseList(ListView):
    model = Database
    template_name = 'database.html'
    context_object_name = 'dbs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My list db'
        return context


def mydb(request):
    db = Database.objects.all()
    my = Database.objects.select_related('config_id').get(pk=1)
    print(db)
    print(my.config_id)
    return HttpResponse(db)
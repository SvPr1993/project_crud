from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person


# вывод данных
def index_views(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})


# получение и сохранение новых данных
def create_views(request):
    if request.method == 'POST':
        person = Person()
        person.name = request.POST.get('name')
        person.surname = request.POST.get('surname')
        person.save()
    return HttpResponseRedirect('/')


# изменение данных
def edit_views(request, id):
    person = Person.objects.get(id=id)

    if request.method == 'POST':
        person.name = request.POST.get('name')
        person.surname = request.POST.get('surname')
        person.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'edit.html', {'person': person})


# удаление данных
def delete_views(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return HttpResponseRedirect('/')

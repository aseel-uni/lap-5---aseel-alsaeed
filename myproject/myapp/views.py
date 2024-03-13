from django.shortcuts import render, redirect
from django.http import HttpResponse

people = []


class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username


def add_view(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        passW = request.POST.get('password')
        person = Person(username = name, password = passW)
        people.append(person)
        return redirect('default')
    return render(request, 'myapp/add.html')


def default_view(request):
    return render(request, 'myapp/default.html', {'people': people})

from django.http import HttpResponseRedirect
from django.shortcuts import render
from webapp.models import Task, status_choices


def list_of_task_view(request):
    list_tasks = Task.objects.all()
    return render(request, 'list_of_task_view.html', {"list_tasks": list_tasks})


def task_view(request):
    task_id = request.GET.get('id')
    task = Task.objects.get(id=task_id)
    return render(request, 'task_view.html', {'task': task})


def task_create_view(request):
    if request.method == "GET":
        return render(request, 'task_create_view.html', {'status': status_choices})
    elif request.method == "POST":
        description = request.POST.get("description")
        status = request.POST.get("status")
        pub_date = request.POST.get("pub_date")
        if pub_date == '':
            pub_date = None

        task = Task.objects.create(
            description=description,
            status=status,
            pub_date=pub_date,
        )
        return render(request, 'task_view.html', {'task': task})


def remove_view(request):
    id = request.GET.get('id')
    task_remove = Task.objects.get(id=id)
    task_remove.delete()
    return HttpResponseRedirect('/')

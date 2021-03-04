from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect, get_object_or_404

from webapp.forms import TaskForm
from webapp.models import Task


def list_of_task_view(request):
    list_tasks = Task.objects.all()
    return render(request, 'list_of_task_view.html', {"list_tasks": list_tasks})


def task_view(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'task_view.html', {'task': task})


def task_create_view(request):

    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task_create_view.html', context={'form': form})

    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                description=form.cleaned_data.get('description'),
                text_for_detailed=form.cleaned_data.get('text_for_detailed'),
                status=form.cleaned_data.get('status'),
                pub_date=form.cleaned_data.get('pub_date')
            )
            return redirect('list-view')
        return render(request, 'task_create_view.html', context={'form': form})


def task_update_view(request, id):
    task_update = get_object_or_404(Task, id=id)

    if request.method == 'GET':
        form = TaskForm(initial={
            'description': task_update.description,
            'text_for_detailed': task_update.text_for_detailed,
            'status': task_update.status,
            'pub_date': task_update.pub_date
        })
        return render(request, 'task_update.html', context={'form': form, 'task_update': task_update})

    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task_update.description = form.cleaned_data.get("description")
            task_update.text_for_detailed = form.cleaned_data.get("text_for_detailed")
            task_update.status = form.cleaned_data.get("status")
            task_update.pub_date = form.cleaned_data.get("pub_date")
            task_update.save()
            return redirect('list-view')

        return render(request, 'task_create_view.html', context={'form': form})


def remove_view(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'GET':
        task.delete()
    url = reverse('list-view')
    return HttpResponseRedirect(url)


from django.shortcuts import render
from webapp.models import Task


def list_of_task_view(request):
    list_tasks = Task.objects.order_by('pub_date')
    return render(request, 'list_of_task_view.html', {"list_tasks": list_tasks})


def task_view(request):
    task_id = request.GET.get('id')
    task = Task.objects.get(description=task_id)
    return render(request, 'task_view.html', {'task': task})


def task_create_view(request):
    if request.method == "GET":
        return render(request, 'task_create_view.html')
    elif request.method == "POST":
        description = request.POST.get("description")
        status = request.POST.get("status")
        pub_date = request.POST.get("pub_date")

        task = Task.objects.create(
            description=description,
            status=status,
            pub_date=pub_date,
        )

        return render(request, 'task_create_view.html', {'task': task})
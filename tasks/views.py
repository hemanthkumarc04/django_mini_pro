from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Task
from .forms import TaskForm


def task_list(request):
    """Display all tasks grouped by status on a Kanban board."""
    todo_tasks = Task.objects.filter(status='todo')
    in_progress_tasks = Task.objects.filter(status='in_progress')
    done_tasks = Task.objects.filter(status='done')

    context = {
        'todo_tasks': todo_tasks,
        'in_progress_tasks': in_progress_tasks,
        'done_tasks': done_tasks,
        'total_count': Task.objects.count(),
        'done_count': done_tasks.count(),
    }
    return render(request, 'tasks/task_list.html', context)


def task_create(request):
    """Create a new task."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Create'})


def task_edit(request, pk):
    """Edit an existing task."""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Update', 'task': task})


def task_delete(request, pk):
    """Delete a task after confirmation."""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@require_POST
def task_toggle_status(request, pk):
    """Cycle task status: todo → in_progress → done → todo."""
    task = get_object_or_404(Task, pk=pk)
    status_cycle = {'todo': 'in_progress', 'in_progress': 'done', 'done': 'todo'}
    task.status = status_cycle.get(task.status, 'todo')
    task.save()
    return redirect('task_list')

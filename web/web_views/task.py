from django.forms import ModelForm
from django.forms import widgets
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from web import models
from web.web_views.user import TaskModelForm


class TaskModelForm1(ModelForm):
    class Meta:
        model = models.Task
        fields = {'level', 'title', 'detail', 'createtime'}
        widgets = {
            "level": widgets.Select(attrs={'class': 'form-control'}),
            "title": widgets.TextInput(attrs={'class': 'form-control'}),
            "detail": widgets.TextInput(attrs={'class': 'form-control'}),
            "createtime": widgets.DateTimeInput(attrs={'class': 'form-control'}),
        }


@csrf_exempt
def index(request):
    info_id = request.session.get('info')['id']
    info_name = request.session.get('info')['username']
    form = TaskModelForm(initial={'user': info_name})
    return render(request, 'task/task.html', {'form': form})


def task_add(request):
    return None

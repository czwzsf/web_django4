from django.shortcuts import render, redirect
from django import forms
from web import models
from django.forms import widgets
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class Login_ModelForm(forms.ModelForm):
    """登入的ModelForm"""

    class Meta:
        model = models.User
        fields = {"username", "password"}

    username = forms.CharField(label='username', widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={"class": "form-control"}),
                               required=True)


def login(request):
    if request.method == "GET":
        form = Login_ModelForm()
        return render(request, 'user/login.html', {'form': form})
    form = Login_ModelForm(data=request.POST)
    if form.is_valid():
        user_object = models.User.objects.filter(**form.cleaned_data).first()
        if not user_object:
            form.add_error('password', '用户名或密码错误')
            return render(request, 'user/login.html', {'form': form})
        request.session["info"] = {'id': user_object.id, 'username': user_object.username}
        request.session.set_expiry(60 * 60 * 24)
        return redirect('/index/')
    else:
        return render(request, 'user/login.html', {'form': form})


# 个人任务的创建
class TaskModelForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            "level": widgets.Select(attrs={'class': 'form-control'}),
            "title": widgets.TextInput(attrs={'class': 'form-control'}),
            "detail": widgets.TextInput(attrs={'class': 'form-control'}),
            "user": widgets.Select(attrs={'class': 'form-control'}),
            "createtime": widgets.DateTimeInput(attrs={'class': 'form-control'}),
        }


def index(request):
    info_id = request.session.get('info')['id']
    queryset = models.Task.objects.filter(user=info_id).all()
    print(queryset)
    taskform = TaskModelForm()
    context = {
        "taskform": taskform,
        "queryset": queryset,
    }

    return render(request, 'user/index.html', {'queryset': queryset})


def logout(request):
    request.session.clear()  # 清除session信息
    return redirect('/login/')

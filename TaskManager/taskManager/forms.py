from .models import Task, UserProfile
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


class TaskAdding(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'finish': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
        }
        exclude = ['id', 'pub_date', 'user_creator']


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/profile/"
    template_name = "taskManager/sign.html"

    def form_valid(self, form):
        form.save()
        name = form.cleaned_data['username']
        UserProfile(id=name, user_auth=User.objects.get(username=name)).save()
        super(RegisterFormView, self).form_valid(form)
        login(self.request, User.objects.get(username=name))
        logger.info('Пользователь {} успешно зарегистрирован.'.format(name))
        return redirect('profile')

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from . import forms


urlpatterns = [
    path('', views.index, name='home'),
    path('tasks/', views.tasks_page, name='tasks'),
    path('tasks/create/', views.add_task, name='add_task'),
    path('sign_up/', forms.RegisterFormView.as_view(), name='sign_up'),
    path('sign_in/', LoginView.as_view(redirect_authenticated_user=True, template_name='taskManager/sign_in.html',
                                       redirect_field_name="{% url 'profile' %}"), name='sign_in'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout', views.logout_view, name='logout'),
    path('password_change', views.change_password, name='password'),
    path('delete_user', views.delete_user, name='delete_user'),
    path('edit/<str:task_id>', views.task_edit, name='edit'),
    path('remove/<str:task_id>', views.remove, name='remove'),
    path('finished/<str:task_id>', views.finished, name='finished'),
    path('friends_page/remove/', views.remove_friend, name='friends_remove'),
    path('accounts/profile/friends_page/', views.user_friends, name='friends_page'),
]


from django.urls import path

from . import views

app_name = "pastebin"
urlpatterns = [
    path('', views.index, name='index'),
    path('paste/<str:paste_id>/', views.paste, name='paste'),
    path('create/', views.create_form, name='create'),
    path('confirm/', views.confirm_paste, name='confirm'),
]

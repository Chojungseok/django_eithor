from django.urls import path
from . import views

app_name = 'eithor'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:question_id>/detail/', views.detail, name='detail'),
    path('random/', views.random_detail, name='random_detail'),

    # comment
    path('<int:question_id>/comment/create/', views.comment_create, name='comment_create'),
    ]
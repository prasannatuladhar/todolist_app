from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<task_id>',views.task_delete,name='task_delete'),
    path('edit/<task_id>',views.edit_task,name='task_edit'),
    path('completed/<task_id>',views.mark_as_completed,name='mark_as_completed'),
    path('pending/<task_id>',views.mark_as_pending,name='mark_as_pending'),

]

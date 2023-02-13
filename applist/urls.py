
from django.urls import path
from applist import views
from applist.views import Update_form,Update_List

app_name='applist'

urlpatterns = [
    path('',views.add_fun,name='add'),
    path('delete/ <int:i>',views.delete_fun,name='delete'),
    path('updateform/<int:pk>',Update_form.as_view(),name='updateform'),
    path('updatelist/',Update_List.as_view(),name='updatelist'),
    
]
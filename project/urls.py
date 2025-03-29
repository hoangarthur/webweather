from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProjListView.as_view(), name='project'),
    path('<int:id>/', views.content, name='content'),
               ]

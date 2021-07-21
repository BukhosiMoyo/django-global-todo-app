from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeListView, name="home"),
    path('create/', views.TaskCreateView, name="create"),
    path("update/<int:pk>/", views.TaskUpdateView, name="update"),
    path("delete/<int:pk>/", views.TaskDeleteView, name="delete")
]
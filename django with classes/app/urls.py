from django.urls import path
from . import views
from .views import (List,Detail,Create,Update,Delete)



urlpatterns = [
    path('',List.as_view(),name="home"),
    path('detail/<int:pk>/',Detail.as_view(),name="detail"),
    path('create/',Create.as_view(),name="create"),
    path('post/<int:pk>/edit/',Update.as_view(),name="update"),
    path('post/<int:pk>/delete/',Delete.as_view(),name="delete")
]

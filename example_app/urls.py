from django.urls import path

from .views import *

urlpatterns = [
    path('one/', Second_logger_API.as_view()),
]
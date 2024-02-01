from django.urls import path
from .views import *

urlpatterns = [
    path('',project_list),
    path('<int:id>',project_detail)
]

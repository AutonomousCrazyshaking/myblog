from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/<int:page>.html', board, name='board'),
]

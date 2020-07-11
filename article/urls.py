from django.urls import path
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    path('', RedirectView.as_view(url='user/login.html')),
    path('<int:id>/<int:page>.html', article, name='article'),
    path('detail/<int:id>/<int:aId>.html', detail, name='detail')
]

# mlb/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('news_list/', views.news_list, name='news_list'),
    path('standings/', views.standings_view, name='standings'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

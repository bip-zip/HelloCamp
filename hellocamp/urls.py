from django.contrib import admin
from django.urls import path
from camps.views import IndexView
from scraper.views import DynamicScraperView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),   
    path('scraper/', DynamicScraperView.as_view(), name='scraper'), 
]

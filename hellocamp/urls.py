from django.contrib import admin
from django.urls import path
from camps.views import IndexView, search
from scraper.views import DynamicScraperView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', IndexView.as_view(), name='index'),   
    path('search/', search, name='search'),   
    path('', DynamicScraperView.as_view(), name='scraper'), 
]

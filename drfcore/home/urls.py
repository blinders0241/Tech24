from . import views
from rest_framework import routers
from .views import *
from django.urls import path

router = routers.DefaultRouter()
router.register('home',views.HomeViewSet, basename='home')
urlpatterns = [
    
    path('displayNotes/', views.displayNotes),
    path('upload', views.handle_request),
    path('uploadData/', views.handleDBUpload),
    path('delete/', views.clearDB),
    path('displayStockdetails/', views.displayStockdetails),
    path('displayIndexdetails/', views.displayIndexdetails),
    path('stockMasterDetail/', views.stockMasterDetail),
    path('heatMap/', views.heatMapGenerate),
    
]
urlpatterns += router.urls  
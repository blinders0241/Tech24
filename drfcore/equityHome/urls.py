from . import views
from rest_framework import routers
from .views import *
from django.urls import path

urlpatterns = [
    path('uploadequity/', views.handleEquityDBUpload),
    path('uploadIndexHistoricals/', views.uploadIndexHistoricals),
    path('deleteEquity/', views.clearDB),
    path('displayEquityetails/', views.displayEquityetails),
    # path('displayIndexdetails/', views.displayIndexdetails),
    # path('stockMasterDetail/', views.stockMasterDetail),
    # path('latest/created', views.getMostRecentDate),
    
]

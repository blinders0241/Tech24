from . import views
from rest_framework import routers
from .views import *
from django.urls import path

urlpatterns = [
    path('FarFlixhome/', views.FarFlixhome),
    path('FarFlixUpload/', views.FarFlixUpload),
    path('FFMovieDetailsUpload/', views.FFMovieDetailsUpload),
    path('FarFlixSearch/', views.FarFlixIMDBDetails),
    path('FarFlixFileDetails/', views.FarFlixFileDetails),
    # path('displayIndexdetails/', views.displayIndexdetails),
    # path('stockMasterDetail/', views.stockMasterDetail),
    path('FF_FetchDetailsFromDB/', views.FF_FetchDetailsFromDB),
    path('FF_FetchEditDetailsTODB/', views.FF_FetchEditDetailsTODB),
    path('FF_DeleteMoviebyID/', views.FF_DeleteMoviebyID),
    
]

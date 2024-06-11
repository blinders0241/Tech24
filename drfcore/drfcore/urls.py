from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include('home.urls')),
    path("equity/",include('equityHome.urls')),
    path("farFlix/",include('FarFlix.urls')),
    path("sparrow/",include('sparrow.urls'))
]

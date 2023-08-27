
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('studentapi',views.StudentViewset,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]

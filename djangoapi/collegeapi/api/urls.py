from django.urls import path,include
from api.views import collegeviewset,Studentviewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'college',collegeviewset)
router.register(r'students',Studentviewset)


urlpatterns = [
  
    path('',include(router.urls)),
]

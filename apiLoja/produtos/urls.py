from django.urls import path
from rest_framework import routers


from .views import *
router = routers.DefaultRouter()
router.register('produtos', ProdutosViewSet)

urlpatterns = router.urls
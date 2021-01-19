from django.urls import path, include
from .views import OrderViewSet, OrderSpecifiedNIPViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

#order router
router = routers.SimpleRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('nip/', OrderSpecifiedNIPViewSet.as_view({
        'post': 'create'
    })),
]

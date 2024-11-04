# from django.urls import path, include
# from rest_framework import routers
# from api import views #
# #from . import views  # Asegúrate de que sea relativo a tu app


# router = routers.DefaultRouter()
# router.register(r'certificates', views.CertificateViewSet)
# router.register(r'domains', views.DomainViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]


from django.urls import path, include
from rest_framework import routers

from rest_framework.routers import DefaultRouter

from . import views  # Importa las vistas de la aplicación

# # Define el router y registra los viewsets
# router = routers.DefaultRouter()
# router.register(r'certificates', views.CertificateViewSet)
# router.register(r'domains', views.DomainViewSet)

# # Incluye las rutas del router en las URLs de la aplicación
# urlpatterns = [
#     path('', include(router.urls)),  # Incluir las rutas registradas en el router.
# ]

# from . import BrandViewSet, ModelViewSet, SeriesViewSet, CategoryViewSet, InventoryViewSet

router = DefaultRouter()
router.register(r'brands', views.BrandViewSet)
router.register(r'models', views.ModelViewSet)
router.register(r'series', views.SeriesViewSet)
router.register(r'categories',views.CategoryViewSet)
router.register(r'inventory', views.InventoryViewSet)
router.register(r'certificates', views.CertificateViewSet)
router.register(r'domains', views.DomainViewSet)

urlpatterns = [
    path('', include(router.urls)),
]





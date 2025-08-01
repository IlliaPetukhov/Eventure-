"""
URL configuration for EventManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from event.views import EventViewSet
from user.views import UserViewSet, OrganizerViewSet
from authentication.views import LoginView, RegistrationView
from rest_framework import routers
from django.urls import path
from django.urls import include
from rest_framework_simplejwt.views import TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
import debug_toolbar
from django.conf.urls.static import static
from django.conf import settings



schema_view = get_schema_view(
   openapi.Info(
      title="Event API",
      default_version='v1',
      description="Документація API для івент-платформи від Ілюшки)",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register("events", EventViewSet, basename="events")
router.register("user", UserViewSet, basename="user")
router.register("organizers", OrganizerViewSet, basename="organizers")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path('__debug__/', include(debug_toolbar.urls)),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/registration/", RegistrationView.as_view(), name="registration"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

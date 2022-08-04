from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views as quickstart_views
from tutorial.scheduler import views as scheduler_views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', quickstart_views.UserViewSet)
router.register(r'groups', quickstart_views.GroupViewSet)
router.register(r'apsjob',scheduler_views.DjangoJobViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

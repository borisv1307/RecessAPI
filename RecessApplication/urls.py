"""RecessApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path, re_path
from RecessApplication import views
from .api import LoginAPI, RegistrationAPI
import logging
from .router import OptionalSlashRouter

router = OptionalSlashRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'class_info', views.ClassViewSet)
router.register(r'class_enrollment', views.ClassEnrollmentViewSet)
router.register(r'class_schedule', views.ClassScheduleViewSet)
router.register(r'assignments', views.ClassScheduleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^admin/?', admin.site.urls),
    re_path(r'^api-auth/register/?', RegistrationAPI.as_view()),
    re_path(r'^api-auth/auth/?', LoginAPI.as_view()),
    re_path(r'^api-auth/?', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^zoom/meetings/(?P<pk>[0-9]+)/?$', views.ZoomMeetingsView.as_view()),
    re_path(r'^zoom/meetings/?', views.ZoomMeetingsListView.as_view()),
]

logger = logging.getLogger(__name__)
logger.info("----- INITIALIZATION COMPLETE -----")
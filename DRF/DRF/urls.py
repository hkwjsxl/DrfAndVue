from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('version_manage/',
         include(('sub_apps.version_manage.urls', 'sub_apps.version_manage'), namespace='version_manage')),
    path('auth_permission/',
         include(('sub_apps.auth_permission.urls', 'sub_apps.auth_permission'), namespace='auth_permission')),
    path('access_frequency/',
         include(('sub_apps.access_frequency.urls', 'sub_apps.access_frequency'), namespace='access_frequency')),
    path('serializer_related/',
         include(('sub_apps.serializer_related.urls', 'sub_apps.serializer_related'), namespace='serializer_related')),

]

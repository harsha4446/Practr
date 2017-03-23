from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('users.urls')),
    url(r'^profile_page/', include('profile_page.urls')),

]


from django.conf.urls import url
from django.contrib import admin

from video.views import home, login, register

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^admin/', admin.site.urls),
]


from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^about/$', views.about),

    url(r'^$', views.homepage),

    url(r'^register$', views.register, name='register'),

]

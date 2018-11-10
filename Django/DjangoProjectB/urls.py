"""DjangoProjectB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from settings import MEDIA_ROOT
from interview.views import InterListView

from rest_framework.authtoken.views import obtain_auth_token
from interview.urls import router
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
    url(r'^interlist/$',InterListView.as_view(),name='interlist'),

    url(r'^api/token/',obtain_auth_token,name='api-token'),
    url(r'^api/',include(router.urls)),
]

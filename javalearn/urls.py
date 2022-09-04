"""javalearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from testapp.views import index,blog,materials, quizz, reminder, sertificate, login, signup
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve

urlpatterns = [
    path('',lambda request: redirect('index/', permanent=False)),
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('blog/', blog, name="blog"),
    path('materials/', materials, name="materials"),
    path('quizz/', quizz, name="quizz"),
    path('reminder/', reminder, name="reminder"),
    path('sertificate/', sertificate, name="sertificate"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

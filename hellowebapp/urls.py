"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
url(r'^$', 'collection.views.index', name='home'),
	url(r'^about/$',
		TemplateView.as_view(template_name='about.html'),
		name='about'),
	url(r'^contact/$',
		TemplateView.as_view(template_name='contact.html'),
		name='contact'),
    url(r'^pharmacists/(?P<slug>[-\w]+)/$',
        'collection.views.pharmacist_detail',
        name='pharmacist_detail'),
    url(r'^pharmacists/(?P<slug>[-\w]+)/edit$',
        'collection.views.edit_pharmacist', name='edit_pharmacist'),
    url(r'^admin/', admin.site.urls),
]
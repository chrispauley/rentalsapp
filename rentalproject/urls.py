from django.conf.urls import include, url
from django.contrib import admin
from rentalsapp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'rentalproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^contracts', views.contracts, name='contracts'),
    url(r'^contract/(?P<id>\d+)/', views.contract_detail, name='contract_detail'),
    url(r'^admin/', include(admin.site.urls)),
]

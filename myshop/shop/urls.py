from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^product/$', views.product_list, name='product_list'),
    url(r'^product/new/$', views.product_listNew, name='product_listNew'),
    url(r'^product/sale/$', views.product_listSale, name='product_listSale'),
    url(r'^contacts/$', views.contacts_list, name='contacts_list'),
    url(r'^abouts/$', views.about, name='about'),
    url(r'^brands/$', views.brand, name='brand'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
from django.conf.urls import url
from django.contrib import admin

from inventory import views

urlpatterns = [
	# match top level / url
	url(r'^$', views.index, name='index'),
	url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
	url(r'^backorder/(?P<id>\d+)/', views.backorder_detail, name='backorder_detail'),
	url(r'^employees/', views.employee_list, name='employee_list'),
    url(r'^admin/', admin.site.urls),
]

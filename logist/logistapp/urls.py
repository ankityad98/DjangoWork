from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^$',views.Home.as_view(),name='home'),
url(r'^triplist$',views.TripListView.as_view(),name='trip_list'),
url(r'^register/$',views.register,name='register'),
url(r'^trip/new$',views.CreateTripView.as_view(),name='add_trip'),
url(r'^trip/(?P<pk>\d+)$',views.TripDetailView.as_view(),name='trip_detail'),
url(r'^trip/(?P<pk>\d+)/edit/$', views.TripDetailView.as_view(), name='trip_edit'),
url(r'^trip/(?P<pk>\d+)/remove/$', views.TripDeleteView.as_view(), name='trip_remove'),
]

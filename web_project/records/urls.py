from django.conf.urls import url, include 
from records import views

urlpatterns = [

	url(r'^$', views.PostListView.as_view(), name = 'list_posts'),
	url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name = 'detail_posts'),
	url(r'^create/$', views.CreatePostView.as_view(), name = 'create_posts'),
	url(r'^(?P<pk>\d+)/update/$', views.UpdatePostView.as_view(), name = 'delete_posts'),
	url(r'^(?P<pk>\d+)/delete/$', views.DeletePostView.as_view(), name = 'delete_posts'),

]
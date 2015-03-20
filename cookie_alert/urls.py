from django.conf.urls import patterns, url
from views import views 

urlpatterns = patterns('',
    url(r'^$', views.alert, name='cookie-alert-index'),
)


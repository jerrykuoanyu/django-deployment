from django.conf.urls import url
from userInfo import views

app_name = "userInfo"

urlpatterns = [
    url(r'^$',views.users,name='users'),
    url(r'^forms/$', views.form_name_view, name='forms'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),

    url(r'^register/$', views.register_view, name='register'),

    #url(r'users/$',views.users,name='user'),


]

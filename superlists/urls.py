from django.conf.urls import url
from lists import views
from accounts import views as accounts_views
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/new$', views.new_list, name='new_list'),
    url(r'^lists/(\d+)/$', views.view_list, name='view_list'),
    url(r'^accounts/send_login_email$', accounts_views.send_login_email, name='send_login_email'),
    url(r'^accounts/login$', accounts_views.login, name='login'),
    url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
]


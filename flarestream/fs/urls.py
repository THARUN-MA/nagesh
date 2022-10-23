from django.conf.urls import url,include
from fs import views

app_name='fs'

urlpatterns=[
    url('login/',views.login,name='login'),
    url('signup/',views.signup,name='signup'),
    url('logout/',views.logout,name='logout'),
    url('dashboard/',views.dashboard,name='dashboard'),
    url('admindash/',views.admindash,name='admindash'),
    url('subscription/',views.subscription,name='subscription'),
    url('albumsong/',views.albumsong,name='albumsong'),
    url('shortmovie/',views.shortmovie,name='shortmovie'),
    url('addmedia/',views.addmedia,name='addmedia'),
    url(r'^watchshort/(?P<value>\w+)$',views.watchshort,name='watchshort'),
    url(r'^watchalbum/(?P<value>\w+)$',views.watchalbum,name='watchalbum'),
]

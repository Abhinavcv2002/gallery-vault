from django.conf import settings
from django.urls import path
from .import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.signin,name='signin'),
    path('index',views.index,name="index"),
    path('signup',views.usersignup,name="signup"),

    path('gv',views.viewsmain,name='namemain'),
    path('delete/<pk>',views.delete,name='urdelete'),
    path('addimage',views.add,name='add'),
    path('pic/<id>',views.picture,name='pic'),

    path('logout',views.logout,name='logout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
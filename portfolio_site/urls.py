from django.urls import path, include
#from quote_generator import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views


urlpatterns = [
    path("admin/", admin.site.urls), #Link to admin
    path("", views.home, name="home"),
    # path("", views.index, name="index"), #Link to home page 
    # path("about/", views.about, name="about"), # Link to about page
    #path('', views.home, name="home"),
    path('blog/', include('blog.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
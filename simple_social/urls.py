from django.conf.urls import url
from simple_social import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='social_home'),
]
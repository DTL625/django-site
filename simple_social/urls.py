from django.conf.urls import url, include
from simple_social import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='social_home'),
    url(r'accounts/', include('social_account.urls', namespace='accounts')),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'test/$', views.TestPage.as_view(), name='test'),
    url(r'thanks/$', views.ThanksPage.as_view(), name='thanks'),
]
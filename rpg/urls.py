from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from card import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cards/', views.CardList.as_view()),
    url(r'^card/(?P<pk>[0-9]+)/', views.CardDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

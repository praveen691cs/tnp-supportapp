from django.conf.urls import url

from myapp import views

urlpatterns=[
    url(r'^index$',views.index),
    url(r'^link1$',views.link1,name='link1'),
url(r'^link2$',views.link2,name='link2'),
url(r'^link3$',views.link3,name='link3'),
url(r'^link4$',views.link4,name='link4'),
url(r'^link5$',views.link5,name='link5')
]
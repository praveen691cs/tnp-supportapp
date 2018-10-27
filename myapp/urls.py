from django.conf.urls import url

from myapp import views

urlpatterns=[
    url(r'^index$',views.index,name='index'),
    url(r'^link1$',views.link1,name='Link1'),
url(r'^link2$',views.link2,name='Link2'),
url(r'^link3$',views.link3,name='Link3'),
url(r'^link4$',views.link4,name='Link4'),
url(r'^link5$',views.link5,name='Link5')
]
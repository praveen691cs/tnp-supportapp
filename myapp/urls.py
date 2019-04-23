from django.conf.urls import url

from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^api/json/', views.tnp_api_json, name='tnp_api_json'),
    url(r'^index$',views.index,name='index'),
    url(r'^pageviews$',views.page,name='page'),
    url(r'^averagetime$',views.average,name='average'),
    url(r'^product$',views.product,name='product'),

    url(r'^link1$',views.link1,name='Link1'),
url(r'^link2$',views.link2,name='Link2'),
url(r'^link3$',views.link3,name='Link3'),
url(r'^link4$',views.link4,name='Link4'),
url(r'^link5$',views.link5,name='Link5')
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf.urls import url, include
from basic_ap import views

# template tagging
app_name = 'basic_ap'

urlpatterns = [
    url('relative/', views.relative, name = 'relative'),
    url('other/', views.other, name = 'other'),
]

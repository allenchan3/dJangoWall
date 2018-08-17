from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^post_message$', views.add_message),
    url(r'^post_comment$$', views.add_comment),
    url(r'^delete/(?P<m_id>\d+)$', views.delete_message),
    url(r'^toEdit/(?P<m_id>\d+)$', views.toEdit),
    url(r'^toEdit/editPost/(?P<m_id>\d+)$', views.Edit),
]
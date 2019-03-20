from django.conf.urls import url
from fls.views import *

app_name = "fls"

urlpatterns = [
    url(r'^$', login_view),
    url(r'^logout$', logout_page, name='logout'),
    url(r'^profile$', profile, name="profile"),
    url(r'^login/$', login_view, name="login_view"),
    url(r'^criteria/(?P<id>\d+)/$', criteria, name="criteria"),
    url(r'^comps$', list_comp, name="list_comp"),
    url(r'^comp$', comp, name="comp"),
    url(r'^load_request/(?P<comp_id>\d+)/$', load_request, name="load_request"),
    url(r'^comp/(?P<comp_id>\d+)/pairwise_comparison$', pairwise_comparison, name="pairwise_comparison"),
    url(r'^preq/(?P<id>\d+)/$', process_request, name="preq"),
]

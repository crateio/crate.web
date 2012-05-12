from django.conf.urls import patterns, url

from crate.web.search.views import Search


urlpatterns = patterns("",
    url(r"^$", Search.as_view(), name="search"),
)

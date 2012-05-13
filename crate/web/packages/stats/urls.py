from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r"^(?P<slug>[^/]+)/delta\.json$", "crate.web.packages.stats.views.stats_delta", name="package_stats_delta"),
)

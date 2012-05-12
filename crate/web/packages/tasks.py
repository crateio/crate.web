from celery.task import task

from crate.web.packages.simple.views import PackageIndex


@task
def refresh_package_index_cache():
    pi = PackageIndex()
    pi.get_queryset(force_uncached=True)

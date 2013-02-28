from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.utils.translation import ugettext as _
from django.views.generic.detail import DetailView
from django.shortcuts import render

from crate.web.history.models import Event
from crate.web.packages.models import Release, Package


class ReleaseDetail(DetailView):

    model = Release
    queryset = Release.objects.all().prefetch_related(
                                        "uris",
                                        "files",
                                        "requires",
                                        "provides",
                                        "obsoletes",
                                        "classifiers",
                                    )

    def get_context_data(self, **kwargs):
        ctx = super(ReleaseDetail, self).get_context_data(**kwargs)
        ctx.update({
            "release_files": [x for x in self.object.files.all() if not x.hidden],
            "version_specific": self.kwargs.get("version", None),
            "versions": Release.objects.filter(package=self.object.package).select_related("package").order_by("-order"),
            "history": Event.objects.filter(package=self.object.package.name).order_by("-created"),
        })
        return ctx

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        package = self.kwargs["package"]
        version = self.kwargs.get("version", None)

        queryset = queryset.filter(package__name=package)

        if version:
            queryset = queryset.filter(version=version)
        else:
            queryset = queryset.filter(hidden=False).order_by("-order")[:1]

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise Http404(_(u"No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj


def fuck_the_status_quo(request):
    blah = Package.objects.exclude(name__in=Release.objects.exclude(files=None).distinct("package").values_list("package__name", flat=True)).order_by("name")
    # blah = {}
    # for r in Release.objects.filter(files=None).select_related("package").prefetch_related("package"):
    #     blah.setdefault(r.package.name, []).append(r)
    return render(request, "status_quo.html", {"projects": blah})

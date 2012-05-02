from django.conf.urls import patterns, url

from lists.views import AddToList, AddToNewList, RemoveFromList

urlpatterns = patterns("",
    url(r"^(?P<list>[^/]+)/(?P<package>[^/]+)/add/$", AddToList.as_view(), name="add_package_to_list"),
    url(r"^_/(?P<package>[^/]+)/new/$", AddToNewList.as_view(), name="add_package_to_new_list"),
    url(r"^(?P<list>[^/]+)/(?P<package>[^/]+)/remove/$", RemoveFromList.as_view(), name="remove_package_from_list"),
)
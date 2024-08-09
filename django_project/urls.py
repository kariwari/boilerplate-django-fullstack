from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from django.conf.urls import handler500, handler404, handler403

# from users.views import Error403View, Error404View, Error500View

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin/django-rq/", include("django_rq.urls")),
    path("", include("users.urls", namespace="users")),
]

# https://docs.djangoproject.com/en/dev/topics/http/views/#customizing-error-views
# handler404 = Error404View.as_view()  # noqa: F811
# handler403 = Error403View.as_view()  # noqa: F811
# handler500 = Error500View.as_view()  # noqa: F811


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
        path("__reload__/", include("django_browser_reload.urls")),
    ]

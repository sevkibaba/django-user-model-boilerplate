from django.contrib import admin
from django.urls import path, include
from django.http import HttpRequest, HttpResponse


admin.site.site_title = admin.site.site_header = "Example App"


def health_check(request: HttpRequest) -> HttpResponse:
    return HttpResponse(content="OK", status=200)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check),
    path('users/', include('example_app.users.urls')),
    path('example-sub-app/', include('example_app.example_sub_app.urls')),

]

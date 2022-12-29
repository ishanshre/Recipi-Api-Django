from django.urls import path

from accounts import views

app_name = "accounts"
urlpatterns = [
    path("create/", views.UserCreateApiView.as_view(), name="create"),
]
from rest_framework.routers import DefaultRouter

from recipi import views

app_name="recipi"

router = DefaultRouter()

router.register("",views.RecipiViewSet)

urlpatterns = router.urls



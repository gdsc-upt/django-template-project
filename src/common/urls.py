from rest_framework.routers import DefaultRouter

from common.views import ExampleViewSet

router = DefaultRouter()
router.register("examples", ExampleViewSet)

common_urls = router.urls

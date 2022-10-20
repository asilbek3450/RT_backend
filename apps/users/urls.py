from rest_framework import routers
# from views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import UserViewSet


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls

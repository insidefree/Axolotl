from rest_framework.routers import DefaultRouter
from .views import *


ROUTER = DefaultRouter()
ROUTER.register(r'articles', ArticleViewSet)


urlpatterns = ROUTER.urls

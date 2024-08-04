from rest_framework.routers import DefaultRouter

from src.views.v1.statistic_views import StatisticViewSet

statistic_router = DefaultRouter()
statistic_router.register(r'statistic', StatisticViewSet)
from django.urls import path, include

from src.routers.statistic_routers import statistic_router
from src.routers.teacher_routers import teacher_router
urlpatterns = [
    path('v1/', include(teacher_router.urls)),
    path('v1/', include(statistic_router.urls))
]

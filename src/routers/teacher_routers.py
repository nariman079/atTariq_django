from rest_framework.routers import DefaultRouter

from src.views.v1.teacher_views import DisciplineViewSet, TeacherViewSet

teacher_router = DefaultRouter()
teacher_router.register(r'disciplines', DisciplineViewSet)
teacher_router.register(r'teachers', TeacherViewSet)


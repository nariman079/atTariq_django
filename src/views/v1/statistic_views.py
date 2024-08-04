from rest_framework.viewsets import ModelViewSet
from src.serializers.statistic_serializers import StatisticSerializer
from src.models import Statistic


class StatisticViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options']
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    pagination_class = None

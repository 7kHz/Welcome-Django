# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer


# @api_view(['GET'])
# def sensors_view(request):
#     sensors = Sensor.objects.all()
#     sensors_data = SensorDetailSerializer(sensors, many=True)
#     return Response(sensors_data.data)


class SensorsView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        sensors_data = SensorDetailSerializer(sensors, many=True)
        return Response(sensors_data.data)

    def post(self, request):
        eps40 = Sensor(id=4, name='EPS40', description='Балкон').save()
        add_eps40 = SensorDetailSerializer(eps40)
        return Response(add_eps40.data)


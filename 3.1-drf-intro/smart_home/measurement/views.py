# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.forms import model_to_dict
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer


class SensorsView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        sensors_data = SensorDetailSerializer(sensors, many=True)
        return Response(sensors_data.data)

    #
    def post(self, request):
        post_sensor = Sensor.objects.create(name=request.data['name'],
                                            description=request.data['description'])
        return Response({'post': model_to_dict(post_sensor)})

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorDetailSerializer(sensor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response({'patch': serializer.data})


class MeasurementView(APIView):
    def post(self, request):
        post_measurement = Measurement.objects.create(sensor_id=request.data['sensor_id'],
                                                      temperature=request.data['temperature'])
        return Response({'post': model_to_dict(post_measurement)})
    def __str__(self):
        return self.post()

    # def patch(self, request, *args, **kwargs):
    #     dh780 = Sensor(id=5)
    #     add_dh780 = SensorDetailSerializer(dh780)
    #     return Response(add_dh780.data)

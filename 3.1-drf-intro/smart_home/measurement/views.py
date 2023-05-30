from django.forms import model_to_dict
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorsSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorsView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        sensors_data = SensorsSerializer(sensors, many=True)
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
                                                      temperature=request.data['temperature']
                                                      )
        return Response({'post': model_to_dict(post_measurement)})


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.forms import model_to_dict
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

    #
    def post(self, request):
        post_sensor = Sensor.objects.create(name=request.data['name'],
                                            description=request.data['description'])
        return Response({'post': model_to_dict(post_sensor)})

    def patch(self, request):
        patch_sensor = Sensor.objects.update(name=request.data['name'],
                                             description=request.data['description'])
        return Response({'patch': model_to_dict(patch_sensor)})


class SensorCreate(CreateAPIView):
    serializer_class = SensorDetailSerializer

    def post(self, request, *args, **kwargs):
        dh780 = Sensor(id=5, name='DH780', description='Кладовка')
        add_dh780 = SensorDetailSerializer(dh780)
        return Response(add_dh780.data)


class SensorUpdate(RetrieveUpdateAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()

    def patch(self, request, *args, **kwargs):
        dh780 = Sensor(id=5)
        add_dh780 = SensorDetailSerializer(dh780)
        return Response(add_dh780.data)

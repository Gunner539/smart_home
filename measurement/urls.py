from django.urls import path

from measurement.views import SensorsList, SensorView, MeasurementView, MeasurementDetail, SensorChangeView

urlpatterns = [
    path('sensor/', SensorsList.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
    path('sensor/update/<pk>', SensorChangeView.as_view()),
    path('measurement/', MeasurementView.as_view()),
    path('measurement/<pk>/', MeasurementDetail.as_view()),
]


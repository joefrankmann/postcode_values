from django.urls import path
from postcodes.api.views import (OutcodeDetailsAPIView, OutcodeListCreateAPIView, 
                                NexusDetailsAPIView, NexusListCreateAPIView)

urlpatterns = [
    path('outcode/', OutcodeListCreateAPIView.as_view(), name='outcode-list'),
    path('outcode/<str:outcode_code>/', OutcodeDetailsAPIView.as_view(), name='outcode-details'),
    path('nexus/', NexusListCreateAPIView.as_view(), name='nexus-list'),
    path('nexus/<str:outcode_code>', NexusDetailsAPIView.as_view(), name='nexus-details'),
]
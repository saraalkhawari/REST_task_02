from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView
from datetime import datetime

from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer,  BookingDisplaySerializer, UpdateSerializer


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer

class BookingsDetail(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingDisplaySerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'object_id'

class BookingsUpdate(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = UpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'object_id'

class BookingsDelete(DestroyAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'object_id'

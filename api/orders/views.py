from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import Http404, HttpResponse
from django.core import serializers
import django_filters.rest_framework

from .serializers import OrderSerializer, OrderSpecifiedNIPSerializer
from .models import Order, Contractor

import json

class OrderViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing order instances.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'delete', 'patch', 'head']

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['contractor_id', 'implementation_date', 'data_of_placing_the_order', 'order_value', 'status']
    ordering_fields = ['implementation_date', 'data_of_placing_the_order', 'order_value']

class OrderSpecifiedNIPViewSet(viewsets.ViewSet):

    """
    A viewset for creating seo analysis.
    """

    @action(detail = False, methods = ['post'])
    def create(self, request, *args, **kwargs):

        serializer = OrderSpecifiedNIPSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        nip = serializer.validated_data['nip']

        orders = Order.objects.filter(contractor_id__nip = nip)

        if not orders:
            raise Http404

        data = serializers.serialize('json', orders)

        return HttpResponse(data, content_type="application/json")

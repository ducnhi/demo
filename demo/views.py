import time

from rest_framework import generics, status
from rest_framework.response import Response

from demo.models import OrderModels
from demo.serializers import OrderSerializers


class CreateOrder(generics.ListCreateAPIView):
    serializer_class = OrderSerializers

    def post(self, request, *args, **kwargs):
        try:
            serializer = OrderSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        obj = OrderModels.objects.all()
        output = []
        for item in obj:
            output.append({
                "seller_id": item.seller_id,
                "tracking_number":item.tracking_number,
                "country": item.country
            })
        return Response(data=output)
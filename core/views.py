from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from core.serializers import CreateDeviceSerializer
import boto3


class DeviceViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    def create(self, request, *args, **kwargs):
        serializer = CreateDeviceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(validated_data=serializer.validated_data)

        return Response({"detail": " Created"}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk, *args, **kwargs):
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("sajjad_devices")

        try:
            response = table.get_item(Key={"id": pk})
            item = response["Item"]
            return Response(item, status=status.HTTP_200_OK)
        except KeyError:
            raise NotFound

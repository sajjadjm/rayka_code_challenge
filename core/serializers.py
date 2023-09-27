from rest_framework import serializers
import boto3

class CreateDeviceSerializer(serializers.Serializer):
  id = serializers.CharField(required=True)
  deviceModel = serializers.CharField(required=True)
  name = serializers.CharField(required=True, max_length=255)
  note = serializers.CharField(required=True)
  serial = serializers.CharField(required=True)

  def create(self, validated_data):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table('sajjad_devices')

    table.put_item(Item=validated_data)

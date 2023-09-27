from rest_framework.test import APISimpleTestCase
from rest_framework import status
from rest_framework.reverse import reverse
from moto import mock_dynamodb
import boto3


class DevicesTestCase(APISimpleTestCase):
    def setUp(self):
        self.create_devices_url = reverse("devices-list")
        self.retrieve_device_url = reverse("devices-detail", kwargs={"pk": 1})

    def setup_mock_database(self):
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.create_table(
            TableName="sajjad_devices",
            KeySchema=[
                {"AttributeName": "id", "KeyType": "HASH"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "id", "AttributeType": "S"},
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 10, "WriteCapacityUnits": 10},
        )

        return table

    def test_create_device_valid(self):
        mock = mock_dynamodb()
        mock.start()

        self.setup_mock_database()
        data = {
            "id": "1",
            "deviceModel": "2",
            "name": "test",
            "note": "alkjsfglkajsg",
            "serial": "A100000113",
        }
        response = self.client.post(self.create_devices_url, data, format="json")
        mock.stop()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_device_invalid(self):
        mock = mock_dynamodb()
        mock.start()
        self.setup_mock_database()

        response = self.client.post(self.create_devices_url, {}, format="json")
        mock.stop()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_device_valid(self):
        mock = mock_dynamodb()
        mock.start()

        table = self.setup_mock_database()
        table.put_item(
            Item={
                "id": "1",
                "deviceModel": "2",
                "name": "test",
                "note": "alkjsfglkajsg",
                "serial": "A100000113",
            }
        )

        response = self.client.get(self.retrieve_device_url, format="json")
        mock.stop()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_device_not_found(self):
        mock = mock_dynamodb()
        mock.start()
        
        self.setup_mock_database()
        response = self.client.get(self.retrieve_device_url, format="json")
        mock.stop()

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

from rest_framework.serializers import ModelSerializer

from common.models import Example


class ExampleSerializer(ModelSerializer):
    class Meta:
        model = Example
        fields = "__all__"

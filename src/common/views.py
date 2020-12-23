from django.db.models import QuerySet
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from common.models import Example
from common.serializers import ExampleSerializer
from common.utils import create_swagger_info


@create_swagger_info(
    swagger_auto_schema(
        operation_id='Operation id',
        operation_description='Example description',
        operation_summary='Example operation summary',
        security=[],
        request_body=ExampleSerializer(),
        responses={status.HTTP_201_CREATED: ExampleSerializer()},
        tags=['Common'],
    )
)
class ExampleViewSet(ModelViewSet):
    serializer_class = ExampleSerializer
    queryset: QuerySet[Example] = Example.objects.filter(is_published=True)

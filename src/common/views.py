from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from common.models import Example
from common.serializers import ExampleSerializer
from common.utils import create_swagger_info


@create_swagger_info(
    extend_schema(
        operation_id="Operation id",
        description="Example description",
        summary="Example operation summary",
        auth=[],
        request=ExampleSerializer(),
        responses={status.HTTP_201_CREATED: ExampleSerializer()},
        tags=["Common"],
    )
)
class ExampleViewSet(ModelViewSet):
    serializer_class = ExampleSerializer
    queryset: QuerySet[Example] = Example.published.all()

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

many_delete_swagger = swagger_auto_schema(
    operation_description="Toplu silme işlemi",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'ids': openapi.Schema(type=openapi.TYPE_ARRAY,
                                  items=openapi.Items(type=openapi.TYPE_INTEGER))
        },
        required=['ids'],
    ),
    responses={204: 'No Content'},
)

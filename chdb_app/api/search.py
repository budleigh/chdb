from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.serializers import serialize
from chdb_app.models import *


@require_POST
def search(request):
    query = request.POST['query']

    return JsonResponse(
        serialize('json', Entity.objects.filter(name__icontains=query)),
        status=200,
        safe=False  # serializing lists...not sure why this is necessary.
    )

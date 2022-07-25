from django.http import JsonResponse
from .models import User


def index(request):
    doc = User.objects.get(id=1)
    print(doc.id)
    return JsonResponse({
        'code': 200,
        'msg': 'success'
    })

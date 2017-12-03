from django.shortcuts import render_to_response
from .models import Category
from django.http import HttpResponseBadRequest
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse

def show_cats(request):
    return render_to_response("cats.html",
                          {'nodes':Category.objects.all()})


@api_view(['POST'])
def set_user_type(request):

    if request.user.is_authenticated():

        try:
            data = request.data
        except ValueError:
            return HttpResponseBadRequest()

        if data.get('type') == None:
            return HttpResponseBadRequest()

        user = request.user

        user.type = data['type']

        user.save()

        return JsonResponse({})



from django.conf import settings
from django.shortcuts import render, redirect, resolve_url
from django.db import IntegrityError, connection
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# Create your views here.


def transaction_log(request):
    return render(request, 'views/layouts/pages/transaction_log.html')

def load_collection_history(request):
    cursor = connection.cursor()
    cursor.callproc("SP_SELECT_COLLECTION_LOG"
                    ,(request.POST['range'],))
    data = cursor.fetchall()
    return JsonResponse(data, safe=False)
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def helloWorld(request):
    return JsonResponse({
        "status":"Success",
        "message":"Hello World!, you have been logged in"
    })

def GoodByeWorld(request):
    return JsonResponse({
        "status":"Success",
        "message":"Hello World!, you have been logged out"
    })
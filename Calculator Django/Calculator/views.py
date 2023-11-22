from django.http import JsonResponse

# note: implement this file inside of Calculator/views.py
def add(request):
    x = float(request.GET.get('x', 0))
    y = float(request.GET.get('y', 0))
    result = x + y
    return JsonResponse({"result": result})

def subtract(request):
    x = float(request.GET.get('x', 0))
    y = float(request.GET.get('y', 0))
    result = x - y
    return JsonResponse({"result": result})

def multiply(request):
    x = float(request.GET.get('x', 0))
    y = float(request.GET.get('y', 0))
    result = x * y
    return JsonResponse({"result": result})

def divide(request):
    x = float(request.GET.get('x', 0))
    y = float(request.GET.get('y', 0))

    if y != 0:
        result = x / y
        return JsonResponse({"result": result})
    else:
        return JsonResponse({"error": "Cannot divide by zero"})

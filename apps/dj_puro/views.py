from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Category


def category_list(request):
    MAX_OBJECTS = 20
    cat = Category.objects.all()[:MAX_OBJECTS]
    data = {"results": list(cat.values('description', 'active'))}
    return JsonResponse(data)


def category_detail(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    data = {
        "results": {
            "description": cat.description,
            "active": cat.active,            
        }
    }
    return JsonResponse(data)
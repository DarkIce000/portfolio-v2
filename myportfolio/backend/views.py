from django.shortcuts import render
from django.http import JsonResponse
import json

def about_view(request):
    return JsonResponse({'success': 'installation successfull'})


def projects_view(request):
    return JsonResponse({'success': 'installation successfull'})


def experiences_view(request):
    return JsonResponse({'success': 'installation successfull'})


def certifications_view(request):
    return JsonResponse({'success': 'installation successfull'})


def tools_and_technologies_view(request):
    return JsonResponse({'success': 'installation successfull'})

def socials_view(request):
    return JsonResponse({'success': 'installation successfull'})

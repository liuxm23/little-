from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Person
import random

def random_person(request):
    people = list(Person.objects.all())
    if people:
        person = random.choice(people)
        data = {
            'name': person.name,
            'student_id': person.student_id,
            'class': person.class_name,
            'catchphrase': person.catchphrase if person.catchphrase is not None else '无'
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'No data found'}, status=404)
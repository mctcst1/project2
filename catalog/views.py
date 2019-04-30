from django.shortcuts import render
from catalog import models


def index(request):
 return render(request, 'index.html', {'name': models.Test.name, 'degree': models.Test.degrees})

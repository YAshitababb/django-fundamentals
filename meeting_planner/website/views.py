from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

# Create your views here.
def welcome(request):
  return render(request, "website/welcome.html",
                context={"meetings": Meeting.objects.all()})

def about(request):
  return HttpResponse("Hello, My name is Tatsu.")

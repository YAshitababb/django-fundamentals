from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
  return render(request, "website/welcome.html",
                context={"message": "This data was sent from the view to the template."})

def about(request):
  return HttpResponse("Hello, My name is Tatsu.")

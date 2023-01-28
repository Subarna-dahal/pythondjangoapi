
from django.http import HttpResponse

def home_page(request):
    print("home page request")
    friends=[
             'ram',
             'hari',
             'sita',


    ]
    return HttpResponse("this is home page")

from django.http import HttpResponse
from django.contrib.auth import login, logout,authenticate


def view_a(request):
    return HttpResponse("in view a")

def view_b(request):
    return HttpResponse("in view b")

def new_line(request):
    pass

def emp_pf_details(request):
    pass


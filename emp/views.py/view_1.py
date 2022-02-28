from django.http import HttpResponse


def view_a(request):
    return HttpResponse("in view a")

def view_b(request):
    return HttpResponse("in view b")
from django.http import HttpResponse


def list(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, player_id):
    return HttpResponse("You're looking at question %s." % player_id)

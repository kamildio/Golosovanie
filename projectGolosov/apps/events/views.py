from django.shortcuts import render

def eventsAll(request):

    return render(request, "events/events.html")

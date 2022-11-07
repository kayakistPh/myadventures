from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('log_trip.html')
    return HttpResponse(template.render())

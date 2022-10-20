"""
new application
"""
from django.http import HttpResponse

def index(request):
    """
    Main application
    """
    return HttpResponse('Hello world!')


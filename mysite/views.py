"""
new application
"""
from django.http import HttpResponse

def index(_request):
    """
    Main application
    """
    return HttpResponse('Hello world!')

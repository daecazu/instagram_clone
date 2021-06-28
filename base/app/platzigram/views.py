"""
Platzigram views
"""
# Django
from django.http import HttpResponse


# Utilities
from datetime import datetime
import remote_pdb
import json

def hello_world(request):
    """Return a gretting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hello, world! current server time {now}')


def sort_integers(request):
    """
    returns a json response with sorted integers
    """
    try:
        numbers = request.GET['numbers'].split(',')
        numbers = list(map(lambda number: int(number),numbers))
        sorted_numbers = sorted(numbers)
        # remote_pdb.set_trace(host='0.0.0.0', port=4444)
        data = {
            'status': 'ok',
            'numbers': sorted_numbers,
            'message': 'sorted numbers'
        }
        response = HttpResponse(
            json.dumps(data, indent=4),
            content_type='application/json'
        )
        return response
    except:
        return HttpResponse('Hi!')

def say_hi(request, name, age):
    """Returns a greeting"""
    if age <= 12:
        message = f'Sorry {name} you are not allowed here'
    else:
        message =f'Welcome to platzigram {name}'
    return HttpResponse(message)
    
"""posts views"""

# Django
from django.http import HttpResponse


def list_posts(request):
    posts = [1,2,3]
    return HttpResponse(str(posts))

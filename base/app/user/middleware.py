""" Platzigram middleware catalog"""
# Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware():
    """
    User completion middleware
    Ensure every user that is interacting with the platform
    have their profile pricture and biography.
    """

    def __init__(self, get_response):
        """middleware init"""
        self.get_response = get_response

    def __call__(self, request):
        """
        code to be executed for each request before the view
        is called.
        """
        if not request.user.is_anonymous:
            user = request.user
            if not user.picture or not user.biography:
                urls = [
                    reverse('users:update_profile'),
                    reverse('users:logout')
                ]
                if request.path not in  urls:
                    return redirect('users:update_profile')
        
        response = self.get_response(request)
        return response
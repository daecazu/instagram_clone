"""user views"""

# Django
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect

# Django DRF
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSerializer

# Exceptions
from django.db.utils import IntegrityError

# utilities
import remote_pdb


def update_profile(request):
    """update profile"""
    return render(request, 'users/update_profile.html')


def login_view(request):
    """login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request, 
            username=username,
            password=password
        )
        if user:
            login(request, user)
            return redirect('/posts/')
        else:
            return render(
                request,
                'users/login.html',
                {'error': 'Invalid username or password'} 
            )
           
            
        # remote_pdb.set_trace(host='0.0.0.0', port=4444)
    return render(request, 'users/login.html')

def signup(request):
    """sign up view"""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        if password != password_confirmation:
            return render(
                request,
                'users/signup.html',
                {'error': 'password confirmation does not match'}
            )
        try:
            get_user_model().objects.create_user(
                email=email,
                password=password
            )
        except IntegrityError:
            return render(
                request,
                'users/signup.html',
                {'error': 'email already in use'}
            )

        return redirect("users:login")
    return render(request, 'users/signup.html')

@login_required
def logout_view(request):
    """Logout a user """
    logout(request)
    return redirect('/users/login/')

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new token for a user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""

        return self.request.user

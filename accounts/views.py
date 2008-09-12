from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.template import RequestContext
from django.shortcuts import render_to_response

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField()
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            u = User.objects.get(email=email)
        except User.DoesNotExist:
            pass
        else:
            raise forms.ValidationError("This email already has an account.")
        
    def save(self, commit=True):
        user = super(UserCreationFormWithEmail, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

def register(request):
    ctx = RequestContext(request, {}) # Just to make later code shorter...
    
    # Don't allow users to create accounts if they're already logged in.
    if request.user.is_authenticated():
        return render_to_response("registration/account_already_exists.html", {}, ctx)
        
    # Handle the form
    if request.method == "POST":
        form = UserCreationFormWithEmail(request.POST)
        if form.is_valid():
            # Create, authenticate, and log in the new user.
            user = form.save()
            user = auth.authenticate(username=user.username, password=request.POST["password1"])
            auth.login(request, user)
            return render_to_response("registration/account_created.html", {}, ctx)
    else:
        form = UserCreationFormWithEmail()
    
    return render_to_response("registration/register.html", {"form" : form}, ctx)
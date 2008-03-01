from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import oldforms
from django.core.validators import ValidationError
from django.template import RequestContext
from django.shortcuts import render_to_response

class UserCreationFormWithEmail(UserCreationForm):
    def __init__(self):
        UserCreationForm.__init__(self)
        self.fields += (oldforms.EmailField(field_name="email", validator_list=[self.isUniqueEmail]),)
    
    def isUniqueEmail(self, field_data, all_data):
        try:
            u = User.objects.get(email=field_data)
        except User.DoesNotExist:
            pass
        else:
            raise ValidationError("This email already has an account.")
        
    def save(self, data):
        return User.objects.create_user(data['username'], data['email'], data['password1'])

def register(request):
    ctx = RequestContext(request, {}) # Just to make later code shorter...
    
    # Don't allow users to create accounts if they're already logged in.
    if request.user.is_authenticated():
        return render_to_response("registration/account_already_exists.html", {}, ctx)
        
    # Handle the form
    manipulator = UserCreationFormWithEmail()
    if request.method == "POST":
        data = request.POST.copy()
        errors = manipulator.get_validation_errors(data)
        if not errors:
            # Create, authenticate, and log in the new user.
            u = manipulator.save(data)
            u = auth.authenticate(username=u.username, password=data["password1"])
            auth.login(request, u)
            return render_to_response("registration/account_created.html", {}, ctx)
    else:
        data, errors = {}, {}
    
    form = oldforms.FormWrapper(manipulator, data, errors)
    return render_to_response("registration/register.html", {"form" : form}, ctx)
# Create your views here.
from django.shortcuts import *

from django.contrib.auth.decorators import login_required

from api.models import ApiKey
from api.forms import APIKeyForm

@login_required
def add_key(request):
    submitted = False
    if request.method == 'POST':  # If the form has been submitted...
        form = APIKeyForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            submitted = True
            login(request, user)
            render_dict = {}
            render_dict["logged_in"] = request.user.is_authenticated()
            render_dict["title"] = "Registration Complete"
            return render_to_response("registration/registration_complete.html", render_dict,  context_instance=RequestContext(request))
    else:
        form = RegisterForm()  # An unbound form

    render_dict = {'form': form}
    render_dict["submitted"] = submitted
    render_dict["logged_in"] = request.user.is_authenticated()
    render_dict["title"] = "Register"
    return render_to_response("registration/registration.html", render_dict,  context_instance=RequestContext(request))

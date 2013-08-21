import evelink

from django.shortcuts import *
from django.contrib.auth import logout
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from api.models import ApiKey

from forms import RegisterForm


def custom_logout(request):
    logout(request)
    return HttpResponseRedirect("../../accounts/login")


def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("../../accounts/profile")
    else:
        return login(request)


@csrf_exempt
@login_required
def profile(request):
    render_dict = {}
    render_dict["title"] = "Register"
    render_dict["user"] = request.user.first_name
    render_dict["logged_in"] = request.user.is_authenticated()
    render_dict["api_keys"] = ApiKey.objects.filter(user=request.user)

    return render_to_response("registration/profile.html", render_dict,  context_instance=RequestContext(request))


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("../../accounts/profile")
    submitted = False
    if request.method == 'POST':  # If the form has been submitted...
        form = RegisterForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            user = form.save()
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

from django.shortcuts import render
from light.forms import RegistrationForm
from django.views.generic import FormView


def index(request):
    context = {}
    return render(request, 'base.html', context)


class LightCommandView(FormView):
    template_name = 'command.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print("in form valid")
        form.send_email()
        return super().form_valid(form)

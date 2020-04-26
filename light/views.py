from django.shortcuts import render
from light.forms import CommandForm
from django.views.generic import FormView


from django.http import JsonResponse
from django.views.generic.edit import CreateView

class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


def index(request):
    context = {}
    return render(request, 'base.html', context)


class LightCommandView(FormView):
    success_url = '#'
    template_name = 'command.html'
    form_class = CommandForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(form.cleaned_data)
        return super().form_valid(form)


class LightCommandViewAjax(AjaxableResponseMixin, LightCommandView):
    pass

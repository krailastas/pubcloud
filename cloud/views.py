from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from .tasks import send_to_cloud
from .forms import PubCloudForms


class PubCloudViews(FormView):
    form_class = PubCloudForms
    template_name = 'pub_cloud.html'

    def form_valid(self, form):
        if settings.DEBUG:
            send_to_cloud(form.cleaned_data)
        else:
            send_to_cloud.delay(form.cleaned_data)
        return HttpResponseRedirect(reverse_lazy('pub_cloud'))

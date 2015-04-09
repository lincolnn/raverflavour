from django.shortcuts import render

import stripe

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import StripeForm


class StripeMixin(object):
    def get_context_data(self, **kwargs):
        context = super(StripeMixin, self).get_context_data(**kwargs)
        context['publishable_key'] = settings.STRIPE_PUBLIC_KEY
        return context


class SuccessView(TemplateView):
    template_name = 'thank_you.html'


class SubscribeView(StripeMixin, FormView):
    template_name = 'subscribe.html'
    form_class = StripeForm
    success_url = reverse_lazy('thank_you')

    def form_valid(self, form):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        customer_data = {
            'description': 'Some Customer Data',
            'card': form.cleaned_data['stripe_token']
        }
        customer = stripe.Customer.create(**customer_data)

        customer.subscriptions.create(plan="raverflavour")

        return super(SubscribeView, self).form_valid(form)
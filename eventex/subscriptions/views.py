from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.model import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    # Verifications if form is valid
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    subscription = Subscription.objects.create(**form.cleaned_data)

    # Send email
    _send_mail('Confirmação de inscrição', settings.DEFAULT_FROM_EMAIL, subscription.email,
               'subscriptions/subscription_email.txt', {'subscription': subscription})

    return HttpResponseRedirect('/inscricao/{}/'.format(subscription.pk))


def new(request):
    context = {'form': SubscriptionForm()}

    return render(request, 'subscriptions/subscription_form.html', context)


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscriptions/subscription_details.html', {'subscription': subscription})

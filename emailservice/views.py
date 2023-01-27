# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.template.loader import render_to_string

from emailservice.forms import ContactForm
from emailservice.models import Contact
from emailservice.service import send
from .tasks import send_spam_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = r'^email/'
    template_name = 'emailservice/contact.html'

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        send_spam_email.delay(form.instance.email)
        return super(ContactView, self).form_valid(form)


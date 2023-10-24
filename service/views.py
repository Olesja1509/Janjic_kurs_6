import random
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Article
from service.forms import MailingForm, ClientForm
from service.models import Mailing, Logs, Client
from service.services import send_email


# Контроллеры для класса Mailing

class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    extra_context = {
        'title': 'Сервис рассылок'
    }

    def get_queryset(self):
        qs = super().get_queryset()

        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = random.sample(list(Article.objects.all()), 3)

        qs = super().get_queryset()
        context['mailing_count'] = qs.filter(user=self.request.user).count()
        context['active_mailing_count'] = qs.filter(user=self.request.user).exclude(status='завершена').count()
        context['clients_count'] = Client.objects.filter(user=self.request.user).count()
        return context


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logs_mailing'] = Logs.objects.filter(title=self.object.title)
        return context


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'service.add_mailing'
    success_url = reverse_lazy('service:index')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['clients'].queryset = Client.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        email_list = [cl for cl in self.object.clients.all()]

        if self.object.start_time <= timezone.now():
            send_email(self.object.title, self.object.body, email_list)

        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'service.change_mailing'
    success_url = reverse_lazy('service:index')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['clients'].queryset = Client.objects.filter(user=self.request.user)
        return form


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('service:index')
    permission_required = 'service.delete_mailing'


# Контроллеры для класса Client

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    extra_context = {
        'title': 'Все клиенты'
    }

    def get_queryset(self):
        qs = super().get_queryset()

        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)

        return qs


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    permission_required = 'service.add_client'
    success_url = reverse_lazy('service:clients')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    permission_required = 'service.change_client'
    success_url = reverse_lazy('service:clients')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('service:clients')
    permission_required = 'service.delete_client'

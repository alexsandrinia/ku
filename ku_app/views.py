# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import ClientForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Client
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import os
from docxtpl import DocxTemplate

from django.urls import reverse

class ClientCreateView(LoginRequiredMixin, CreateView):
	model = Client
	fields = ['FIO_Client', 'INN_Client', 'Phone_Client']
	success_url = '/client/add'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class ClientListView(LoginRequiredMixin, ListView):
	model = Client

	def get_queryset(self):
		if self.request.user.is_staff:
			return Client.objects.all()
		return Client.objects.filter(author = self.request.user)

def base_view(request):
	context = {}
	return render(request, 'base.html', context)

def create_docx_document1(request):
	form = ClientForm(request.POST or None)
	if form.is_valid():
		FIO_Client = form.cleaned_data['FIO_Client']
		Phone_Client = form.cleaned_data['Phone_Client']
		INN_Client = form.cleaned_data['INN_Client']

		if request.POST:
			if 'doc1' in request.POST:
				doc = DocxTemplate(os.path.abspath('templates/my_word_template.docx'))
				context = { 
					'FIO_Client' : FIO_Client,
					'Phone_Client': Phone_Client
					}
				doc.render(context)
				response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
				response['Content-Disposition'] = 'attachment; filename=test_doc.docx'
				doc.save(response)
				return response
				return HttpResponseRedirect(reverse('base'))
			elif 'doc2' in request.POST:
				doc = DocxTemplate(os.path.abspath('templates/my_word_template2.docx'))
				context = { 
					'FIO_Client' : FIO_Client,
					'Phone_Client': Phone_Client
					}
				doc.render(context)
				response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
				response['Content-Disposition'] = 'attachment; filename=test_doc2.docx'
				doc.save(response)
				return response
				return HttpResponseRedirect(reverse('base'))
			elif 'save_data' in request.POST:
				new_client = Client()
				new_client.author = request.user
				new_client.save()
				new_client.FIO_Client = FIO_Client
				new_client.Phone_Client = Phone_Client
				new_client.INN_Client = INN_Client
				new_client.save()
				return HttpResponseRedirect(reverse('save_data'))
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from models import Enquete

@login_required(login_url='/login/')
def cadastra_enquete(request):
	
	context = {}
	context['username'] = request.user.username

	if request.POST:
		X = request.POST.get('pergunta')
		context['pergunta'] = X

		Enquete.objects.create(
			pergunta = X,
			autor = request.user
		)

	return render(request, 'adiciona_enquete.html',context)

@login_required(login_url='/login/')
def mostra_enquetes(request):
	
	context = {}
	context['username'] = request.user.username
	context['enquetes'] = Enquete.objects.all()
	
	#import ipdb;ipdb.set_trace()

	return render(request, 'mostra_enquetes.html',context)



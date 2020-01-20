from django.shortcuts import render,  get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Noticia
from .forms import NotForm
from .forms import Area
from .forms import AreaForm

def not_list(request):
	noticias=Noticia.objects.all()
	return render(request, 'noticia/not_list.html', {'noticias':noticias})
	
def detalhesdasnot(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)
	return render(request, 'noticia/detalhesdasnot.html', {'noticia' : noticia})

def nova_not(request):
	if request.method == "POST":
		form = NotForm(request.POST, request.FILES)
		if form.is_valid():
			noticia = form.save(commit=False)
			noticia.autor = request.user
			noticia.save()
			return redirect('detalhesdasnot', pk=noticia.pk)
			
	else:	
		form = NotForm()
	return render(request, 'noticia/not_edit.html', {'form': form})

def not_edit(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)
	if request.method == "POST":
		form = NotForm(request.POST, request.FILES, instance=noticia)
		if form.is_valid():
			noticia = form.save(commit=False)
			noticia.autor = request.user	
			noticia.save()
			return redirect('detalhesdasnot', pk=noticia.pk)
			
	else:	
		form = NotForm(instance=noticia)
	return render(request, 'noticia/not_edit.html', {'form': form})

def publicar(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)
		
	noticia.publish()
	return redirect('detalhesdasnot', pk=noticia.pk)
			
def remover_not(request, pk):
	noticia = get_object_or_404(Noticia,pk=pk)
	noticia.delete()
	return redirect('not_list')

# Create your views here.
def area_list(request):
	areas=Area.objects.all()
	return render(request, 'area/area_list.html', {'areas':areas})

def detalhesdaarea(request, pk):
	area = get_object_or_404(Area, pk=pk)
	return render(request, 'area/detalhesdaarea.html', {'area' : area})

def nova_area(request):
	if request.method == "POST":
		form = AreaForm(request.POST)
		if form.is_valid():
			area = form.save(commit=False)
			area.save()
			return redirect('detalhesdaarea', pk=area.pk)
			
	else:	
		form = AreaForm()
	return render(request, 'area/area_edit.html', {'form': form})

def area_edit(request, pk):
	area = get_object_or_404(Area, pk=pk)
	if request.method == "POST":
		form = AreaForm(request.POST, instance=area)
		if form.is_valid():
			area = form.save(commit=False)
			area.save()
			return redirect('detalhesdaarea', pk=area.pk)
			
	else:	
		form = AreaForm(instance=area)
	return render(request, 'area/area_edit.html', {'form': form})

def ativar(request, pk):
	area = get_object_or_404(Area, pk=pk)
	area.ativar()
	area.save()
def desativar(request, pk):
	area = get_object_or_404(Area, pk=pk)
	area.desativar()
	area.save()
			
def remover_area(request, pk):
	area = get_object_or_404(Area,pk=pk)
	area.delete()
	return redirect('area_list')
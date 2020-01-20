from django.db import models
from django.utils import timezone
import datetime

class Area(models.Model):
	descricao = models.CharField(max_length=300, null=False)
	cor = models.CharField(max_length=300, null=False)
	status = models.BooleanField(null=False)
	def __str__(self):
		return self.descricao	
	def ativar(self):
		self.status = True
	def desativar(self):
		self.status = False

class Noticia(models.Model):
	autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=200, null=False)
	area = models.ForeignKey('Area', on_delete=models.SET_NULL, null=True)
	texto = models.TextField(null=False)
	foto = models.ImageField(upload_to='imagens/', null=True,blank=True)
	data_publicacao = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.data_publicacao = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo


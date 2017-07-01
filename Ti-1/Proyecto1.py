import os, shutil
from PIL import Image


class CLasificador:
	def __init__(self):

		self.lista=[]

	def revisar(self):
		if os.path.isdir(os.path.dirname(os.path.realpath(__file__))+'/etiquetado_imagenes')==True:
			if os.path.isfile(os.path.dirname(os.path.realpath(__file__))+'/etiquetado_imagenes/informacion.txt'):
				informacion=open(os.path.dirname(os.path.realpath(__file__))+'/etiquetado_imagenes/informacion.txt','r')
				for linea in informacion:
					archivo,etiqueta,comentario=linea.split()
					if os.path.isfile(os.path.dirname(os.path.realpath(__file__))+'/etiquetado_imagenes/'+archivo):
						self.lista.append(Etiqueta(os.path.dirname(os.path.realpath(__file__))+'/etiquetado_imagenes/'+archivo,etiqueta,comentario))
					else:
						pass
			else:
				print 'falta archivo de informacion'
		else:
			pass

	def agregar_imagenes(self,carpeta):
		try:
			os.mkdir(os.path.dirname(os.path.realpath(__file__))+'/etiquetado_imagenes')
		except:
			pass
		guardado=os.path.dirname(os.path.realpath(__file__))+'/etiquetado_imagenes'
		informacion=open(guardado+'/'+'informacion.txt','a')
		if os.path.exists(carpeta)==True:
			if os.path.isdir(carpeta)==True:
				for archivo in os.listdir(carpeta):
					if os.path.isfile(carpeta+'/'+archivo)==True:
						if archivo.lower().endswith(('.png', '.jpg', '.gif')):
							ver=Image.open(carpeta+'/'+archivo)
							ver.show()
							etiqueta=raw_input('Etiqueta ')
							comentario=raw_input('Comenatario ')
							shutil.copy2(carpeta+'/'+archivo,guardado)
							self.lista.append(Etiqueta(guardado+'/'+archivo,etiqueta,comentario))
							informacion.write(archivo+' '+etiqueta+' '+comentario+'\n')
						else:
							pass
					elif os.path.isdir(carpeta+'/'+archivo)==True:
						self.agregar_imagenes(carpeta+'/'+archivo)
					else:
						pass
			else:
				print 'la ruta no pertenece a una carpeta'
		else:
			print 'la carpeta no existe'
		informacion.close()

	def contar_etiquetas(self):

		etiquetas={}
		for i in self.lista:
			if i.etiqueta in etiquetas:
				etiquetas[i.etiqueta]+=1
			else:
				etiquetas[i.etiqueta]=1
		return etiquetas

	def mostrar_imagenes(self):
		for i in self.lista:
			nombre=i.ruta.split('/')[-1]
			print nombre,':',i.etiqueta
			print 'comentario:'+i.comentario
			ver=Image.open(i.ruta)
			ver.show()
			raw_input('Siguiente (enter)')

class Imagen:
	def __init__(self,ruta,etiqueta,comentario):
		self.ruta=ruta
		self.etiqueta=etiqueta
		self.comentario=comentario

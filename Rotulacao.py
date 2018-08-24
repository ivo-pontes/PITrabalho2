#!/usr/bin/env python3
# -*- coding: utf-8 -*

from PIL import Image
import numpy as np


class Rotulacao():

	def __init__(self, nome_imagem):
		self.nome_imagem = nome_imagem
		self.m = 0
		self.n = 0
		self.matriz = []
		self.img = []

	'''
	Abrindo o arquivo e pegando dimensões MxN
	'''
	def carregarImagem(self):
		img = Image.open(self.nome_imagem)
		self.img = img
		#Converte Imagem Object para Matriz
		self.matriz = np.asarray(img.convert('L'))
		#Dimensão M
		self.m = np.size(self.matriz, 0)	
		#Dimensão N
		self.n = np.size(self.matriz, 1)
		print("Linhas: {}\nColunas: {}\n".format(self.m, self.n))
		print(self.matriz)

	'''
	Executar
	'''
	def executar(self):
		m = np.zeros([self.m,self.n])
		m1 = np.size(m, 0)
		n1 = np.size(m, 1)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))

		#B&W
		#Ternário em Python
		m1 = self.m if self.m%2==0 else self.m-1
		n1 = self.n if self.n%2==0 else self.n-1

		for i in range(m1):
			for j in range(n1):
				if self.matriz[i][j] < 127:
					m[i][j] = 1
				else:
					m[i][j] = 0

		print("Matriz B&W:")
		print(m)
		x = Image.fromarray(m)
		#x.show()

		labels = self.gerarLabels()
		#print(labels)
		label = 0
		rotulos = np.chararray((m1, n1),unicode=True)

		#print(rotulos)
		for i in range(m1):
			for j in range(n1):
				rotulos[i][j] = str(m[i][j])

		print(rotulos)

		for i in range(m1):
			for j in range(n1):
				#p = self.matriz[i][j]
				r = j-1
				t = i-1
				
				if i == 0 and j == 0: #primeira linha, primeria coluna
					if m[i][j] == 1:
						rotulos[i][j] = labels[label]
						label += 1
				elif i == 0 and m[i][j] == 1: # primeira linha, preto
					if m[i][r] == 1:
						rotulos[i][j] = labels[label-1]
					else:
						rotulos[i][j] = labels[label]
						label += 1
				elif m[i][j] == 1: #linha > 0, preto
					if j == 0:
						if m[t][j] == 1:
							rotulos[i][j] = labels[label-1]
						else:
							rotulos[i][j] = labels[label]
							label += 1
					elif m[t][j] == 1 or m[i][r] == 1:
						rotulos[i][j] = labels[label-1]
					else:
						rotulos[i][j] = labels[label]
						label += 1

		print("Matriz Rotulada:")

		for i in range(len(rotulos)):
			for j in range(len(rotulos[i])):
				if rotulos[i][j] == '0':
					print(" ", end='')
				else:
					print("{}".format(rotulos[i][j]), end='')
			print("")

		#print(rotulos)
		#imagem = Image.fromarray(rotulos)
		#self.img.show()		
		#imagem.show()

	def gerarLabels(self):
		return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

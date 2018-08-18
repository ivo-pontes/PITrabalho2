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
		self.m = np.size(self.matriz, 1)
		#Dimensão N
		self.n = np.size(self.matriz, 0)
		print("Linhas: {}\nColunas: {}\n".format(self.m, self.n))
		print(self.matriz)

	'''
	Executar
	'''
	def executar(self):
		saida = np.zeros([self.m,self.n])
		m1 = np.size(saida, 1)
		n1 = np.size(saida, 0)
		print("Linhas: {}\nColunas: {}\n".format(m1,n1))

		#B&W
		for i in range(m1):
			for j in range(n1):
				if self.matriz[i][j] < 127:
					saida[i][j] = 0
				else:
					saida[i][j] = 255

		labels = []
		label = 0
		for i in range(m1):
			for j in range(n1):
				#p = self.matriz[i][j]
				r = saida[i][j-1]
				s = saida[i-1][j]

				if i > 0 and saida[i][j] == 0:
					pass
				if saida[i][j] == 1:
					if r == 0 and s == 0:
						saida[i][j] = self.letters[label]
						label += 1
					elif r == 1 or s == 1:
						label.append(label)
					elif r == 1 and s == 1:
						pass
					
					
		print(saida)
		imagem = Image.fromarray(saida)
		self.img.show()		
		imagem.show()

	def gerarLabels(self):
		self.letters = "ABCDEFGHIJKLMNOPQRSTUVXYWZ"
		print(self.letters[3])
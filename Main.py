#!/usr/bin/env python3
# -*- coding: utf-8 -*

from Rotulacao import Rotulacao

if __name__ == '__main__':
	print("Processamento de Imagens.")

	rotulacao = Rotulacao("img/quadrados.png")
	rotulacao.carregarImagem()
	op = -1

	menuStr = "\n\nDigite 0 para sair.\nMenu:\n"
	menuStr += "Vizinho Mais Próximo\n1 - Por Redução\n2 - Por Ampliação\n"

	while op != 0:
		op = input(menuStr)
		op = int(op)
		if op == 1:
			rotulacao.executar()
			
	print("Fim execução!!")

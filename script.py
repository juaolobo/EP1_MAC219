import os
import re

path = './results/'
dirs = os.listdir(path)

content = f'Tamanho,Tempo,Desvio,Imagem,Threads,Programa\n'
for d in dirs:
	files = os.listdir(path + d)
	for f in files:
		full_path = path + d + '/' + f 
		if '_parsed' not in f:
			with open(full_path, "r") as f_:
				data = f_.readline()
				entradas = ["16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192"]
				i = 0
				while data: 
					data = f_.readline()
					if 'time elapsed' in data:
						data = data.replace(",", ".")
						data_ = data.split()
						regex = re.findall(r'(\w+?)(\d+)', f)

						try:
							num = regex[0][1]
							filename = regex[0][0]
						except:
							filename = f.replace('.log', '')
							num = '1'
							pass
						print(filename, num)
						content += entradas[i] + ',' + data_[0] + ',' + data_[2] + ',' + filename + ',' + num + ',' + d +'\n'
						i +=1

with open('/home/hiroshi/Área de Trabalho/EPs e Exercícios/Paralela/EP1_MAC219' + '/all_files.csv', "w") as wr:
	wr.write(content)



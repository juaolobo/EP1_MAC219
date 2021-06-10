import os

path = './results/'
dirs = os.listdir(path)

for d in dirs:
	files = os.listdir(path + d)
	for f in files:
		full_path = path + d + '/' + f 
		with open(full_path, "r") as f_:
			new_lines = ''
			data = f_.readline()
			while data: 
				data = f_.readline()
				if 'time elapsed' in data:
					data = data.replace(",", ".")
					data_ = data.split()
					content = data_[0] + ' ' + data_[2] + '\n'
					new_lines += content
			with open(full_path.replace('.log', '_parsed.log'), "w") as wr:
				wr.write(new_lines)



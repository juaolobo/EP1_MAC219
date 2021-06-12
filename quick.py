import os

path = './results/'
dirs = os.listdir(path)

for d in dirs:
	files = os.listdir(path + d)
	print(files)
	print(len(files)/2)
	
	for f in files:
		full_path = path + d + '/'
		full_ = full_path + f
		if 'full6' in f:
			new_f = f.replace("full6", "full16")
			os.rename(full_, full_path + new_f)

		elif 'elephant6'  in f:
			new_f = f.replace("elephant6", "elephant16")
			os.rename(full_, full_path + new_f)

		elif 'seahorse6'  in f:
			new_f = f.replace("seahorse6", "seahorse16")
			os.rename(full_, full_path + new_f)

		elif 'triple_spiral6'  in f:
			new_f = f.replace("triple_spiral6", "triple_spiral16")
			os.rename(full_, full_path + new_f)

		# if 'full1'  in f:
		# 	new_f = f.replace("full1", "full")
		# 	os.rename(full_, full_path + new_f)

		# elif 'elephant1'  in f:
		# 	new_f = f.replace("elephant1", "elephant")
		# 	os.rename(full_, full_path + new_f)

		# elif 'seahorse1'  in f:
		# 	new_f = f.replace("seahorse1", "seahorse")
		# 	os.rename(full_, full_path + new_f)

		# elif 'triple_spiral1'  in f:
		# 	new_f = f.replace("triple_spiral1", "triple_spiral")
		# 	os.rename(full_, full_path + new_f)

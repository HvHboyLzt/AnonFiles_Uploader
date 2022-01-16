from anonfile import AnonFile
import os


anon = AnonFile()
files = os.listdir('./upload/')
result = open('result.txt', 'w')
s = len(files)
j = 0

while j < s:
	file = './upload/' + files[j]
	upload = anon.upload(file, progressbar = False)
	print('\033[32m{}'.format("Uploaded: \033[0m") + upload.url.geturl())
	j = j + 1
	result.write(upload.url.geturl() + '\n')

print('\033[1m{}'.format("All files uploaded!\nCoded with love by HvHboy!"))

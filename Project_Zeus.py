"""
Auther: N00DL3S
Version: V1
GitHub: https://github.com/B1GN00DL3S
"""
import os

Error = ["Error File Does Not Exist.","Error Folder Does Not Exist"]

def File(file):
	try:
		open(file,"rt")
	except:
		return(Error[0])
	else:
		FileLen = len(str(open(file,"rt").read()))
	Delete = open(file,"w")
	for x in range(FileLen):
		Delete.write("0")
	os.remove(file)
	return("Done")
	
def Folder(FolderPath):
		try:
			os.scandir(FolderPath)
		except:
			return(Error[1])
		else:
			for x in os.scandir(FolderPath):
				if x.is_file():
					File(x.path)
				elif x.is_dir():
					dir = str(FolderPath)+"/"+str(x.name)
					Folder(dir)
		os.rmdir(FolderPath)
		return("Done")
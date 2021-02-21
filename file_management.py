#get libraries
import os
import sys
def change_CWD():
	"""
	Will change the current directory into the directory where the files that will be sorted are.
	"""
	current_dir=os.getcwd()# get current directory
	choice=0
	while choice!=1:
		print("Current Working Direcotry:",current_dir)
		try:
			choice=int(input("Enter 1 if current directory is acceptable\nEnter 2 to change directory starting from userroot\nEnter 3 to clear screen\n"))
		except ValueError:
			print("Input is not a integer")
			continue
		if choice==2:#
			last_path=os.getcwd()# storing last good path we had in case of invalid path given
			dir_level=len(current_dir.split("/"))-2#We need to reach the user root level
			for i in range(dir_level):
				os.chdir("..")
			current_dir=os.getcwd()
			print("\nPath:",current_dir)
			path=input("\nEnter Path\n")
			path=os.path.join(current_dir,path)
			try:
				os.chdir(path)
			except :
				print("\nPath is invlaid\nERROR INFO:\n",sys.exc_info())
				os.chdir(last_path)
				current_dir=os.getcwd()
				continue
			current_dir=os.getcwd()
		elif choice==3:
			os.system("clear")
		elif choice==1:
			return
		else:
			print("No valid input given")
#TESTING
#change_CWD()

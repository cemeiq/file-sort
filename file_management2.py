import os
import time
import utility_functions as UF
import json

def change_CWD(FILE_PATH):
	"""
	Will change the current directory into the directory where the files that will be sorted are.
	Will return True for succesfull changing of CWD
	Will reutnr False for failed chaning of CWD
	"""
	current_dir=os.getcwd()# get current directory
	last_path=current_dir# to go 
	dir_level=len(current_dir.split("/"))-2 #We need to reach the user root level
	for i in range(dir_level):
		os.chdir("..")
	current_dir=os.getcwd()
	path=os.path.join(current_dir,FILE_PATH) #combine the Current directory with t he parameter passed in funciton
	#Now we check if its a valid path
	try:
		os.chdir(path)
	except : #IF path is not valid change path to last path and return false
		os.chdir(last_path)
		current_dir=os.getcwd()
		return False
	return True # if no error occurs then it will return True
Testing
#print(change_CWD("/home/hamza/Desktop/Hello2314"))

def setup_duplicate_folder():
    """
    This function will setup the duplicates folder
    :return: None
    """
    UF.run_command(["mkdir", "./Duplicates/Keep"], PIPE, PIPE)
    UF.run_command(["mkdir"m "./Duplicates/Waste"], PIPE, PIPE)
    instructions = \
    "In this folder are all duplicate files. Find the ones that you want to keep, just drag it into the folder called Keep. For all the ones that you want deleted, put them a folder called Waste. Once you have at least one file in the Keep folder, you can restart the program and use the move duplicates command and it will move all the files in the Keep folder to their correct folders. You can repeat this process as many times as you like. Also, when you are putting the files in the keep folder, you don't need to remove the _COPY extension, the program will do that automattically when they get moved into their folders."
    with open("./Duplicates/instructions.txt") as instructions_file:
        instructions_file.write(instructions)

import utility_functions as UF
import os
import sys
from subprocess import PIPE

def list_file_paths(extensions,sub_folders):
	"""
	Function to list the files in the current direcotires and sub direcotires.
	pararmeter sub_folders so that we can go to subfolder instead of the CWD
	"""
	# files list containing all the file paths
	files = [] 
	if sub_folders:
		for file_type in extensions:
			command = ['find', '.', '-iname', '*' + file_type + '']
			command_input = UF.run_command(command, PIPE, PIPE)
			command_out = UF.subprocess_output(command_input)
			if "\\n" in command_out:
				command_out = command_out.split("\\n")
				for file in command_out:
					if file !='':
						files.append(file.strip("\\n"))
			elif command_out !='':
				files.append(command_out)

	else:					
		for extension in extensions:
				for file in os.listdir("."):
					if file.endswith(extension):
						files.append(file)
	return files

import utility_functions
import os
import sys

def list_file_paths(extensions,sub_folders):
	"""
	Function to list the files in the current direcotires and sub direcotires.
	pararmeter sub_folders so that we can go to subfolder instead of the CWD
	"""
	files=[]#list storing the file paths
	if sub_folders:
		for file_type in extensions:
			command=['find','.','iname','*','extension']
			command_input=utility_functions.run_command(command,'PIPE','PIPE')
			command_out=utility_functions.subprocess_output(command_input)
			if "\\n" in command_out:
				command_out=command_out.split("\\n")
				for file in command_out:
					if file !='':
						file.append(file.strip("\\n"))
			else:
				if command_out !='':
					files.append(command_out)
	else:
		for file_type in extensions:
			command=['find','-','maxdepth','1','.','iname','*','extension', ]
			command_input=utility_functions.run_command(command,PIPE,PIPE)
			command_out=utility_functions.subprocess_output(command_input)
			if "\\n" in command_out:
				command_out=command_out.split("\\n")
				for file in command_out:
					if file !='':
						file.append(file.strip("\\n"))
			else:
				if command_out !='':
					files.append(command_out)
	return files
print(list_file_paths('.txt',True))

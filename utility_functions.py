
import subprocess
from subprocess import PIPE
import string

def subprocess_output(subprocess_command):
    """
    Getting the output of the subprocess commmand that was run
    :param subprocess_command: the sub_process command 
    :return: the command's output
    """
    string_command = str(subprocess_command)
    stdout_position = string_command.find("stdout")
    stderr_position = string_command.find("stderr")
    relative_string = string_command[stdout_position:stderr_position]
    final_string = relative_string[relative_string.find("'") + 1:-3]
    return final_string
    
def run_command(shell_command, stdout_option, stderr_option):
    """
    Will run a shell command using the subprocess module
    :param command: The command that the user wants to run
    :param shell_output: The output of the shell command is captured
    :return: the command output 
    """
    command_ran = subprocess.run(shell_command, stdout=stdout_option, stderr=stderr_option)
    return command_ran

def file_creation_date(file_path):
    """
    Finds the creation date for the file
    :param file_path: The file of the path the date will be extracted for
    :return: string that shows the file creation date
    """
    # command_ran = run_command(["stat", file_path], PIPE, PIPE)
    # subprocess_command_output = subprocess_output(command_ran)
    # command_output = subprocess_output(subprocess_command_output).strip("\\n")
    # elements = command_output.split(" ")
    # print(elements)
    print(file_path)
    date = subprocess_output(run_command(["stat", file_path], PIPE, PIPE)).strip('\\n').split(" ")[-5]

    year = date[:4]
    month = date[5:7]
    day = date[8:11]
    return [month, day, year]



# print(file_creation_date('/home/iqra/Documents/python-projects/file-sort/sorter.py'))
# print(subprocess_output(run_command(["stat", '/home/iqra/Documents/python-projects/file-sort/sorter.py'], PIPE, PIPE)).strip('\\n').split(" ")[-5])
# print(file_creation_date('/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/2020_Book_ArtificialIntelligenceXXXVII (4th copy).pdf')[0])
# print(subprocess_output(run_command(['find', '.', '-iname', '*' + '.pdf' + ''], PIPE, PIPE)))
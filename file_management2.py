import os
import time
import utility_functions as UF
import json


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

import os
import time
import utility_functions as UF
import json
import subprocess
from subprocess import PIPE


def setup_duplicate_folder():
    """
    This function will setup the duplicates folder
    :return: None
    """
    keep_path = './Duplicates/Keep'
    waste_path = './Duplicates/Waste'
    os.makedirs(keep_path)
    os.makedirs(waste_path)
    instructions = \
    "In this folder are all duplicate files. Find the ones that you want to keep, just drag it into the folder called Keep. For all the ones that you want deleted, put them a folder called Waste. Once you have at least one file in the Keep folder, you can restart the program and use the move duplicates command and it will move all the files in the Keep folder to their correct folders. You can repeat this process as many times as you like. Also, when you are putting the files in the keep folder, you don't need to remove the _COPY extension, the program will do that automattically when they get moved into their folders."
    with open("./Duplicates/instructions.txt", "w") as instructions_file:
        instructions_file.write(instructions)
    print("\nGo into the Duplicates folder and read the instructions.txt file to know what to do with the duplicates.", "yellow")    


def manage_duplicate_folder(keep_remove):
    """
    This function moves the files in the keep filder and removes the files in the waste folder.
    :param keep_remove: either Remove or Keep (answer with boolean)
    :return: none
    """
    if keep_remove:
        try:
            org_file_names = os.listdir('./Duplicates/Keep')
        except FileNotFoundError:
            raise Exception("It seems as though the program has not been ran here before here. This is due to the fact that there is no folder called Duplicates/Keep.")
        fixed_file_names = {}
        print(org_file_names)
        for file in org_file_names:
            if ("copy" in file) == False:
                fixed_file_names.setdefault(file,[]).append(0)     
                print(0)
            elif "copy" in file:
                print(file)
                file_name_str = str(file)
                copy_index = file_name_str.rindex('copy')
                dot_index = file_name_str.rindex('.')
                curly_bracket_index = file_name_str.rindex('(')
                file_extension = file_name_str[dot_index+1:]
                file_name = file_name_str[:curly_bracket_index]
                new_file_name = file_name + '.'+file_extension
                
                new_file_name = new_file_name.replace(" ", "")
                # print(new_file_name)
                

                # if new_file_name in org_file_names:    
                #     fixed_file_names.setdefault(new_file_name,[]).append(file_name_str)
       
                # # print(fixed_file_names)     
                # # print(file)          
                # else:
                fixed_file_names.setdefault(new_file_name,[]).append(file_name_str)
        print(fixed_file_names)
        updated_dict = {}
        
        for key, value in fixed_file_names.items():
            copies = 0
            for item in value:
                if (item !=0):
                    print(item)
                    copies+=1
                    file_name_str = str(item)
                    copy_index = file_name_str.rindex('copy')
                    dot_index = file_name_str.rindex('.')
                    curly_bracket_index = file_name_str.rindex('(')
                    file_extension = file_name_str[dot_index+1:]
                    file_name = file_name_str[:curly_bracket_index]
                    new_file_name = file_name + '.'+file_extension
                    
                    new_file_name = new_file_name.replace(" ", "")
                    

                    copy_file_item = str(file_name) + str(copies) + '.'+file_extension
                    copy_file_item = copy_file_item.replace(" ", "")

                    org_path = '/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/'+ file_name_str
                    print('orgpath: '+org_path)
                    new_path = '/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/'+ copy_file_item
                    print('newpath: '+new_path)
                    UF.run_command(["mv",org_path,new_path], PIPE, PIPE)
                    updated_dict.setdefault(key,[]).append(copy_file_item)
                    date_folder_path = '/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/'+file_path_dates(UF.file_creation_date(new_path))
                    UF.run_command(["mkdir","-p",date_folder_path], PIPE, PIPE)
                    UF.run_command(["mv",new_path,date_folder_path], PIPE, PIPE) 
                else:
                    print(key)
                    new_path = '/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/'+ str(key)
                    date_folder_path = '/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/'+file_path_dates(UF.file_creation_date(new_path))
                    UF.run_command(["mkdir","-p",date_folder_path], PIPE, PIPE)
                    UF.run_command(["mv",new_path,date_folder_path], PIPE, PIPE)               

        # print(updated_dict)         
        # for x, y in fixed_file_names.items():
            
            #             copies = 0
            # while True:
            #     copies += 1
            #     copy_file_name = str(y) + str(copies) + '.'+file_extension
            #     print(copy_file_name)
            #     if copy_file_name in fixed_file_names:
            #             continue
            #     else:
            #             fixed_file_names[x] = copy_file_name

        # print(fixed_file_names)                 
                
        # for org_file_name, copies in updated_dict.items():
        #     for copy_file_name in copies:
        #             org_path = '/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/'+ org_file_name
        #             print('orgpath: '+org_path)
        #             new_path = '/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/'+ copy_file_name
        #             print('newpath: '+new_path)
        #             UF.run_command(["mv",org_path,new_path], PIPE, PIPE)
        #             # date_folder_path = '/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/'+file_path_dates(UF.file_creation_date(new_path))
                    # UF.run_command(["mkdir","-p",date_folder_path], PIPE, PIPE)
                    # UF.run_command(["mv",new_path,date_folder_path], PIPE, PIPE)            
        
        # num_of_files = len(fixed_file_names.values())
        # print("Moved " + str(num_of_files) + " files to their proper folders")
        
    else:
        folder_name = 'Waste'
        waste_file_names = os.listdir('./Duplicates/'+folder_name)
        
        if len(waste_file_names) == 0:
            print('No files in Waste folder')

        else:
            for file_name in waste_file_names:
                path = './Duplicates/'+folder_name+'/'+file_name
                UF.run_command(["rm", path], PIPE, PIPE)
        print("Removed " + str(len(waste_file_names)) + " files in the Remove folder")
                
# def put_files_in_folders(raw_exif_data):
#     pass

def file_path_dates(input_date):
    if len(input_date) == 3:
        month = input_date[0]
        day = int(input_date[1])
        year = int(input_date[2])
        if day in (1, 21, 31):
            new_day = str(day) + "st"
        elif day in (2, 22):
            new_day = str(day) + "nd"
        elif day == 23:
            new_day = str(day) + "rd"
        else:
            new_day = str(day) + "th"
        final_string =  str(year) + "/" + str(month) + "/" + str(month) + "-" + str(new_day)
        return final_string 

# # setup_duplicate_folder()
manage_duplicate_folder(True)
# new_path = '/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/'+ '2020_Book_ArtificialIntelligenceXXXVII.pdf'
# date_folder_path = '/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/'+file_path_dates(UF.file_creation_date(new_path))
# UF.run_command(["mkdir","-p",date_folder_path], PIPE, PIPE)
# UF.run_command(["mv",new_path,date_folder_path], PIPE, PIPE) 
                
# org_path = '/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/2020_Book_ArtificialIntelligenceXXXVII (3rd copy).pdf'
# new_path = '/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/2020_Book_ArtificialIntelligenceXXXVII.pdf'
# UF.run_command(["mv",org_path,new_path], PIPE, PIPE)

# new_path = '/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/2020_Book_ArtificialIntelligenceXXXVII (copy).pdf'        
# date_folder_path = '/home/iqra/Documents/python-projects/file-sort/Duplicates/Keep/'+file_path_dates(UF.file_creation_date(new_path))
# # print(date_folder_path)
# print(date_folder_path)
# UF.run_command(["mkdir","-p",date_folder_path], PIPE, PIPE)
# UF.run_command(["mv",new_path,date_folder_path], PIPE, PIPE)            
        
import os
from shutil import move

src = "/home/iqra/Documents/python-projects/file-sort/test"
documents_dest = "/home/iqra/Documents"
music_dest = "/home/iqra/Music"
docs_ext = ["docx", "pdf"]
music_ext = ["mp3", "wav"]
filtered_list = []
dirList = os.listdir(src)

for i in dirList:
    for j in i:
        if j == '.':
            filtered_list.append(i)
print(filtered_list)
print('Entering Sorting Stage')
ext = None
for a in filtered_list:
    if a.endswith('pdf'):
        ext = 'pdf'
    elif a.endswith('mp3'):
        ext = 'mp3'         
    for b in docs_ext:
        if ext == b:
            temp =  os.path.join(src, a)
            move(temp, documents_dest) 
    for c in music_ext:
        if ext == c:
            temp1 =  os.path.join(src,a)
            move(temp1, music_dest) 



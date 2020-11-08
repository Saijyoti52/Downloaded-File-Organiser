import os
import shutil
import sys


while (1):

    files_present=os.listdir('C:/Users/Jyoti/Downloads')
    if files_present!=None:
        for i in files_present:
            
            if i.endswith('.exe'):
                shutil.move(os.path.join('C:/Users/Jyoti/Downloads',i),os.path.join('C:/Users/Jyoti/OneDrive/Desktop',i))
            elif i.endswith('.txt') or i.endswith('.docx'):
                shutil.move(os.path.join('C:/Users/Jyoti/Downloads',i),os.path.join('C:/UsersJyoti/OneDrive/Documents',i))
            elif i.endswith('.jpeg') or i.endswith('.png') or i.endswith('.jfif'):
                shutil.move(os.path.join('C:/Users/Jyoti/Downloads',i),os.path.join('C:/Users/Jyoti/OneDrive/Pictures/Saved Pictures',i))
            elif i.endswith('.mov') or i.endswith('.avi') or i.endswith('.wmv'):
                shutil.move(os.path.join('C:/Users/Jyoti/Downloads',i),os.path.join('C:/Users/Jyoti/Videos',i))
            elif i.endswith('.mp4') or i.endswith('.mpeg'):
                shutil.move(os.path.join('C:/Users/Jyoti/Downloads',i),os.path.join('C:/Users/Jyoti/Music',i))
import zipfile
import os
import sys
from zipfile import ZipFile
import traceback
import tkinter
from tkinter import filedialog

def search(dirname):
    filenames = os.listdir(dirname)
    
    try:
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                sys.stdout.write("탐색한 폴더 : " + full_filename + "\n")
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.zip': 
                    with zipfile.ZipFile(full_filename,'r') as zip_ref:
                        file_list = zip_ref.infolist()
                        for file in file_list:
                            #file.filename = file.filename.encode("cp437").decode('euc-kr','ignore')
                            
                            if(file.file_size == 0):
                                sys.stdout.write("0바이트 파일: " + full_filename + " "+ str(file.filename) + "\n")
                                #print("0바이트 파일: " + full_filename + " "+ str(file.file_size))
    except PermissionError:
        sys.stdout.write("PermissionError 발생한 파일 : " + full_filename + "\n")
        traceback_message = traceback.format_exc()
        sys.stdout.write("에러 내용: " + traceback_message + "\n")
        pass
    except UnicodeEncodeError:
        sys.stdout.write("UnicodeEncodeError 발생한 압축파일 : " + full_filename + "\n")
    #    traceback_message = traceback.format_exc()
    #    sys.stdout.write("에러 내용: " + traceback_message + "\n")
        pass
        

root = tkinter.Tk()
root.withdraw()
dir_path = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
#print("\ndir_path : ", dir_path)

sys.stdout.write("탐색시작 폴더 : " + dir_path + "\n")
search(dir_path)

#sys.stdout.write("탐색시작 폴더 : " + os.getcwd() + "\n")
#search(os.getcwd())

sys.stdout.write("탐색완료 종료하려면 엔터키 입력하세요\n")
data = sys.stdin.readline().rstrip()

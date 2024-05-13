import os 
import io
import sys
import traceback

def search(dirname): 
    files = os.listdir(dirname)

    try:
        for file in files:
            full_filename = os.path.join(dirname, file)
            if os.path.isdir(full_filename):
                sys.stdout.write("탐색한 폴더 : " + full_filename + "\n")
                search(full_filename)
            else:
                file_size = os.path.getsize(dirname + '/' + file)
                if file_size == 0:
                    sys.stdout.write('0바이트 파일 : ' + full_filename + '\n')
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
    except:
        sys.stdout.write("예기치 않은 에러가 발생하였습니다.\n")
        sys.stdout.write("에러 발생 파일 명: " + full_filename + "\n")
        sys.stdout.write("에러 내용: " + traceback_message + "\n")
        pass

#root = tkinter.Tk()
#root.withdraw()
#dir_path = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')

sys.stdout.write("탐색시작 폴더 : " + os.getcwd() + "\n")
search(os.getcwd())
sys.stdout.write("탐색완료 종료하려면 엔터키 입력하세요\n")
data = sys.stdin.readline().rstrip()

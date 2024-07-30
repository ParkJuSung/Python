import os
import configparser

def read_config():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.getcwd(), 'config.ini')
    config.read(config_path, encoding='utf-8')  # 설정 파일 경로
    sections = config.sections()
    target_folders = config.get('Settings', 'TargetFolders')
    return [folder.strip() for folder in target_folders.split(',')]

def check_specific_folders(root_dir, target_folders):
    for target_folder in target_folders:

        if target_folder.endswith('변화정보'):
            check_path(root_dir + '\\1. 변화정보')
        elif target_folder.endswith('수치도화'):  # '수치도화'로 시작하는 폴더만 검사
            target_folder_path = os.path.join(root_dir, target_folder)

            if os.path.exists(target_folder_path) and os.path.isdir(target_folder_path):
                # 모든 하위 폴더 검사
                for root, dirs, files in os.walk(target_folder_path):
                    for dir_name in dirs:
                        if dir_name.endswith('원점'):  # 원점으로 끝나는 폴더
                            sub_folder_path = os.path.join(root, dir_name)
                            check_sub_folders(sub_folder_path)
                if(os.path.exists(target_folder_path + '\\2. 모델색인도')):
                    check_path(target_folder_path + '\\2. 모델색인도')
                    #print(target_folder_path + '\\모델색인도 폴더가 존재')
                else:
                    print(target_folder_path + '\\2. 모델색인도 폴더가 존재하지 않습니다.')
                if(os.path.exists(target_folder_path + '\\3. 산높이DB성과')):
                    check_path(target_folder_path + '\\3. 산높이DB성과')
                    #print(target_folder_path + '\\산높이DB성과 폴더가 존재')
                else:
                    print(target_folder_path + '\\3. 산높이DB성과 폴더가 존재하지 않습니다.')
            else:
                print(f"대상 폴더 '{target_folder}'가 '{root_dir}' 안에 존재하지 않습니다.")
        elif target_folder.endswith('지리조사'):
                    check_path(root_dir + '\\3. 지리조사')
        elif target_folder.endswith('편집성과'):
            target_folder_path = os.path.join(root_dir, target_folder)
            if os.path.exists(target_folder_path + '\\1. 수치지형도1.0'):
                for root, dirs, files in os.walk(target_folder_path + '\\1. 수치지형도1.0'):
                    for dir_name in dirs:
                        sub_folder_path = os.path.join(target_folder_path+'\\1. 수치지형도1.0', dir_name)
                        check_sub_folders(sub_folder_path)
            else:
                print(f"대상 폴더 '{target_folder_path}'\\1. 수치지형도1.0'가 '{target_folder_path}' 안에 존재하지 않습니다.")
            if os.path.exists(target_folder_path + '\\2. 수치지형도2.0'):
                for root, dirs, files in os.walk(target_folder_path + '\\2. 수치지형도2.0'):
                    for dir_name in dirs:
                        sub_folder_path = os.path.join(target_folder_path+'\\2. 수치지형도2.0', dir_name)
                        check_sub_folders(sub_folder_path)
            else:
                print(f"대상 폴더 '{target_folder_path}'\\2. 수치지형도2.0가 '{target_folder_path}' 안에 존재하지 않습니다.")
            if os.path.exists(target_folder_path + '\\3. 구조화중간편집성과(50k)'):
                for root, dirs, files in os.walk(target_folder_path + '\\3. 구조화중간편집성과(50k)'):
                    for dir_name in dirs:
                        sub_folder_path = os.path.join(target_folder_path+'\\3. 구조화중간편집성과(50k)', dir_name)
                        check_sub_folders(sub_folder_path)
            else:
                print(f"대상 폴더 '{target_folder_path}'\\3. 구조화중간편집성과(50k)'가 '{target_folder_path}' 안에 존재하지 않습니다.")
            if os.path.exists(target_folder_path + '\\4. 보안바운더리'):
                check_path(target_folder_path + '\\4. 보안바운더리')
            else:
                print(f"대상 폴더 '{target_folder_path}'\\4. 보안바운더리'가 '{target_folder_path}' 안에 존재하지 않습니다.")
        elif target_folder.endswith('메타데이터 및 관리파일'):
            #메타데이터, 기관표준 폴더가 필수라면 수정 필요
            target_folder_path = os.path.join(root_dir, target_folder)
            if os.path.exists(target_folder_path + '\\1. 메타데이터'):
                check_path(target_folder_path + '\\1. 메타데이터')
            else:
                print(f"대상 폴더 '{target_folder_path}'\\1. 메타데이터'가 '{target_folder_path}' 안에 존재하지 않습니다.")
            
            if os.path.exists(target_folder_path + '\\2. 기관표준'):
                check_path(target_folder_path + '\\2. 기관표준')
            else:
                print(f"대상 폴더 '{target_folder_path}'\\2. 기관표준'가 '{target_folder_path}' 안에 존재하지 않습니다.")

            #print(f"대상 폴더 '{target_folder}'가 '{root_dir}' 안에 존재합니다.")
        elif target_folder.endswith('품질검사보고서'):
            target_folder_path = os.path.join(root_dir, target_folder)
            if os.path.exists(target_folder_path + '\\1. 기본측량성과검증결과표'):
                check_path(target_folder_path + '\\1. 기본측량성과검증결과표')
            else:
                print(f"대상 폴더 '{target_folder_path}'\\1. 기본측량성과검증결과표'가 '{target_folder_path}' 안에 존재하지 않습니다.")
            if os.path.exists(target_folder_path + '\\2. 자체검사err파일'):
                for root, dirs, files in os.walk(target_folder_path + '\\2. 자체검사err파일'):
                        for dir_name in dirs:
                            sub_folder_path = os.path.join(target_folder_path + '\\2. 자체검사err파일',dir_name)
                            check_sub_folders(sub_folder_path)
            else:
                print(f"대상 폴더 '{target_folder_path}'\\2. 자체검사err파일'가 '{target_folder_path}' 안에 존재하지 않습니다.")
        elif target_folder.endswith('용역결과보고서'):
            target_folder_path = os.path.join(root_dir, target_folder)
            check_path(target_folder_path)
            #print(f"대상 폴더 '{target_folder}'가 '{root_dir}' 안에 존재합니다.")
        elif target_folder.endswith('기타성과'):
            target_folder_path = os.path.join(root_dir, target_folder)
            check_path(target_folder_path)
            #print(f"대상 폴더 '{target_folder}'가 '{root_dir}' 안에 존재합니다.")
        else:
            target_folder_path = os.path.join(root_dir, target_folder)
            if not os.path.exists(target_folder_path) and not os.path.isdir(target_folder_path):
                print(f"대상 폴더 '{target_folder}'가 '{root_dir}' 안에 존재하지 않습니다.")

def check_sub_folders(parent_folder):
    # 원점으로 끝나는 폴더의 모든 하위 폴더 검사
    for root, dirs, files in os.walk(parent_folder):
        for dir_name in dirs:
            if dir_name.endswith('수정도화모델') or dir_name.endswith('수정도화') or dir_name.endswith('완성도엽'):
                sub_folder_path = os.path.join(root, dir_name)
                for folder_name, extension in [('dwg', '.dwg'), ('dxf', '.dxf')]:
                    folder_path = os.path.join(sub_folder_path, folder_name)
                    if os.path.exists(folder_path) and os.path.isdir(folder_path):
                        # 해당 폴더 내의 파일 목록 가져오기
                        files_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(extension)]
                        if folder_name == 'dwg' and len(files_list) == 0:
                            print(f"│  └─'{folder_path}' 폴더가 존재하지만, 확장자가 {extension}인 파일이 없습니다.")
                        elif folder_name == 'dxf' and len(files_list) == 0:
                            print(f"│  └─'{folder_path}' 폴더가 존재하지만, 확장자가 {extension}인 파일이 없습니다.")
                    else:
                        print(f"│  └─'{folder_path}' 중 {folder_name} 폴더가 존재하지 않습니다.")

            if '수치지형도1.0\\' in parent_folder and parent_folder.endswith('원점'):
                if(root == parent_folder):
                    sub_folder_path = os.path.join(root, dir_name)
                    for folder_name, extension in [('dwg', '.dwg'), ('dxf', '.dxf')]:
                        folder_path = os.path.join(sub_folder_path, folder_name)
                        if os.path.exists(folder_path) and os.path.isdir(folder_path):
                            # 해당 폴더 내의 파일 목록 가져오기
                            files_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(extension)]
                            if folder_name == 'dwg' and len(files_list) == 0:
                                print(f"│  └─'{folder_path}' 폴더가 존재하지만, 확장자가 {extension}인 파일이 없습니다.")
                            elif folder_name == 'dxf' and len(files_list) == 0:
                                print(f"│  └─'{folder_path}' 폴더가 존재하지만, 확장자가 {extension}인 파일이 없습니다.")
                        else:
                            print(f"│  └─'{folder_path}' 중 {folder_name} 폴더가 존재하지 않습니다.")

            if '수치지형도2.0\\' in parent_folder and parent_folder.endswith('원점'):
                if(root == parent_folder):
                    sub_folder_path = os.path.join(root, dir_name)
                    for folder_name, extension in [('gpkg', 'gpkg'), ('shp', 'shp')]:
                        folder_path = os.path.join(sub_folder_path, folder_name)
                        if os.path.exists(folder_path) and os.path.isdir(folder_path):
                            # 해당 폴더 내의 파일 목록 가져오기
                            files_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(extension)]
                            if folder_name == 'gpkg' and len(files_list) == 0:
                                print(f"│  └─'{folder_path}' 폴더가 존재하지만, 확장자가 {extension}인 파일이 없습니다.")
                            elif folder_name == 'shp' and len(files_list) == 0:
                                print(f"│  └─'{folder_path}' 폴더가 존재하지만, 확장자가 {extension}인 파일이 없습니다.")
                        else:
                            print(f"│  └─'{folder_path}' 중 {folder_name} 폴더가 존재하지 않습니다.")

            if '구조화중간편집성과(50k)\\' in parent_folder and parent_folder.endswith('원점'):
                if(root == parent_folder):
                    sub_folder_path = os.path.join(root, dir_name)
                    for folder_name, extension in [('gpkg', 'gpkg'), ('shp', 'shp')]:
                        folder_path = os.path.join(sub_folder_path, folder_name)
                        if os.path.exists(folder_path) and os.path.isdir(folder_path):
                            # 해당 폴더 내의 파일 목록 가져오기
                            files_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(extension)]
                            if folder_name == 'gpkg' and len(files_list) == 0:
                                print(f"│  └─'{folder_path}' 폴더가 존재하지만, 확장자가 {extension}인 파일이 없습니다.")
                            elif folder_name == 'shp' and len(files_list) == 0:
                                print(f"│  └─'{folder_path}' 폴더가 존재하지만, 확장자가 {extension}인 파일이 없습니다.")
                        else:
                            print(f"│  └─'{folder_path}' 중 {folder_name} 폴더가 존재하지 않습니다.")
            
            #if '1. 구조화중간파일' in parent_folder or '2. 수치지형도1.0' in parent_folder or '3. 수치지형도 2.0' in parent_folder:
            if parent_folder.endswith('구조화중간파일') or parent_folder.endswith('수치지형도1.0') or parent_folder.endswith('수치지형도2.0'):
                if(root == parent_folder):
                    sub_folder_path = os.path.join(root, dir_name)
                    for folder_name, extension in [('err', 'err')]:
                        folder_path = os.path.join(sub_folder_path, folder_name)
                        if os.path.exists(folder_path) and os.path.isdir(folder_path):
                            # 해당 폴더 내의 파일 목록 가져오기
                            files_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(extension)]
                            if folder_name == 'err' and len(files_list) == 0:
                                print(f"│  └─'{folder_path}' 폴더가 존재하지만, 확장자가 {extension}인 파일이 없습니다.")
                        else:
                            print(f"│  └─'{folder_path}' 중 {folder_name} 폴더가 존재하지 않습니다.")

def check_path(path):
    contents = os.listdir(path)
    subfolders = [f for f in contents if os.path.isdir(os.path.join(path, f))]
    files = [f for f in contents if os.path.isfile(os.path.join(path, f))]
    
    # 만약 하위 폴더와 파일이 모두 없는 경우 출력
    if not subfolders and not files:
        print(f"│  └─'{path}'에는 하위 폴더와 파일이 모두 없습니다.")

    # 하위 폴더가 있는 경우 재귀적으로 각 하위 폴더에 대해 검사
    for folder in subfolders:
        subfolder_path = os.path.join(path, folder)
        check_path(subfolder_path)



def check_if_item_exists(target_folder_path, search_name):
    """
    특정 폴더 경로 내의 모든 폴더와 파일에서 지정한 이름이 포함된 항목이 존재하는지 확인합니다.
    
    :param target_folder_path: 검색할 기본 폴더 경로
    :param search_name: 검색할 이름(부분 문자열)
    :return: 이름이 포함된 폴더나 파일이 있으면 True, 그렇지 않으면 False
    """
    for root, dirs, files in os.walk(target_folder_path):
        # 디렉토리 검색
        if any(search_name in dir for dir in dirs):
            return True
    return False

# 실행 파일이 있는 경로를 기준으로 설정
root_directory = os.getcwd()  # 현재 작업 디렉토리를 root_directory로 설정

# 설정 파일에서 타겟 폴더들을 읽어옴
target_folders = read_config()  

# 함수 호출
check_specific_folders(root_directory, target_folders)

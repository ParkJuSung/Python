import os
import json
import re
import fnmatch

def read_config():
    config_path = os.path.join(os.getcwd(), 'folders.json')
    with open(config_path, 'r', encoding='utf-8') as file:
        config = json.load(file)
    
    directories = config['Directories']
    extensions = config['Extensions']
    required_subfolders = config.get('RequiredSubfolders', {})
    
    return directories, extensions, required_subfolders

def normalize_folder_name(folder_name):
    """
    폴더 이름을 정규화하여 설정 파일의 키와 매칭합니다.
    - 공백, 점, 밑줄 제거
    - 모든 문자를 소문자로 변환
    """
    if isinstance(folder_name, list):
        return [normalize_folder_name(name) for name in folder_name]

    folder_name = folder_name.lower()
    folder_name = re.sub(r'^\d+\.?\s*', '', folder_name)  # 앞에 붙은 숫자와 점 제거
    folder_name = folder_name.replace(' ', '')  # 공백 제거
    folder_name = folder_name.replace('.', '')  # 점 제거
    folder_name = folder_name.replace('_', '')  # 밑줄 제거
    
    return folder_name

def matches_wildcard(pattern, name):
    """
    이름이 패턴(와일드카드)과 일치하는지 확인합니다.
    """
    pattern = normalize_folder_name(pattern)
    name = normalize_folder_name(name)
    return fnmatch.fnmatch(name, pattern)

def find_matching_pattern(required_subfolders, folder_key):
    """
    와일드카드 패턴을 사용하여 folder_key와 일치하는 항목을 찾습니다.
    """
    # 중첩된 구조를 재귀적으로 처리합니다.
    for pattern, subfolders in required_subfolders.items():
        if matches_wildcard(pattern, folder_key):
            if isinstance(subfolders, dict) and subfolders:
                return subfolders
            return subfolders
    return {}

def check_required_files(path, required_extensions):
    """
    지정된 폴더에서 파일 확장자 검사를 수행합니다.
    """
    if isinstance(required_extensions, dict):
        return  # If required_extensions is a dict, skip file checking
    
    if required_extensions:
        if isinstance(required_extensions, str):
            required_exts = [ext.strip() for ext in required_extensions.split(',')]
        else:
            required_exts = [ext.strip() for ext in required_extensions]

        contents = os.listdir(path)
        files = [f for f in contents if os.path.isfile(os.path.join(path, f))]
        file_extensions = {os.path.splitext(f)[1][1:].lower() for f in files}

        for ext in required_exts:
            if ext == '*':
                continue  # '*'는 모든 파일을 의미하므로 무시
            if ext not in file_extensions:
                print(f"│  └─'{path}' 폴더에 확장자가 {ext}인 파일이 없습니다.")

def check_path(path, extensions, folder_key, required_subfolders):
    contents = os.listdir(path)
    subfolders = [f for f in contents if os.path.isdir(os.path.join(path, f))]
    files = [f for f in contents if os.path.isfile(os.path.join(path, f))]

    required_extensions = find_matching_pattern(required_subfolders, folder_key)

    if isinstance(required_extensions, dict):
        for subfolder_pattern, ext_list in required_extensions.items():
            matched = False
            for subfolder in subfolders:
                if matches_wildcard(subfolder_pattern, subfolder):
                    matched = True
                    subfolder_path = os.path.join(path, subfolder)
                    check_required_files(subfolder_path, ext_list)
                    break
            if not matched:
                print(f"│  └─'{path}' 폴더에 '{subfolder_pattern}' 서브폴더가 없습니다.")
    else:
        check_required_files(path, required_extensions)

    # Check if both files and subfolders are missing and if it has extensions
    if not subfolders and not files and not isinstance(required_extensions, list) and extensions.get(folder_key) is None:
        print(f"│  └─'{path}'에는 하위 폴더와 파일이 모두 없습니다.")
    
    # Check required subfolders recursively
    for folder in subfolders:
        subfolder_path = os.path.join(path, folder)
        subfolder_key = normalize_folder_name(folder)
        subfolder_requirements = find_matching_pattern(required_subfolders, subfolder_key)
        check_path(subfolder_path, extensions, subfolder_key, required_subfolders)

def check_specific_folders(root_dir, directories, extensions, required_subfolders):
    directory_keys = {normalize_folder_name(v): k for k, v in directories.items()}

    # 제외할 파일 확장자 목록
    excluded_extensions = {'.ini', '.json', '.py', '.exe'}

    for item_name in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item_name)
        
        if os.path.isdir(item_path):
            normalized_name = normalize_folder_name(item_name)
            if normalized_name in directory_keys:
                folder_key = directory_keys[normalized_name]
                check_path(item_path, extensions, folder_key, required_subfolders)
            else:
                print(f"미정의 폴더 '{item_name}'가 '{root_dir}' 안에 존재합니다.")
        
        elif os.path.isfile(item_path):
            # 파일의 확장자를 가져와서 제외할 목록에 있는지 확인
            _, ext = os.path.splitext(item_name)
            ext = ext.lower()
            if ext not in excluded_extensions:
                print(f"대상 파일 '{item_name}'이 '{root_dir}' 안에 존재합니다.")
        
        else:
            print(f"'{item_name}'은(는) 폴더도 파일도 아닌 항목입니다.")

# 실행 파일이 있는 경로를 기준으로 설정
root_directory = os.getcwd()  # 현재 작업 디렉토리를 root_directory로 설정

# 설정 파일에서 디렉토리, 확장자, 필수 서브폴더 정보를 읽어옴
directories, extensions, required_subfolders = read_config()

# 함수 호출
check_specific_folders(root_directory, directories, extensions, required_subfolders)

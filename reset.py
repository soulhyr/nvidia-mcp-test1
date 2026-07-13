# reset.py
import os
import shutil

def reset_all_data():
    # 관리하고 있는 모든 데이터 경로
    data_paths = ["data/employees", "data/todos", "data/todo_list.json"]
    
    print("--- 데이터 초기화를 시작합니다 ---")
    
    for path in data_paths:
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)  # 폴더 삭제
                print(f"삭제 완료: {path}/")
            else:
                os.remove(path)      # 파일 삭제
                print(f"삭제 완료: {path}")
        else:
            print(f"이미 없음: {path}")

    # 필수 디렉토리 다시 생성
    os.makedirs("data/employees", exist_ok=True)
    os.makedirs("data/todos", exist_ok=True)
    
    print("--- 모든 데이터가 초기화되었습니다 ---")

if __name__ == "__main__":
    reset_all_data()
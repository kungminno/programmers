import os

# 파일을 생성할 디렉터리 (현재 폴더로 지정)
output_dir = './algorithm/'

for i in range(78,80):
    filename = f"algorithm_{i}.py"
    filepath = os.path.join(output_dir, filename)
    # 파일이 이미 없으면 새로 생성
    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            # 원하는 기본 템플릿이 있다면 여기에 넣을 수 있습니다.
            f.write("def solution()")

        print(f"Created {filename}")



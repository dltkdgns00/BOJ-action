import os
import sys
from libs.extract_markdown import extract_markdown
from libs.scrapper import fetch_code_performance
from libs.update_markdown import update_markdown_with_performance


def main(not_filled_files_path, user_id, language_id):
    print("Current working directory:", os.getcwd())

    workspace = os.environ["GITHUB_WORKSPACE"]  # 워크플로우 워크스페이스 경로 가져오기

    # 'not_filled_files.txt' 파일을 열어 각 줄을 읽는다.
    with open(not_filled_files_path, "r") as f:
        files = f.readlines()

    # 각 줄마다 (각 파일 경로마다) 작업을 수행
    for file_path in files:
        file_path = file_path.strip()  # 줄바꿈 문자 제거
        if not file_path:  # 만약 빈 줄이면, 넘어간다.
            continue
        # 파일 경로를 절대 경로로 변환한다.
        absolute_path = os.path.join(workspace, file_path)
        if not os.path.exists(absolute_path):
            print(f"File {absolute_path} does not exist!")  # 경로가 잘못되었을 경우 경로 출력
            continue

        problem_id = extract_markdown(absolute_path)
        if problem_id:
            # scrapper.py에서 스크래핑 기능을 호출하여 코드의 성능 정보를 가져온다.
            time, memory = fetch_code_performance(problem_id, user_id, language_id)
            if time != "None" or memory != "None":
                # update_markdown.py에서 마크다운 업데이트 기능을 호출하여 성능 정보를 업데이트한다.
                update_markdown_with_performance(absolute_path, time, memory)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])

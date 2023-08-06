import re


def extract_markdown(file_path):
    file_path = file_path.strip('"')
    file_path = file_path.encode("utf-8").decode("utf-8")
    with open(file_path, "r") as f:
        content = f.read()
        # 문제 번호를 찾기 위한 정규식
        match = re.search(r"# (\d+)번:", content)
        if match:
            return match.group(1)
        return None

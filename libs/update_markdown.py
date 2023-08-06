import re


def update_markdown_with_performance(file_path, time, memory):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 가정: 성능을 업데이트할 부분이 <!-- performance --> <!-- end --> 사이에 있다.
    performance_str = f"<!-- performance -->\n### 성능 요약\n메모리: {memory} KB, 시간: {time} ms\n<!-- end -->"
    updated_content = re.sub(
        r"<!-- performance -->.*?<!-- end -->",
        performance_str,
        content,
        flags=re.DOTALL,
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

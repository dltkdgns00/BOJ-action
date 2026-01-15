import requests
from bs4 import BeautifulSoup


def fetch_code_performance(problem_id, user_id, language_id):
    try:
        url = f"https://www.acmicpc.net/status?problem_id={problem_id}&user_id={user_id}&result_id=4"
        if language_id:
             url += f"&language_id={language_id}"
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # 웹 페이지에서 필요한 정보를 추출하는 코드를 여기에 추가합니다.
        time = soup.find("td", {"class": "time"}).text
        memory = soup.find("td", {"class": "memory"}).text

        print(time, memory)
    except Exception as e:
        return "None", "None"

    return time, memory

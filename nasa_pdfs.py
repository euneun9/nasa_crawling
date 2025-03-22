import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pdfkit
import os

config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')  # 경로 설정 안 해도 되면 None

# 1. frameset 페이지 요청
base_url = "https://workmanship.nasa.gov/lib/insp/2%20books/frameset.html"
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# 2. <frame> src 추출
frame_srcs = [frame.get('src') for frame in soup.find_all('frame') if frame.get('src')]

# 3. 모든 프레임에서 href 수집
all_links = []
for frame_src in frame_srcs:
    frame_url = urljoin(base_url, frame_src)
    try:
        frame_response = requests.get(frame_url)
        frame_soup = BeautifulSoup(frame_response.text, 'html.parser')
        for a_tag in frame_soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(frame_url, href)
            all_links.append(full_url)
    except Exception as e:
        print(f"❌ Failed to process {frame_url}: {e}")

# 중복 제거
all_links = list(set(all_links))

# 4. 저장 폴더 생성
os.makedirs("nasa_pdfs", exist_ok=True)

# 5. 각 링크를 PDF로 저장
for link in all_links:
    try:
        filename = link.rstrip('/').split('/')[-1]
        if not filename.endswith('.pdf'):
            filename += '.pdf'
        save_path = os.path.join("nasa_pdfs", filename)
        print(f"📄 Saving {link} → {save_path}")
        pdfkit.from_url(link, save_path, configuration=config)
    except Exception as e:
        print(f"❌ Error saving {link}: {e}")

print("✅ All done.")

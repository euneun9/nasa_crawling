# NASA Workmanship Standards PDF Crawler

[NASA Workmanship Standards 사이트](https://workmanship.nasa.gov/lib/insp/2%20books/frameset.html) 에 포함된 모든 페이지를 크롤링하여 PDF 형식으로 저장하기

---

## 📌 주요 기능

- 프레임셋 구조 분석 및 프레임 내 페이지 접근
- 모든 링크 수집 및 접근
- HTML 페이지를 PDF 파일로 저장

---

## 🛠 설치 방법

### 1. wkhtmltopdf 설치
[wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)에서 운영체제에 맞는 버전 다운로드 및 설치
설치 경로 확인 후 코드에 반영 필요
### 2. 코드 실행
```
python nasa_crawler.py

```
### 3. 자동으로 폴더에 저장됨
![image](https://github.com/user-attachments/assets/cd911f94-807a-4d27-a707-7319445c35a4)
![image](https://github.com/user-attachments/assets/92debdcd-d8ac-4ade-909b-68218026ee82)

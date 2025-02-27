import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ✅ 보내는 이메일 정보 설정
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "hyw22choi@gmail.com"  # ✨ 너의 Gmail 주소로 변경
SENDER_PASSWORD = "ijfu mlcn uegd fkns"  # ✨ Gmail 앱 비밀번호 사용

# ✅ 받는 사람 이메일
RECEIVER_EMAIL = "hyw22choi@gmail.com"  # ✨ 받을 이메일 주소로 변경

# ✅ 전송할 파일
TEXT_FILE = "word_list.txt"

# 파일 읽기
if not os.path.exists(TEXT_FILE):
    print("⚠️ 단어 목록 파일이 없습니다. 먼저 실행해주세요!")
    exit()

with open(TEXT_FILE, "r", encoding="utf-8") as f:
    email_content = f.read()

# 이메일 메시지 구성
msg = MIMEMultipart()
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg["Subject"] = "📖 오늘의 일본어 단어 15개"

# 이메일 본문 추가
msg.attach(MIMEText(email_content, "plain", "utf-8"))

# SMTP 서버에 연결하여 메일 전송
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # 보안 연결
    server.login(SENDER_EMAIL, SENDER_PASSWORD)  # 로그인
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())  # 메일 전송
    server.quit()

    print("✅ 메일 전송 완료!")

except Exception as e:
    print(f"❌ 메일 전송 실패: {e}")

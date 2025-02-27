import pandas as pd
import os

# ✅ 엑셀 파일 경로
EXCEL_FILE = "Jananese_words800.xlsx"
PROGRESS_FILE = "progress.txt"
OUTPUT_FILE = "word_list.txt"

# ✅ 엑셀 파일 불러오기 (헤더 명확히 지정)
df = pd.read_excel(EXCEL_FILE, header=0)  # 첫 번째 행을 헤더로 사용

# ✅ 엑셀 데이터 확인 (컬럼명 출력)
print("🔹 데이터 컬럼명:", df.columns.tolist())

# ✅ 진행 상태 확인
if os.path.exists(PROGRESS_FILE):
    with open(PROGRESS_FILE, "r") as f:
        start_idx = int(f.read().strip())
else:
    start_idx = 0

# ✅ 총 단어 개수
total_words = len(df)

# ✅ 한 번에 보낼 단어 개수
batch_size = 15

# ✅ 마지막 배치인지 확인
if start_idx >= total_words:
    print("✅ 모든 단어가 이미 전송되었습니다.")
    exit()

# ✅ 15개씩 데이터 가져오기
subset = df.iloc[start_idx:start_idx + batch_size]

# ✅ 단어 저장 (컬럼명으로 접근)
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for _, row in subset.iterrows():
        japanese = row["일본어"] if "일본어" in df.columns else row.iloc[1]  # 일본어 단어
        korean = row["한국어"] if "한국어" in df.columns else row.iloc[2]  # 한국어 뜻
        
        # 일본어, 발음, 한국어 뜻 저장
        f.write(f"{japanese}\n")
        if "발음" in df.columns and pd.notna(row["발음"]):
            f.write(f"{row['발음']}\n")  # 발음 정보 추가
        f.write(f"{korean}\n\n")  # 한국어 뜻 추가

# ✅ 진행 상태 업데이트
new_index = start_idx + batch_size
with open(PROGRESS_FILE, "w") as f:
    f.write(str(new_index))

print(f"✅ {batch_size}개의 단어를 '{OUTPUT_FILE}' 파일로 저장 완료!")

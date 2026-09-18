# 운영체제 환경변수를 읽기 위한 모듈
import os

# .env 파일 내용을 환경변수로 등록
from dotenv import load_dotenv

# .env 파일 읽기
load_dotenv()

# 프로젝트 연결정보 확인
url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]

print("환경변수 로드 완료")

import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]

supabase: Client = create_client(url, key)
print("Supabase Client 생성 완료")

stock_code = "005930"

response = (
    supabase
    .schema("edu_finance")
    .table("stock_prices")
    .select("stock_code,trade_date,close_price,volume")
    .eq("stock_code", stock_code)
    .order("trade_date")
    .execute()
)

""" for row in response.data:
    print(row)

 """
#email = input("이메일: ").strip()
#password = input("비밀번호: ").strip()

""" try:
    login = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password,
    })

    user_id = login.user.id

    print("로그인 성공")
    print("현재 user_id:", user_id)

except Exception as e:
    print("로그인 실패:", e)
    raise SystemExit

difficulty = input("난이도(easy/normal/hard): ").strip()
answer_number = int(input("정답 숫자: "))
attempt_count = int(input("시도 횟수: "))
elapsed_seconds = float(input("소요 시간(초): "))
 """
""" data = {
    "user_id": user_id,
    "difficulty": difficulty,
    "answer_number": answer_number,
    "attempt_count": attempt_count,
    "elapsed_seconds": elapsed_seconds,
} """
""" 
response = (
    supabase
    .table("updown_games") ## updown_games 라는 테이블 안에 
    .insert(data) ## data 를 삽입하고
    .execute() ##  이 코드를 실행하겠다
) """

## 저장 결과 조회
print("저장 결과:", response.data)

response = (
    supabase
    .table("updown_games")
    .select("*")
    .order("played_at", desc=True)
    .execute()
)

#print(response.data)

response = (
    supabase
    .schema("edu_finance")
    .table("stocks")
    .select("stock_code,stock_name,market,sector")
    .limit(5)
    .execute()
)

#print(response.data)

#[
#  {'stock_code': '005930', 'stock_name': '삼성전자', ...},
#  ...
#]

import pandas as pd

""" price_df = pd.DataFrame(response.data)

print(price_df)

# info() 자체가 내용을 출력하므로 print()로 감싸지 않는다.
price_df.info()

price_df["trade_date"] = pd.to_datetime(price_df["trade_date"])
price_df["close_price"] = pd.to_numeric(price_df["close_price"])
price_df["volume"] = pd.to_numeric(price_df["volume"])

print(price_df.dtypes)


stock_code = input("관심 종목코드: ").strip()
memo = input("메모: ").strip()

print("입력 종목:", stock_code)
print("입력 메모:", memo)
 """
## 조건이나 예외처리로 입력 가능한 사람인지 걸러준다. 
""" if stock_code == "":
    print("종목코드를 입력해주세요.")
else:
    print("입력 가능")


data = {
    "stock_code": stock_code,
    "memo": memo,
}
## 데이터 적재, 단, 권한이 있다면
result = (
    supabase
    .schema("edu_finance")
    .table("user_watchlist")
    .insert(data)
    .execute()
)

print("저장 결과")
print(result.data)
 """
## 예상 결과
""" [{'watch_id': 1,
  'user_id': '로그인 사용자의 UUID',
  'stock_code': '005930',
  'memo': '관심 종목',
  'created_at': '...'}] """

""" watch_id = int(input("수정할 watch_id: "))
new_memo = input("새 메모: ").strip()

result = (
    supabase
    .schema("edu_finance")
    .table("user_watchlist")
    .update({"memo": new_memo})
    .eq("watch_id", watch_id) ## 조건을 걸어주는것, 닉네임 변경과 같은 게 필요할떄 조건을 걸어주고 ,통과여부에따라서 
    .execute()
)

print(result.data)


## 삭제 대상 확인
watch_id = int(input("삭제할 watch_id: "))

check_result = (
    supabase
    .schema("edu_finance")
    .table("user_watchlist")
    .select("watch_id,stock_code,memo")
    .eq("watch_id", watch_id)
    .execute()
)

print("삭제 대상:", check_result.data) """

all_prices = (
    supabase
    .schema("edu_finance")
    .table("stock_prices")
    .select("stock_code,trade_date,close_price,volume")
    .order("stock_code")
    .order("trade_date")
    .execute()
)

all_df = pd.DataFrame(all_prices.data)

all_df["trade_date"] = pd.to_datetime(all_df["trade_date"])
all_df["close_price"] = pd.to_numeric(all_df["close_price"])
all_df["volume"] = pd.to_numeric(all_df["volume"])

print(all_df.head())

# 종목별 평균 종가 
avg_close = (
    all_df
    .groupby("stock_code")["close_price"] # SQL이 아니고, 파이썬 내부의 Pandas라는 라이브러리를 사용해서 
    .mean() # 사용하는 함수임을 알아야함 
)

print(avg_close)


# 종목별 총거래량
total_volume = (
    all_df
    .groupby("stock_code")["volume"]
    .sum()
)

print(total_volume)

# 일별 수익률
# 종목별 날짜순 정렬
all_df = all_df.sort_values(["stock_code", "trade_date"])

# 같은 종목 안에서 직전 종가 대비 수익률 계산
all_df["return_rate"] = (
    all_df
    .groupby("stock_code")["close_price"]
    .pct_change()
)

print(all_df.head(15))
import pandas as pd
"""data = {
    "menu_name": [
        "아메리카노",
        "카페라떼",
        "아메리카노",
        "자몽허니블랙티",
        "카페라떼",
        "아메리카노"
    ],
    "quantity": [2, 1, 3, 1, 2, 1],
    "menu_price": [
        4700,
        5200,
        4700,
        5700,
        5200,
        4700
    ],
    "age": [23, 35, 27, 42, 31, 25],
    "gender": ["남", "여", "남", "여", "여", "남"],
    "order_time": [
        "2026-09-18 08:30",
        "2026-09-18 09:20",
        "2026-09-18 12:10",
        "2026-09-18 14:30",
        "2026-09-18 18:20",
        "2026-09-18 20:10"
    ]
} """
df = pd.DataFrame(data)
df["order_time"] = pd.to_datetime(df["order_time"])
df["hour"] = df["order_time"].dt.hour
df["sales"] = df["quantity"] * df["menu_price"]
def get_time_zone(hour):
    if hour < 11:
        return "아침"
    elif hour < 17:
        return "점심/오후"
    else:
        return "저녁"
df["time_zone"] = df["hour"].apply(get_time_zone)
def get_age_group(age):
    if age < 20:
        return "10대"
    elif age < 30:
        return "20대"
    elif age < 40:
        return "30대"
    else:
        return "40대 이상"
df["age_group"] = df["age"].apply(get_age_group)
print("===== 매출 통계 =====")
print("총 매출:", df["sales"].sum(), "원")
print("평균 매출:", df["sales"].mean(), "원")
print("최대 매출:", df["sales"].max(), "원")
print("최소 매출:", df["sales"].min(), "원")
menu_quantity = df.groupby("menu_name")["quantity"].sum()

print()
print("===== 메뉴별 판매량 =====")
print(menu_quantity)
print()
print("인기 메뉴:", menu_quantity.idxmax())
print("비인기 메뉴:", menu_quantity.idxmin())
time_sales = df.groupby("time_zone")["sales"].sum()

print()
print("===== 시간대별 매출 =====")
print(time_sales)
print()
print("매출이 가장 높은 시간대:", time_sales.idxmax())
age_menu = df.groupby(
    ["age_group", "menu_name"]
)["quantity"].sum()

print()
print("===== 나이대별 메뉴 판매량 =====")
print(age_menu)
gender_menu = df.groupby(
    ["gender", "menu_name"]
)["quantity"].sum()
print()
print("===== 성별별 메뉴 판매량 =====")
print(gender_menu)
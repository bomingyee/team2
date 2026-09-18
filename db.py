import os

from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]

supabase: Client = create_client(url, key)

class DB():
    # 전체 데이터 적재
    def save_data(user_info, order_info):

        # user_info
        # [user_id, user_name, gender, age]

        # order_info
        # [user_id, order_time, menu_id, quantity, price]

        # 1. users 테이블 적재
        user_data = {
            "user_name": user_info[1],
            "gender": user_info[2],
            "age": user_info[3]
        }

        user_result = (
            supabase
            .schema("cafe_project")
            .table("users")
            .insert(user_data)
            .select("user_id")
            .execute()
        )

        # DB에서 자동 생성된 user_id
        user_id = user_result.data[0]["user_id"]

        # 2. orders 테이블 적재
        order_data = {
            "user_id": user_id,
            "order_time": order_info[1]
        }

        order_result = (
            supabase
            .schema("cafe_project")
            .table("orders")
            .insert(order_data)
            .select("order_id")
            .execute()
        )

        # DB에서 자동 생성된 order_id
        order_id = order_result.data[0]["order_id"]

        # 3. order_items 테이블 적재
        item_data = {
            "order_id": order_id,
            "menu_id": order_info[2],
            "quantity": order_info[3],
            "menu_price": order_info[4]
        }

        item_result = (
            supabase
            .schema("starbucks")
            .table("order_items")
            .insert(item_data)
            .execute()
        )

        return [user_id, order_id]
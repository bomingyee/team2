
from datetime import datetime


class Order():
    def __init__(self):
        self.menus = {
            "1": {"menu_name": "아이스 카페 아메리카노", "menu_price": 4700},
            "2": {"menu_name": "아이스 카페 라떼", "menu_price": 5200},
            "3": {"menu_name": "아이스 바닐라 라떼", "menu_price": 5500},
            "4": {"menu_name": "제주 말차 크림 프라푸치노", "menu_price": 6500},
            "5": {"menu_name": "자바 칩 프라푸치노", "menu_price": 6500},
            "6": {"menu_name": "아이스 퓨어 말차", "menu_price": 5100},
            "7": {"menu_name": "복숭아 아이스 티", "menu_price": 6100},
            "8": {"menu_name": "모짜렐라 포크 커틀릿 샌드위치", "menu_price": 5400},
            "9": {"menu_name": "클래식 피낭시에", "menu_price": 3500}
        }

    def order_menu(self, user_id):
        print()
        print("===== 메뉴 =====")

        for menu_id, menu in self.menus.items():
            print(
                f"{menu_id}. "
                f"{menu['menu_name']} "
                f"{menu['menu_price']}원"
            )

        menu_id = input("\n주문할 메뉴 번호를 입력해주세요: ")

        if menu_id not in self.menus:
            print("잘못된 메뉴 번호입니다.")
            return

        quantity = int(input("수량을 입력해주세요: "))

        selected_menu = self.menus[menu_id]
        price = selected_menu["menu_price"]
        total_price = price * quantity
        order_time = datetime.now()

        print()
        print(
            f"{selected_menu['menu_name']} "
            f"{quantity}개 주문되었습니다."
        )
        print(f"총 금액은 {total_price}원입니다.")

        return [
            user_id,
            order_time,
            int(menu_id),
            quantity,
            price
        ]
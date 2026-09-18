class Order():
    def __init__(self):
        self.menus = {
            "1": {"menu_name": "아이스 아메리카노", "menu_price": 4700},
            "2": {"menu_name": "카페라떼", "menu_price": 5200},
            "3": {"menu_name": "콜드브루", "menu_price": 5500}
        }

    def order_drink(self):
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
        total_price = selected_menu["menu_price"] * quantity

        print()
        print(
            f"{selected_menu['menu_name']} "
            f"{quantity}잔 주문되었습니다."
        )
        print(f"총 금액은 {total_price}원입니다.")
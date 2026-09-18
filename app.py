from user import User
from order import Order
from db import DB

class App:
    def __init__(self):
        self.user = User()
        self.order = Order()
        self.db = DB()
        self.user_data = []
        self.user_id = 0
        self.order_data = []

    def select_menu(self):
        print()
        print("1. 회원 정보 입력하기 2. 주문하기 0. 종료하기")
        return input("메뉴를 선택해 주세요: ")

    def run(self):
        while True:
            # 메뉴 선택
            menu = self.select_menu()
            if menu == "1":
                # 회원 정보 입력
                self.user_data = self.user.get_user_info()
                self.user_id = self.user_data[0]
            elif menu == "2":
                # 주문하기
                self.order_data = self.order.order_drink(self.user_id)
            elif menu == "0":
                # 종료하기
                print()
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 번호입니다. 다시 선택해주세요.")

# test
# app = App()
# app.run()
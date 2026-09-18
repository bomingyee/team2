from user import User
from order import Order

class App:
    def __init__(self):
        self.user = User()
        self.order = Order()

    def select_menu(self):
        print()
        print("1. 회원 정보 수정 2. 주문하기 0. 종료하기")
        return input("메뉴를 선택해 주세요: ")

    def run(self):
        while True:
            # 메뉴 선택
            menu = self.select_menu()
            if menu == "1":
                # 회원 정보 수정
                self.user.get_user_info()
            elif menu == "2":
                # 주문하기
                self.order.order_drink()
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
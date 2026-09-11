from lunchmenu import LunchMenu
from history import History
from coffee import Coffee

class App:
    def __init__(self):
        self.lunchmenu = LunchMenu()
        self.history = History()
        self.coffee = Coffee()

    def select_menu(self):
        print()
        print("1. 점메추 2. 점메추 이력 3. 커피내기 4. 종료")
        return input("메뉴를 선택해 주세요: ")

    def run(self):
        while True:
            # 메뉴 선택
            menu = self.select_menu()
            if menu == "1":
                # 점메추
                self.lunchmenu.run()
            elif menu == "2":
                # 점메추 이력
                self.history.run()
            elif menu == "3":
                # 커피내기
                self.coffee.run()
            elif menu == "4":
                print()
                print("프로그램을 종료합니다.")
                break

# test
# app = App()
# app.run()
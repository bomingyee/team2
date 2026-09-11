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
        print("1. 점메추 2. 점심기록 3. 커피내기 4. 종료")
        return input("메뉴를 선택해 주세요: ")

    def run(self):
        while True:
            # 메뉴 선택
            menu = self.select_menu()
            if menu == "1":
                # 점메추
                self.lunchmenu.run()
            elif menu == "2":
                # 점심기록 하위 메뉴
                self.history.run()
            elif menu == "3":
                # 커피내기
                self.coffee.run()
            elif menu == "4":
                print()
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 메뉴입니다. 1~4 중에서 선택해 주세요.")

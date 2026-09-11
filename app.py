from line import Line
from station import Station
from contents import Contents

class App:
    def __init__(self):
        self.line = Line()
        self.station = Station()
        self.contents = Contents()

    def select_menu(self):
        print()
        print("1. 노선 보기 2. 노선 검색 3. 즐겨찾는 역 등록 4. 종료")
        return input("메뉴를 선택해 주세요: ")

    def run(self):
        while True:
            # 메뉴 선택
            menu = self.select_menu()
            if menu == "1":
                self.line.search()
            elif menu == "2":
                # 노선 검색
                # 역명을 입력하면 몇호선인지 알려줍니다.
                self.station.search()
            elif menu == "3":
                # 지하철에서 보기 좋은 컨텐츠
                self.contents.search()
            elif menu == "4":
                print()
                print("프로그램을 종료합니다.")
                break

# test
# app = App()
# app.run()
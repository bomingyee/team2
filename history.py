class History():
    def __init__(self):
        self.history = []

    def add_history(self):
        print("===== 이력 기록 =====")
        menu = input("메뉴 : ")
        price = int(input("가격 : "))

        self.history.append({"menu":menu, "price":price})
        
        print()
        print("기록되었습니다!")
        print(f"{menu} / {price}원")

        return self.history
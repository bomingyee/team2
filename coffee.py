import random


class Coffee():
    def __init__(self):
        pass

    def run(self):
        print()
        print("===================")
        print("===== 커피내기 =====")
        print("===================")

        people = []

        count = int(input("참여 인원 수 : "))

        for i in range(count):
            name = input(str(i + 1) + "번 : ")
            people.append(name)

        winner = random.choice(people)

        print()

        for i in range(4):
            print("두구두구...")

        print()
        print("커피 당첨자는...")
        print()
        print(winner)
        print()
        print("오늘 커피는", winner + "님이 쏩니다!!!!!")
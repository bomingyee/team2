## 1. 고객 정보 입력 
## 2. Insert 
class GetInfo : 
    def __init__(self) : 
        self.user_id = 0 
        self.users = []

    def get_info(self) :  
        self.user_id += 1 
                

        print("고객 정보를 입력합니다. : ")
        self.user_name= input("이름을 기재해주세요 : ")
        self.gender = input("성별을 입력해주세요(남성 혹은 여성으로 입력) : ")
        self.age = int(input("나이대를 입력해주세요(10, 20, 30, 40, 50, 60, 70, 80, 90, 100) : "))

        print(f"고객님의 ID는 {self.user_id}번 입니다. ")
        
        self.users = [self.user_id , self.user_name, self.gender , self.age ] 
        
        return self.users
        
##a = GetInfo()
##b= a.get_info()
##print(b)




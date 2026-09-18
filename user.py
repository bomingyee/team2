
class User():
    
    def __init__(self) : 
            self.user_id = 0 
            self.users = []
    
    def get_user_info(self) :  
        self.user_id += 1 

        print("\n고객 정보를 입력합니다.")

        self.user_name = input("이름을 기재해주세요 : ")
        
        while True:
            self.gender = input("성별을 입력해주세요(남성 혹은 여성으로 입력) : ")
            if self.gender in ["남성", "여성"]:
                break  # 올바르게 입력했으므로 while문 탈출
            else:
                print("❌ 에러: 남성과 여성 중에 입력해주세요.\n")

        
        self.valid_ages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        while True:
            try:
                self.age = int(input("나이대를 입력해주세요(10, 20, 30, 40, 50, 60, 70, 80, 90, 100) : "))
                
                # 입력한 숫자가 보기(10~100)에 있는지 확인
                if self.age in self.valid_ages:
                    break  # 올바른 숫자이므로 while문 탈출
                else:
                    print(f"❌ 에러: 제시된 나이대({self.valid_ages}) 중에서 입력해주세요.\n")
                    
            except ValueError:
                # 숫자가 아닌 문자열을 입력했을 때 예외 처리
                print("❌ 에러: 숫자를 입력하세요.\n")

        print(f"고객님의 ID는 {self.user_id}번 입니다. ")
        
        self.users = [self.user_id , self.user_name, self.gender , self.age ] 
        
        return self.users

a= User()
b= a.get_user_info()
print(b)
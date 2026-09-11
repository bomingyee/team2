import os
from google import genai
from google.genai import types

class Calories:

  def __init__(self, api_key: str = None):
    # 1. 인자로 키가 안 들어왔으면 환경 변수에서 확인
    if not api_key:
      api_key = os.environ.get("GEMINI_API_KEY")

    # 2. 여전히 키가 없다면 터미널에서 사용자에게 직접 입력받기
    if not api_key:
      api_key = input(
          "Google AI Studio에서 발급받은 API 키를 입력해주세요: "
      ).strip()

    # 3. 입력받은 키를 환경 변수와 client에 적용
    if api_key:
      os.environ["GEMINI_API_KEY"] = api_key
    else:
      raise ValueError("API 키가 제공되지 않아 실행할 수 없습니다.")

    self.client = genai.Client()

  def get_food_calories(self, food_name: str) -> str:
    system_instruction = (
        "너는 팩트를 기반으로 뼈를 아주 잘 때리는 직설적이고 유쾌한 다이어트 코치야."
        "사용자가 입력한 음식의 대략적인 칼로리를 분석하고 아래 규칙을 **반드시** 지켜서 답변해줘.\n"
        "1. 칼로리가 500kcal 이상이면 반드시 답변 맨 처음에 "
        '"🚨 [경고] 이거 먹으면 살쪄! (지방 축적 중...)" 라는 문구를 넣어줘.\n'
        "2. 칼로리가 200kcal 미만(너무 부실한 경우)이면 반드시 답변 맨 처음에 "
        '"🚨 [경고] 이걸로 밥이 돼? 쓰러져! 삐용삐용!" 이라는 문구를 넣어줘.\n'
        "3. 그 외의 경우에는 재치 있는 평범한 코멘트로 시작해줘.\n"
        "4. 마지막에는 간단한 영양 성분(탄수화물, 단백질, 지방)과 함께 정신 번쩍 들게 하는 조언을 덧붙여줘."
    )

    response = self.client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"음식 이름: '{food_name}'",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction, temperature=0.7
        ),
    )
    return response.text

  def run(self):
    print("\n===== AI 칼로리 계산기 =====")
    while True:
      user_input = input(
          "\n칼로리가 궁금한 음식을 입력하세요 (0 입력 시 종료): "
      )

      if user_input.strip() == "0":
        break

      if user_input.strip():
        print("\nAI가 팩트를 수집 중...\n")
        result = self.get_food_calories(user_input)
        print("🩺 다이어트 코치의 진단")
        print(result)
      else:
        print("음식 이름을 올바르게 입력해주세요.")
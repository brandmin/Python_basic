# 랜덤한 숫자를 만들기 위해 사용
import random

# 간단한 한글리스트 만들기
hanguls = list("가나다라마바사아자차카타파하")

# 파일을 쓰기 모드로 엽니다.
with open("info.txt", "w") as file:
  for i in range(1000):
    # 랜덤한 값을 변수로 생성
    name = random.choice(hanguls) + random.choice(hanguls)
    weight = random.randrange(40, 100)
    height = random.randrange(140, 200)
    # 텍스트 쓰기
    file.write("{}, {}, {}\n".format(name, weight, height))
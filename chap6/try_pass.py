# 변수 선언
list_input_a = ["52", "273", "32", "스파이", "103"]

# 반복 적용
list_number = []
for item in list_input_a:
  # 숫자 변환하여 리스트 추가
  try:
    float(item) # 예외 발생시 다음으로 진행x
    list_number.append(item)
  except:
    pass

# 출력
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))
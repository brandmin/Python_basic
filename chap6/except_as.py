list_number = [52, 273, 32, 72, 100]

try:
  number_input = int(input("정수 입력> "))
  # 리스트 요소 출력
  print("{}번째 요소: {}".format(number_input, list_number[number_input]))
# 예외 객체 활용
except ValueError as exception:
  print("정수를 입력해주세요!")
except IndexError as exception:
  print("리스트의 인덱스가 벗어났어요!")

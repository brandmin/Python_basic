list_number = [52, 273, 32, 72, 100]

try:
  number_input = int(input("정수 입력> "))
  # 리스트 요소 출력
  print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except Exception as exception:
  # 예외 객체 출력
  print("type(exception):", type(exception))
  print("exception:", exception)

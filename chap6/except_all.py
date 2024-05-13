list_number = [52, 273, 32, 72, 100]

try:
  number_input = int(input("정수 입력> "))
  # 리스트 요소 출력
  print("{}번째 요소: {}".format(number_input, list_number[number_input]))
  예외.발생해주세요()
except ValueError:
  print("정수를 입력해주세요!")
  print(type(exception), exception)
except IndexError:
  print("리스트의 인덱스가 벗어났어요!")
  print(type(exception), exception)
except Exception as exception:
  # 이외의 예외 발생
  print("미리 파악하지 못한 예외가 발생하였습니다.")
  print(type(exception), exception)

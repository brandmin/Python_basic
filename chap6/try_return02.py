def write_text_file(filename, text):
  try:
    file = open(filename, "w")
    # 여러가지 처리 수행
    return
    # 파일에 텍스트 입력
    file.write(text)
  except:
    print("오류가 발생했습니다.")
  finally:
    # 파일 닫기
    file.close()

# 함수 호출
write_text_file("test.txt", "안녕하세요!")
# 모듈 읽기
import sys

# 명령 매개변수 출력
print(sys.argv)
print("---")

# 컴퓨터 환경과 관련된 정보 출력
print("getwindowsversion:()", sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

# 프로그램 강제 종료
sys.exit()
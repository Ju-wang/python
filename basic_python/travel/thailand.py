class ThailandPackage:
    def detail(self):
        print("[Thailand] 50 dollar")


# 모듈을 안에서 직접 실행하는 것인지 밖에서 불러와서 실행하는 것인지 확인하기 위한 코드
if __name__ == "__main__":
    print("directly process Thailand modeul")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("call from outside of Thailand")

class Borg:
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        # Borg 객체의 모든 속성은 __dict__에 저장됨
        self.__dict__ = self.__shared_state
        pass
# Borg 혹은 모노스테이트 싱글톤은 서로 다른 객체를 만들어 사용하지만 객체들간의 상태는 서로 공유됨


# b와 b1은 서로 다른 객체임
b = Borg()
b1 = Borg()

print("[Before] Object b ", b.__dict__)
print("[Before] Object b1", b.__dict__)
# b 인스턴스를 이용해 속성을 변경
# Borg 객체의 __dict__가 변경
b.x = 4
print("[After] Object b ", b.__dict__)
print("[After] Object b1 ", b1.__dict__)

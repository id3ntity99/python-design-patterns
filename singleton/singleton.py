class Singleton(object):
    # Singleton 클래스 인스턴스 생성
    def __new__(cls):
        # cls == __main__.Singleton
        # 만약 Singleton 클래스에 instance 속성이 없을 경우
        if not hasattr(cls, "instance"):
            # instance 속성을 초기화
            # 부모클래스의 __new__ 메서드를 이용, Singleton 인스턴스를 생성
            cls.instance = super().__new__(cls)
        return cls.instance


# 서로 다른 객체임에도 불구하고 같은 인스턴스를 참조
s = Singleton()
print("Object created: ", s)

s1 = Singleton()
print("Object created: ", s1)

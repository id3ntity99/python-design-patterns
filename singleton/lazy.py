class Singleton:
    _instance = None

    # 인스턴스가 초기화 단계에서 이전에 생성된 인스턴스가 있는지를 확인
    def __init__(self):
        # 이전에 생성된 인스턴스가 없는 경우
        if not Singleton._instance:
            print("No instance")
        # 이전에 생성된 인스턴스가 있는 경우
        else:
            print("Instance already exists")

    # 클래스의 인스턴스를 만들지 않고도 메서드를 사용할 수 있도록
    # classmethod 데코레이터를 이용
    @classmethod
    def get_instance(cls):
        # 인스턴스가 없을 경우 인스턴스를 생성
        if not cls._instance:
            cls._instance = Singleton()
        # 이미 인스턴스가 있는 경우에는 그대로 반환
        return cls._instance


s = Singleton()
print("Creating Instance", Singleton.get_instance())
s1 = Singleton()

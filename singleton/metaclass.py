# 메타클래스는 클래스 객체를 만들기위한 클래스
class MetaSingleton(type):
    _instances = {}

    # 메타클래스가 실행되면 아래 메서드가 실행됨
    # *args 매개변수에는 class_name, bases, attrs가 포함됨
    def __call__(cls, *args, **kwargs):
        # 인스턴스가 이전에 생성되었는지를 확인
        if cls not in cls._instances:
            # type을 이용하여 인스턴스 생성
            # super().__call__ == type()
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


# Logger 클래스 객체가 생성되기 전, 메타클래스의 인스턴스가 실행됨
# 메타클래스 객체의 실행결과로 Logger 클래스가 만들어짐
logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)
print(logger1 == logger2)

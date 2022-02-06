from abc import ABCMeta, abstractmethod

# 팩토리를 사용하면 사용자가 직접 클래스를 호출하지 않고도 객체를 생성할 수 있음


# Abstract product
class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


# Concrete products
class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")


class PatentSection(Section):
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


class StateMessageSection(Section):
    def describe(self):
        print("State Message Section")


# Abstract Factory
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        self.sections.append(type(section).__name__)


# Concrete Factory
class linkedin(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PatentSection())
        self.add_sections(PublicationSection())


class Facebook(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())


class KakaoTalk(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())
        self.add_sections(StateMessageSection())


# Client
if __name__ == "__main__":
    li_profile = linkedin()
    print("Create profile for {}".format(type(li_profile).__name__))
    print(
        "{} profile has sections: {}".format(
            type(li_profile).__name__, li_profile.get_sections()
        )
    )
    kkt_profile = KakaoTalk()
    print("Create profile for {}".format(type(kkt_profile).__name__))
    print(
        "{} profile has sections: {}".format(
            type(kkt_profile).__name__, kkt_profile.get_sections()
        )
    )


"""
팩토리 메서드에서는 새로운 클래스나 기능을 추가하기가 쉽다.
가령, 위 코드에서 인스타그램 클래스를 만들어야한다고 가정해보자.
인스타그램은 PersonalSection, AlbumSection뿐만 아니라 StorySection과
LiveStreamingSection도 필요하다고 해보자. Concrete products에는 StorySection,
LiveStreamingSection이 없으므로 앞서 언급한 새로운 클래스 두 개를 만들어야 한다.
이 때, Abstract products를 상속하고 추상 메서드를 구현하기만하면 쉽게 두 Section을 만들 수 있다.
그리고 Instagram 클래스를 만들어야하는데, 이미 AbstractFactory의 역할을 하고있는 Profile 클래스가 있으므로
해당 클래스를 상속하고 add_sections() 메서드를 이용하여 create_profile() 추상 메서드만 구현해주면 끝이다
만약 팩토리 역할을 하는 추상 클래스 Profile이 없었다면 링크드인, 페이스북, 카카오톡,
인스타그램 클래스 모두 일일이 구현해줘야 했을 것이다. Concrete Factory 클래스들이 알아서 객체를 생성하고 활용하므로,
사용자 입장에서는 여러 객체를 생성하고 조합하는 과정을 피할 수 있다.

Factory method pattern의 전체적인 흐름은 다음과 같다.
1. Abstract Product 클래스를 만들고
2. 그 클래스를 이용해 Concrete Product 클래스들을 만든다.
3. Abstract Factory를 정의하고
4. Concrete Factory 클래스들이 그 클래스를 상속한다.
5. Concrete Factory 클래스가 직접 Concrete Products 객체를 생성한다.
6. 사용자는 Concrete Factory를 이용하여 원하는 기능을 구현한다.
"""

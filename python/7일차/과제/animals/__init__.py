from mammals import Dog
from birds import Eagle

dog = Dog("강아지")
eagle = Eagle("독수리")

print(f"{dog.name}는 소리를 내면 {dog.sound()}합니다.")
print(f"{eagle.name}는 소리를 내면 {eagle.sound()}합니다.")
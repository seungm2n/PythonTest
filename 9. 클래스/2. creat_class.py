class Monster:
    def say(self):
        print("안녕하세요. 몬스터입니다.")


mon = Monster()
mon.say()

print(type(mon))

a = 10
print(type(a))

b = "문자열객체"
print(type(b))
print(b.__dir__())
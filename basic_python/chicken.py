# 각자 에러 메세지를 다르게 할 경우에 사용한다
class NoIngredient(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


chicken = 10
waitting = 1

while(True):
    try:
        print("[left chicken]: {0}".format(chicken))
        order = int(input("how many chicken want to order?"))
        if order <= 0:
            print("please enter int")
        elif order > chicken:
            print("out of ingredients")
        else:
            print("[wating {0}] {1} chicken ordered".format(waitting, order))
            waitting += 1
            chicken -= order
            if chicken <= 0:
                raise NoIngredient("today market is close")
    except ValueError:
        print("please enter int")
    except NoIngredient as err:
        print(err)
        break

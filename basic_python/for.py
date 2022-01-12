from random import *

# customer = 50
# num = 0

# while customer > 0:
#     time = randint(1, 51)
#     print("{0}번째 손님 (소요시간: {1})".format(customer, time))
#     if time >= 5 and time <= 15:
#         num += 1
#     customer -= 1
#     if customer < 1:
#         print("총 탑승 승객:", num, "분")

cnt = 0
for customers in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[o] {0}번째 손님 (소요시간: {1})".format(customers, time))
        cnt += 1
    else:
        print("[] {0}번째 손님 (소요시간: {1})".format(customers, time))
print("총 탑승 승객: {0}분".format(cnt))

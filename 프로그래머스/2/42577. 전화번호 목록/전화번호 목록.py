'''
Point
1. 하나하나 다 따져보기 -> O(n^2) 너무 비효율적
2. O(2n) 방법이 없을까? 없는듯.. 하나하나 봐야하니까

공부 :
sort하면 앞에거가 뒤에거의 접두사가 됨
ex ) 12 13 1212 -> 12 1212 13

'''
def solution(phone_book):
    phone_book.sort()
    flag = True
    for i in range(1,len(phone_book)):
        if phone_book[i-1] == phone_book[i][:len(phone_book[i-1])]:
            flag = False
            break
    return flag
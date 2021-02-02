#리스트 선언 
#list_a  = [이 줄 앞 주석 제거 후 여기에 리스트를 입력하세요]
list_b  = [0]
list_c  = [0]
list_d  =[]
len_a   = len(list_a)
range_a = range(len_a)
a_ = 0

#크기 비교
for a in range(len_a - 1):
    list_b.append (0)
a = 0 
for a in range(len_a - 1):
    list_c.append (0)

for b in range(len(list_a)):
    for c in range(len(list_a)):
        if not c == b:
            if list_a[b] > list_a[c]:
                a_ += 1
    list_b[a_] = list_a[b]
    a_ = 0
    
for d in range_a:
    if list_b[d] == 0:
        list_b[d] =list_b[d-1]


average = 0
#평균
for e in range_a:
    average += list_a[e]

average /= len_a



#최빈값

f =0
mode = list_b
for g in range_a:
    for h in range_a:
        if  g != h:
            if list_a[g] ==list_a[h]:
                list_c[g] += 1
tof = True
ab = 0
while tof:
    if ab in list_c:
        ab += 1
    else:
        tof = False
        ab -= 1
tof =True
mode = list_b
ac = 0
if ab != 0:
    for i in range_a:
        if ab == list_c[i]:
            list_d.append(list_a[i])
            mode = list_d
        
mode = list_d
#중앙값

if len_a%2 == 0:
    median = (list_b[len_a//2] +list_b[(len_a//2) -1])/2
else:
    median = list_b[(len_a//2) ]
print("평균\t= " ,average)
print("중앙값\t= ",median)
print("최빈값\t= ",mode)

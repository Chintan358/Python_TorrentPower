l = ["Python","java","php","afdfdf","sql","oracle","node","angular","java"]

# print(l)

# for i in l:
#     print(i)

# print(l[0])
# print(l[1])
# print(l[-2])
# print(l[1:5])
# print(l[-3:-1])

# print("Python" in l)
# print("abcd" not in l)

rollno = [10,20,6,45,60,23,44,44]

# print(len(rollno))
# print(max(rollno))
# print(min(rollno))

# rollno.append(1000)
# rollno.pop()
# rollno.pop()

# rollno.extend("10")
# rollno.insert(3,3000)

# print(rollno.count(44))

# rollno.reverse()
# rollno.sort()
# rollno.remove(44)
# print(rollno)

from collections import deque
q = deque([10,20,30,40,50,60])
q.append(1000)
q.appendleft(5000)
q.pop()
q.popleft()
print(q)

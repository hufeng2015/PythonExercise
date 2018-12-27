import time

num = [5,12,3,4];
str=["1","123","9"]
for a,b in zip(num,str):
    print(b,'is',a)
print(sorted(num))

reversenum = sorted(num,reverse=True)
for x in reversenum:
    print(x)

a=[]
t0 = time.process_time()
for i in range(1,20000000):
    a.append(i)
print(f'Time:{time.process_time() - t0}')

t0 = time.process_time()
b = [i for i in range(1,20000000)]
print(f'Time:{time.process_time() - t0}')

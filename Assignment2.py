#1
x=[1,2,3,4,[10,20,30,40,[100,200,300,400],"rishabh_",5+5j],4000]
print(x[4][:2])
print(x[4][6])
print(x[4][4][2:6])
print(x[4][3:6])

#2
for i in range(0,21):
    #var = filter(lambda x:x%2 ==0, range(0,21))

    for j in range((i+1),22):
        if((i+j)%2==0):
            lst = [i]
            lst.append(j)
            lstm.append(lst)
print(lstm)



4#

from collections import Counter

x = "hello&*$$world"
y = Counter(x)
print ("count of & = " + str(y['&']) + (" count of $ = " + str(y['$'])))

#3

for x in range(0,50):
    cube = x*x*x
    if(cube>=0 and cube<=50 and cube%2!=0):
        print(cube)

#5

s=("Hello world I am learning python")
print(list(map(len, s.split())))

#6

list=[2,3,4,55,33]
z = ""
for y in list:
    if (isinstance(y,(int))):
        z="True"
        continue
    else:
        z="False"
        break
print(z)

#1



print('My name is "Kinjal". I love coding')
print("This is 'my first program'.")

print('Enter x value')
x=input()
print(type(x))

print('Enter y value')
y=input()
print(type(y))
print('Enter z value')
z=input()
print(type(z))

print('"Value1 = '+x+ ', Value2 = '+y+ ', Value3 = '+z+'"')

#2


print('Hello! My name is Kinjal')
print('"Hello I am a candidate"')
print('"234.56"')
print('"34"')
print('a+3j')


#3

x = 10+20*(45+67.0)
print(type(x))

x = (True and False) or False
print(type(x))

x = (True or True) and (not False and True)
print(type(x))

x = (3>89) or (34>32)
print(type(x))

x = not True and False
print(type(x))

#4


x=input('Enter any number')
if ((int(x)%2==0) and (int(x)%5==0)):
    print("Hurray it is what I am looking for")
else:
    print("Wrong input")

#5

x=input('Enter the number')
if (int(x)>=10 and int(x)<=50):
    print('Yes I am in the range')
else:
    print('Oops')
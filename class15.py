# int = int(input(' hello, your number '))
# newint = int + 1 
# word = ''
# for i in range(1,newint):
#    word = word + ' '+ str(i)
# print(word)

string = 'hello world'
now = string.split()
one = now[0] 
two = now[1]
now3 = one + " " + two
new = list(now3)
print(new)
done = 0
listo = 0
while listo < 5:
    if new[listo] == 'o':
        new[listo] = 'a'
    else:
        listo += 1
print(new)

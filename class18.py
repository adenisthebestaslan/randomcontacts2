# import random
# #SETTIN UP
# turn = 0
# def runout():
#     if turn == 4:
#         print(' you lose!!!!')
# lvl = 0
# fliper = [0,1]
# coin = fliper
# def coinflip():
#     global flipper, coin
#     coin = random.choice(fliper)
# #SERCH 
# newvar = 5
# mine  = ['o','x','-']
# set = 'x,x,x,x,x,'
# lvl += 1
# mine1 = ['0','x','x','[a its in this sector]','x','x']
# clue1 = 'the other side, the _nd.'
# ansr1 = '2nd'
# def check(themine,theclue,theansr):
#     global cmd, coin, turn, lvl
#     print(set)
#     if lvl == 1:
#         cmd = input(' COMMAND?? ')
#         if cmd == 'c':
#             coinflip()
#             if coin == 0:
#                     turn += 1
#                     print(themine)
#                     runout()
#     else: 
#         print('try again')

#     guess = input(theclue)
#     if guess == theansr:
#         print('congrats!! :)')
#         print(themine)
#     else: 
#         print('ooppppsieeee')
# #NOW LVL ORGANIZEATION.
# check(mine1,clue1,ansr1)
# print(lvl)
# mine2 = ['[0 this sector!]','x','x','a','x','x']
# clue2 = 'in the scale, this is the only base ten number besides 7 and 6 to start with s.'
# ansr2 = '2nd'
# check(mine2,clue2,ansr2)
# print(lvl)
# mine3 = ['0','x','x','a [--- is NOT DIRECTLY THERE BUT IN THE A SECTOR','X','X']
# clue3 = ' start of everything'
# ansr3 = 'a'
# print(lvl)
# check(mine3,clue3,ansr3)
# mine4 = ['0','a','b','c','d','e','f']
# clue4 = ' rhymes with d, not e'
# ansr4 = 'c'
# print(mine4)
# check(mine4,clue4,ansr4)

# ##Functions 
# num = 0
# yey = input(' thing to see typed a bunch of times : ')
# def ultraprint(theawnser):
#     global num, newnum,yey
#     print(theawnser)
#     if num < 5:
#         num = num + 1
#         ultraprint(yey)


# ultraprint(yey)
    
## Advanced Functions in python




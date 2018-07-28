python
import random
valholder =[0,0,0,0,0,0,0,0,0]
shd=['','','','','','','','','']
sign1='X'
sign2='O'
def win():
    pass
def funcp1():
    global valholder
    global shd
    win()
    in1=int(input('Player 1, please input position to make move.'))
    if valholder[in1]==0:
     valholder[in1]+=1
     shd[in1]='X'
     print(f"""
______________________
|  {shd[6]}   |   {shd[7]}  |  {shd[8]}   |
----------------------
|  {shd[3]}   |   {shd[4]}  |  {shd[5]}   |
----------------------
|  {shd[0]}   |   {shd[1]}  |  {shd[2]}   |
----------------------
     """)
    else:
        print("Input is invalid")
        funcp1()
    funcp2()
    
    
    
def funcp2():
    global valholder
    global shd
    win()
    in1=int(input('Player 2, please input position to make move.'))
    if valholder[in1]==0:
     valholder[in1]+=1
     shd[in1]='O'
     print(f"""
______________________
|  {shd[6]}   |   {shd[7]}  |  {shd[8]}   |
----------------------
|  {shd[3]}   |   {shd[4]}  |  {shd[5]}   |
----------------------
|  {shd[0]}   |   {shd[1]}  |  {shd[2]}   |
----------------------
     """)
    else:
        print("Input is invalid")
        funcp2()
    funcp1()



def game():
 global valholder
 global showholder
 print('Welcome to 2 player Simple tic-tac-toe game!')
 print('''
This is the game's board structure
______________________
|  6   |   7  |  8   |
----------------------
|  3   |   4  |  5   |
----------------------
|  0   |   1  |  2   |
----------------------

Player 1 = X 
Player 2 = O
Starting player is selected randomly
Please input number according to the place you wish to fill during your turn
''')
 aa=int(random.randint(0,101))
 if aa%2==0:
        print('Player 1 goes first')
        funcp1()
 else:
    print('Player 2 goes first')
    funcp2()
 print("Start")
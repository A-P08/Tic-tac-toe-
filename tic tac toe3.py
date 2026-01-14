while True:
  print("""
1.for start game
2.for exit game""")
  choice=int(input("\nenter choice: "))
  if choice==1:
       list1 = [
    [" ", "|", " ", "|", " "],
    ["-", "+", "-", "+", "-"],
    [" ", "|", " ", "|", " "],
    ["-", "+", "-", "+", "-"],
    [" ", "|", " ", "|", " "]
]

       for row in list1:
         print("".join(row))

       choose=input("\nchoose player 1 X or O:").upper()
       if choose=='X':
            player1="X"
            player2="O"
       elif choose=="O": 
            player1="O"
            player2="X"
       else:
            print("\nchoose valid!")
       pos_available=[1,2,3,4,5,6,7,8,9]
       while len(pos_available)>0:
         for x in range(0,1):
            print("\nplayer 1 your turn: ")
            print(pos_available)
            p=int(input(f"\nenter pos where you want to put {player1}:"))
            if p==1:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player1}:"))
                else:
                  list1[0][0]=player1
            elif p==2:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player1}:"))
                else:
                    list1[0][2]=player1
            elif p==3:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player1}:"))
                else:
                    list1[0][4]=player1
            elif p==4:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player1}:"))
                else:
                   list1[2][0]=player1
            elif p==5:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player1}:"))
                else:
                    list1[2][2]=player1
            elif p==6:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player1}:"))
                else:
                   list1[2][4]=player1
            elif p==7:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player1}:"))
                else:
                    list1[4][0]=player1
            elif p==8:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player1}:"))
                else:
                    list1[4][2]=player1
            elif p==9:
                      if 9 in pos_available:
                        list1[4][4] = player1  # or player2
                      else:
                         print("\nalready filled")
                         p=int(input(f"\n again enter pos where you want to put {player1}:"))

            else:
                print("invalid position")
         pos_available.remove(p)
         for row in list1:
           print("".join(row))
         if list1[0][0]==list1[0][2]==list1[0][4]==player1 or\
            list1[2][0]==list1[2][2]==list1[2][4]==player1 or\
            list1[4][0]==list1[4][2]==list1[4][4]==player1 or\
            list1[0][0]==list1[2][0]==list1[4][0]==player1 or\
            list1[0][2]==list1[2][2]==list1[4][2]==player1 or\
            list1[0][4]==list1[2][4]==list1[4][4]==player1 or\
            list1[0][0]==list1[2][2]==list1[4][4]==player1 or\
            list1[0][4]==list1[2][2]==list1[4][0]==player1 :
             print(f"\nplayer1 win!")
             break
         if pos_available==[]:
             print("\nDraw")
             break
         for x in range(0,1):
            print("\nplayer 2 your turn: ")
            print(pos_available)
            p=int(input(f"\nenter pos where you want to put {player2}:"))
            if p==1:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player2}:"))
                else:
                    list1[0][0]=player2
            elif p==2:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player2}:"))
                else:
                    list1[0][2]=player2
            elif p==3:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player2}:"))
                else:
                    list1[0][4]=player2
            elif p==4:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player2}:"))
                else:
                    list1[2][0]=player2
            elif p==5:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player2}:"))
                else:
                    list1[2][2]=player2
            elif p==6:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player2}:"))
                else:
                    list1[2][4]=player2
            elif p==7:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player2}:"))
                else:
                    list1[4][0]=player2
            elif p==8:
                if p not in pos_available:
                    print("\nalready filled")
                    p=int(input(f"\n again enter pos where you want to put {player2}:"))
                else:
                    list1[4][2]=player2
            elif p==9:
    
                if 9 in pos_available:
                        list1[4][4] = player2  # or player2
                else:
                         print("\nalready filled")
                         p=int(input(f"\n again enter pos where you want to put {player2}:"))
                
            else:
                print("invalid position")
         pos_available.remove(p)
         for row in list1:
          print("".join(row))       
         if list1[0][0]==list1[0][2]==list1[0][4]==player2 or\
            list1[2][0]==list1[2][2]==list1[2][4]==player2 or\
            list1[4][0]==list1[4][2]==list1[4][4]==player2 or\
            list1[0][0]==list1[2][0]==list1[4][0]==player2 or\
            list1[0][2]==list1[2][2]==list1[4][2]==player2 or\
            list1[0][4]==list1[2][4]==list1[4][4]==player2 or\
            list1[0][0]==list1[2][2]==list1[4][4]==player2 or\
            list1[0][4]==list1[2][2]==list1[4][0]==player2 :
             print(f"\nplayer2 win!")
             break
       
       

  elif choice==2:
        print("thank you")
        break
  else:
        print("invalid choice")
import os
while True:
    print("Type O to play \nType X to exit.")
    str=input("")
    if str=="o":
       a=" "
       b=" "
       c=" "
       d=" "
       e=" "
       f=" "
       g=" "
       h=" "
       i=" "
       def cls():
           os.system("cls")
       for n in range(10):
           cls()
           print("     |     |     ", end="\n")
           print(f"  {a}  |  {b}  |  {c}  ", end="\n")
           print("-----------------")
           print(f"  {d}  |  {e}  |  {f}  ", end="\n")
           print("     |     |     ", end="\n")
           print("-----------------")
           print(f"  {g}  |  {h}  |  {i}  ")
           print("     |     |     ", end="\n")
           num=int(input("Enter num "))
           if num==1:
              if n%2==0:
                g="x"
              else:
                g="o"
           elif num==2:
                if n%2==0:
                   h="x"
                else:
                   h="o"
           elif num==3:
                if n%2==0:
                   i="x"
                else:
                   i="o"
           elif num==4:
                if n%2==0:
                   d="x"
                else:
                   d="o"
           elif num==5:
                if n%2==0:
                   e="x"
                else:
                   e="o"
           elif num==6:
                if n%2==0:
                   f="x"
                else:
                   f="o"
           elif num==7:
                if n%2==0:
                   a="x"
                else:
                   a="o"
           elif num==8:
                if n%2==0:
                   b="x"
                else:
                   b="o"
           elif num==9:
                if n%2==0:
                   c="x"
                else:
                   c="o"
           if a==b==c=="x" or d==e==f=="x" or g==h==i=="x" or a==d==g=="x" or b==e==h=="x" or c==f==i=="x" or a==e==i=="x" or c==e==g=="x":
              cls()
              print("Congratulations")
              print("     |     |     ", end="\n")
              print(f"  {a}  |  {b}  |  {c}  ", end="\n")
              print("-----------------")
              print(f"  {d}  |  {e}  |  {f}  ", end="\n")
              print("     |     |     ", end="\n")
              print("-----------------")
              print(f"  {g}  |  {h}  |  {i}  ")
              print("     |     |     ", end="\n")
              break
           elif a==b==c=="o" or d==e==f=="o" or g==h==i=="o" or a==d==g=="o" or b==e==h=="o" or c==f==i=="o" or a==e==i=="o" or c==e==g=="o":
                cls()
                print("Congratulations")
                print("     |     |     ", end="\n")
                print(f"  {a}  |  {b}  |  {c}  ", end="\n")
                print("-----------------")
                print(f"  {d}  |  {e}  |  {f}  ", end="\n")
                print("     |     |     ", end="\n")
                print("-----------------")
                print(f"  {g}  |  {h}  |  {i}  ")
                print("     |     |     ", end="\n")
                break
    elif str=="x":
         break

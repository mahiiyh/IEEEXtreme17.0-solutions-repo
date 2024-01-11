cl = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] # card list
n = int(input())
if 1 <= n <= 25:
    for i in range(n):
        s1 = input().split()
        s2 = input().split()
        while ((s1 and s2) and (s1 != s2)):
            if cl.index(s1[0]) > cl.index(s2[0]):
                s1.remove(s1[0])
                s1.append(s2[0])
                s2.remove(s2[0])
            elif cl.index(s2[0]) > cl.index(s1[0]):
                s2.remove(s2[0])
                s2.append(s1[0])
                s1.remove(s1[0])  
            else:
                eq = s1[0]
                s1.remove(eq)
                s1.append(eq)
                s2.remove(eq)
                s2.append(eq)
                
        if s1 == s2:
            print('draw')
        elif s1:
            print('player 1')
        else:
            print('player 2')
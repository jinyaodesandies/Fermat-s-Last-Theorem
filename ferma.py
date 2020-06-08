wh=1
math=0

    
while wh==1:
        math+=1
        x = math
        if x>0:
            ans = x**(1./3.)
            if ans ** 3 != abs(x):
                print ("is not a perfect cube!")
        else:
            ans = -((-x)**(1./3.))
            if ans ** 3 != -abs(x):
                print("is not a perfect cube!")

        print ("Cube root of " + str(x) + " is " + str(ans))



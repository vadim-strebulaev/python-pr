ar = [" 𐤏 "] * 7
ar1 = [" 𐤏 "] * 7
ar2 = [" 𐤏 "] * 7
ar3 = [" 𐤏 "] * 7
ar4 = [" 𐤏 "] * 7
ar5 = [" 𐤏 "] * 7
# ◉ ●
kon = 1
mainArr = [ar, ar1, ar2, ar3, ar4, ar5]
thisArr = 0
setArr = 0
bekon = False
while(True):
    for i in range(len(mainArr)):
        print(''.join(mainArr[i]))
    x = int(input())
    if(x < 8 and x > 0):
        thisArr = x - 1
        i = 5
        while i >= 0:
            setArr = mainArr[i]
            if(setArr[thisArr] == " 𐤏 "):
                if(kon % 2 == 1):
                    setArr[thisArr] = " ● "
                else:
                    setArr[thisArr] = " ◉ "
                mainArr[i] = setArr
                bekon = True
                break
            i -= 1
        if(bekon == True):
            kon += 1
            bekon = False

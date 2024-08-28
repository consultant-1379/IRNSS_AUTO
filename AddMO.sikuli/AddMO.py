def GRAN_Add_Mo:
    find("1520329431529.png")
    click("1520329431529.png")
    find("1520329472672.png")
    click("1520329472672.png")
    find("1520329517568.png")
    click("1520329517568.png")
    rightClick("1520330793121.png")
    find("1520329611712.png")
    click("1520329611712.png")
    find("1520329651870.png")
    click("1520329651870.png")
    for i in range(10):
        type(Key.DOWN)
        type(Key.ENTER)
    wait(3)
    find("1520329978509.png")
    type("1520329994194.png", "5")
    find("1520330040772.png")
    click("1520330040772.png")
    if(exists("1520330671711.png")):
        find("1520330701726.png")
        click("1520330701726.png")
        find("1520330737461.png")
        click("1520330737461.png")
    else:
        wait(10)
        find("1520330737461.png")
        click("1520330737461.png")
    find("1520330793121.png")
    doubleClick("1520330793121.png")
    if(exists("1520331337367.png")):
        rightClick("1520331337367.png")
        find("1520331400554.png")
        click("1520331400554.png")
        find("1520331431944.png")
        click("1520331431944.png")
        wait(10)
        find("1520331474913.png")
        close("1520331474913.png")
    
    
    


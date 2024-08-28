def GRAN_CDM_STATUS():
    find(Pattern("1520940315159.png").similar(0.75).targetOffset(1,3)) #Finding Citrix button
    click("1520940315159.png") #Citrix Citrix button
    find("1520942091231.png") #Finding Terminal
    click("1520942091231.png") #Clicking Terminal
    type("1519821976130.png", "cdm_cli ") #Typing the command
    type("-status ")        #Typing the command 
    type("BSC117"+Key.ENTER) #Typing the command
    wait(7) #waiting for 7 seconds to produce the output
    if(exists("1519193279180.png")): #Checking the validation
        wait(5)
        find("1519193039055.png") #If the scripts executes successfully it finds and closes the window
        click("1519193039055.png")
    else: #If the scripts could not perform the above steps, it will jump to else part and exceutes below steps.
        type("opt/ericsson/bin/cns_im_interface BSC BSC117"+Key.ENTER)
        type("cdm_cli -stop BSC117 stopping node"+Key.ENTER)
        wait(15)
        type("gsm_sync"+Key.ENTER)
        wait(10)
        type("cdm_cli -start BSC117 starting node"+Key.ENTER)
        wait(10)
        type("cdm_cli –status BSC117"+Key.ENTER)
        find("1519193039055.png")
        click("1519193039055.png")

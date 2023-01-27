from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
class browser():
    def launch(self,First_window=None,Second_window=None, Third_window=None, Forth_Window=None):
        
                    from selenium import webdriver
                    from selenium import webdriver
                    from selenium.webdriver.chrome.options import Options
                    from selenium.webdriver.chrome.service import Service
                    global Driver
                    gh = open("mrobotics.txt")
                    gtxt = gh.readlines()
                    comp=gtxt[10]      
                    opt = Options()
                    capabilities = {'chrome.binary': comp}
                    opt.add_experimental_option("detach", True)
                    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
                    opt.headless=False
                    ser_obj=Service(executable_path="chromedriver.exe")
                    Driver = webdriver.Chrome(service=ser_obj, options=opt,desired_capabilities=capabilities) 
                    
                    Driver.set_window_size(1600,1000)
                    Driver.set_window_position (180,10) 
                    
                   
                    # Driver.maximize_window()
                    if First_window!=None:
                        Driver.get(First_window)
                        if Second_window!=None:
                            Driver.switch_to.new_window()
                            Driver.get(Second_window)
                            if Third_window!=None:
                                Driver.switch_to.new_window()
                                Driver.get(Third_window)
                                if Forth_Window!=None:
                                   Driver.switch_to.new_window()
                                   Driver.get(Forth_Window)
                                else:
                                     print("You Have Otpion to Provide One More Link.........    ")
                            elif Forth_Window!=None:
                                 Driver.switch_to.new_window()
                                 Driver.get(Forth_Window)
                            else:
                                print("You Have Otpion to Provide More Link.........    ")
                        elif Third_window!=None:
                             Driver.switch_to.new_window()
                             Driver.get(Third_window)
                        elif Forth_Window!=None:
                            Driver.switch_to.new_window()
                            Driver.get(Forth_Window)
                        else:
                             print("You Have Otpion to Provide More Link.........    ")
                    elif Second_window!=None:
                        Driver.switch_to.new_window()
                        Driver.get(Second_window)
                    elif Third_window!=None:
                        Driver.switch_to.new_window()
                        Driver.get(Third_window)
                    elif Forth_Window!=None:
                            Driver.switch_to.new_window()
                            Driver.get(Forth_Window)                    
                    else:
                        print("Please Give At Least one Link")
                    return Driver

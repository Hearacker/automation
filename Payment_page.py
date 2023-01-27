from Browser_class import *
def PayMent(Driver, WindowId,wait,cardNumber,cvv,Expiry_Month,Expiry_year,HolderName):
    Driver.switch_to.window(WindowId)
    i=1
    while i>0:
       try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='css-15vx72i']"))).click()
            i-=1
            break
       except:
        pass
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='cardNumber']"))).send_keys(cardNumber)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='cvvNumber']"))).send_keys(cvv)
    j=1
    while j>0:
        try:
              wait.until(EC.element_to_be_clickable((By.XPATH, "//div[2]/button[1]/div[2]/img"))).click()
              j-=1
              break
        except:
            pass
    sleep(0.1)
    month=['01 - January','02 - February','03 - March','04- April','05 - May','06 - June','07 - July','08 - August','09 - September','10 - October','11 - November','12 - December']
    ty=int(Expiry_Month)-1
    mont=month[ty]
    k=1
    while k>0:
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='"+str(mont)+"']"))).click()
            k-=1
            break
        except:
            pass
    l=1
    while l>0:
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH  , "//div[2]/button[2]/div[2]/img"))).click()
            l-=1
            break
        except:
            break

    try:
        for i in range(len(wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/div[5]/div/div/div[2]/div/div"))))):
                j = str(i+1)
                kk = Driver.find_element(By.XPATH, "/html/body/div/div[5]/div/div/div[2]/div/div["+j+"]/p")
                jj = kk.text
                if int(jj) == int(Expiry_year):
                    sleep(0.1)
                    kk.click()
                    break
    except:
        pass
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "cardHolderName"))).send_keys(HolderName)
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[3]/div/div/div[3]/button"))).click() 
    except:
        pass
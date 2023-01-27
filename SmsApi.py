from Browser_class import*
def SmsApiLOG(Driver,WindowId,wait,username,password):
    Driver.switch_to.window(WindowId)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='text-dark h6 mr-3 login-light']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='username']"))).send_keys(username)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-lg btn-primary btn-block']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Incomming SMS']"))).click()
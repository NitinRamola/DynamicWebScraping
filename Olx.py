from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/Users/nitin/Downloads/chromedriver_mac64/chromedriver')
def get_drvier():
    # Set options to make browsing easier
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    options = webdriver.ChromeOptions()
    options.add_argument("disable_infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(service=service,options=options)
    # driver=webdriver.Edge()
    driver.get("https://www.olx.in/dehradun_g4059236/cars_c84")
    return driver
def main():
    opt=[]
    driver = get_drvier()

    for i in range(1,1000):
        try:
            car_name = driver.find_element(by="xpath", value=f"/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div[1]/div[2]/ul/li[{i}]/a/div[1]/div[2]/div[2]")
            car_price = driver.find_element(by="xpath", value=f"/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div[1]/div[2]/ul/li[{i}]/a/div[1]/div[2]/div[1]")
            car_year = driver.find_element(by="xpath", value=f"/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div[1]/div[2]/ul/li[{i}]/a/div[1]/div[2]/div[3]")
            #print(type(car_name.text.lower()))
            ss=car_name.text.lower()
            if ss.find("thar")>0:
                #print(ss)
                #print("inside the loop")
                opt.append([car_name.text.lower(),car_price.text,car_year.text])

        except:
            pass
    return opt
ot=main()
print(*ot,sep='\n')

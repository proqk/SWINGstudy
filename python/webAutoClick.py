from selenium import webdriver

driver=webdriver.Chrome('/Users/proqk/Downloads/chromedriver_win32/chromedriver.exe') #크롬 드라이버
driver.get('http://zzzscore.com/1to50') #접속할 url


def autoClick():
    cnt = 1

    while cnt <= 50:
        btns= driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

        for btn in btns:
            if btn.text == str(cnt):
                btn.click()
                print("number "+str(cnt)+"clicked!")
                cnt+=1
                break

autoClick()

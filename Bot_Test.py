from selenium  import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Edge(executable_path = 'C:\Edge_Driver\msedgedriver.exe')
driver.get("http://game.granbluefantasy.jp/#mypage")
element = driver.find_element_by_xpath("//div[@class='prt-link-quest']")
element.click()


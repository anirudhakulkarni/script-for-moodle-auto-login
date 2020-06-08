import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
import getpass

# Change the username below to your keberos user name

u_name = "cs5190421"

####################################################################################################

driver = webdriver.Chrome()
driver.minimize_window()
driver.get("https://moodle.iitd.ac.in/login/index.php")

driver.find_element_by_id("details-button").click()
driver.find_element_by_id("proceed-link").click()

email = driver.find_element_by_id("username")
passwd = driver.find_element_by_id("password")
form = driver.find_element_by_id("login")
captcha = form.text


email.clear()
email.send_keys(u_name)
passwd.clear()
passwd.send_keys(getpass.getpass())

captcha = captcha.split('\n')[3]
# print(captcha)
captcha = captcha.split(" ")
# print(captcha)
res = 0

if "add" in captcha:
    num1 = int(captcha[2])
    num2 = int(captcha[4])
    res = num1 + num2
elif "subtract" in captcha:
    num1 = int(captcha[2])
    num2 = int(captcha[4])
    res = num1 - num2
elif "first" in captcha:
    num1 = int(captcha[4])
    num2 = int(captcha[6])
    res = num1
elif "second" in captcha:
    num1 = int(captcha[4])
    num2 = int(captcha[6])
    res = num2

# print(num1,num2,res)

captcha_field = driver.find_element_by_id("valuepkg3")
captcha_field.clear()
captcha_field.send_keys(str(res))
driver.find_element_by_id("loginbtn").click()
if driver.title == "Dashboard":
    print("Logged in succesfully")
else:
    print("Invalid Login credentials!!")
driver.maximize_window()
# driver.close()

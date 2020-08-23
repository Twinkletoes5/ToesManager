#trying to autofill into the Web


from selenium import webdriver

class InstaBot:
    def __init__(self):
        self.driver = webdriver.edge()
        self.driver.get("https://www.youtube.com/")

InstaBot()

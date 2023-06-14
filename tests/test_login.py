
from base.pageObjects.loginpage import loginpage
from base.tests.conftest import driver
from base.utilities.BaseClass import BaseClass


class login(BaseClass):

    def test_login(self):
        log = self.test_login(driver)
        login =loginpage(self,driver)
        login.username.send_keys("sasikumar@neokred.tech")
        login.password.send_keys("Neokred@123")
        login.login_button.click()








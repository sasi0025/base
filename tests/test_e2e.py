import time

from base.pageObjects.loginpage import loginpage
from base.utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_login(self):
        self.driver.implicitly_wait(5)
        log = self.test_login()
        login=loginpage(self.driver)
        login.implicitly_wait(5)
        login.username.send_keys("sasikumar@neokred.tech")
        login.password.send_keys("Neokred@123")
        login.login_button.click()
        otp=self.get_otp()
        login.otp_field.send_keys(otp)




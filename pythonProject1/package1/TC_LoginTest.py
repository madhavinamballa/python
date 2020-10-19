import unittest
class LoginTest(unittest.TestCase):
    def tets_loginbyEmail(self):
        print("Login by Email test")
        self.assertTrue(True)
    def tets_loginbyFacebook(self):
        print("Login by Facebook test")
        self.assertTrue(True)

    def tets_loginbytwitter(self):
        print("Login by twitter test")
        self.assertTrue(True)
if __name__=="__main__":
    unittest.main()
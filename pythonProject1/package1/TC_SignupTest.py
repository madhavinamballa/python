import unittest
class SignupTest(unittest.TestCase):
    def tets_signupbyEmail(self):
        print("Login by Email test")
        self.assertTrue(True)
    def tets_signupFacebook(self):
        print("Login by Facebook test")
        self.assertTrue(True)

    def tets_signuptwitter(self):
        print("Login by twitter test")
        self.assertTrue(True)
if __name__=="__main__":
    unittest.main()
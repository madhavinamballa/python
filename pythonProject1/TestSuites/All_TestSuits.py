import unittest
from package1.TC_LoginTest import LoginTest
from package1.TC_SignupTest import SignupTest

from package2.TC_PaymentTest import PaymentTest
from package2.TC_paymentReturns import PaymentReturnTest
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

sanityTestSuite=unittest.TestSuite(tc1,tc2)
functionalTestSuite=unittest.TestSuite(tc3,tc4)
masterTestSuit=unittest.TestSuite(tc1,tc2,tc3.tc4)


unittest.TextTestRunner().run(sanityTestSuite)

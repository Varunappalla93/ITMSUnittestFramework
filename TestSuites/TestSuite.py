import unittest
from TestCases.test_eventdescription import Eventdesctest
from TestCases.test_eventdetails import Eventdettest
from TestCases.test_eventsummary import EventSumtest
from TestCases.test_login_out import Logintest


tc1=unittest.TestLoader().loadTestsFromTestCase(Logintest)
tc2=unittest.TestLoader().loadTestsFromTestCase(EventSumtest)
tc3=unittest.TestLoader().loadTestsFromTestCase(Eventdettest)
tc4=unittest.TestLoader().loadTestsFromTestCase(Eventdesctest)

#Sanity test Suite
sanitytestsuite=unittest.TestSuite([tc1])

#Functional test Suite
functionaltestsuite=unittest.TestSuite([tc2,tc3,tc4])

#Run Suites
unittest.TextTestRunner().run(sanitytestsuite)
unittest.TextTestRunner().run(functionaltestsuite)

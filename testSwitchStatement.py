import unittest
from switchstatement import SwitchStatement

s=SwitchStatement()
s.default("Test")
s.case(index="+",cond="5")
s.default("help")
s.case("*","2*3")
class TestSwitch(unittest.TestCase):
    
    s=SwitchStatement()
    def test_case_number(self):
        self.assertTrue(SwitchStatement().case_number(2),{0:"",1:""})

    def test_case_num(self):
        self.assertTrue(SwitchStatement().case(index="+",cond="5"),{"+":5})

    def test_case_str(self):
        self.assertTrue(SwitchStatement().case(index="+",cond="Test"),{"+":"Test"})

    def test_default(self):

        self.assertTrue(SwitchStatement().default("Test"))

    def test_switch(self):
        s.case("*","2*3")
        print(s.switch(6)," test")
        self.assertEqual(s.switch(6),6)

    def test_switch_not_found(self):
        s.default("Test")
        
        self.assertTrue(s.switch("a"),"Test")

    def test_dic_clear(self):
        self.assertDictEqual(s.clearingClear(),{})

if __name__ == '__main__':
    unittest.main()
import unittest
import calculater

class TestCase(unittest.TestCase):
    def test_isNumber1(self):
        result = calculater.isNumber('HelloSE')
        act = False
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %r แต่ได้ %r' % (act, result))
    def test_isNumber2(self):
        result = calculater.isNumber('123.3025')
        act = True
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %r แต่ได้ %r' % (act, result))
    def test_isNumber3(self):
        result = calculater.isNumber('00000123.3025')
        act = True
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %r แต่ได้ %r' % (act, result))
    def test_isNumber4(self):
        result = calculater.isNumber('00000123..3025')
        act = False
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %r แต่ได้ %r' % (act, result))
    #-----------------------------------------------------------------------------------
    def test_isInt1(self):
        result = calculater.isInt('00000123.3025')
        act = False
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %r แต่ได้ %r' % (act, result))
    def test_isInt2(self):
        result = calculater.isInt('2365')
        act = True
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %r แต่ได้ %r' % (act, result))
    #-----------------------------------------------------------------------------------
    def test_isOperator1(self):
        result = calculater.isOperator('x')
        act = False
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %r แต่ได้ %r' % (act, result))
    def test_isOperator2(self):
        result = calculater.isOperator('/')
        act = True
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %r แต่ได้ %r' % (act, result))
    #-----------------------------------------------------------------------------------
    def test_add1(self):
        result = calculater.add(3, 6)
        act = 9
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))
    def test_add2(self):
        result = calculater.add(0.1, 0.2)
        act = 0.3
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %f แต่ได้ %f' % (act, result))
    #-----------------------------------------------------------------------------------
    def test_minus(self):
        result = calculater.minus(3, 6)
        act = -3
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))
    #-----------------------------------------------------------------------------------
    def test_mul(self):
        result = calculater.multipy(3, 6)
        act = 18
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))
    #-----------------------------------------------------------------------------------
    def test_div1(self):
        result = calculater.divi(10, 2.0)
        act = 5
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %d แต่ได้ %d' % (act, result))
    def test_div2(self):
        result = calculater.divi(10, 0)
        act = 'ZeroDivisionError'
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %s แต่ได้ %s' % (act, result))
    #-----------------------------------------------------------------------------------
    def test_isYN1(self):
        result = calculater.isYN('352')
        act = False
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %r แต่ได้ %r' % (act, result))
    def test_isYN2(self):
        result = calculater.isYN('y')
        act = True
        self.assertEqual(result, act, 'เกิดข้อผิดพลาดค่าที่ควรได้ %r แต่ได้ %r' % (act, result))

if __name__ == '__main__':
    unittest.main()
import Libreriacomplejos as lc
import unittest

class TestCibreriaComplejos(unittest.TestCase):

    #Casos prueba de la suma
    def test_sumacplx(self):
        #Primer caso de prueba
        suma1=lc.sumacplx((3,2),(-5,5.2))
        self.assertAlmostEqual(suma1[0], -2)
        self.assertAlmostEqual(suma1[1], 7.2)
        #Segundo caso de prueba
        suma2=lc.sumacplx((10,3),(9,2))
        self.assertAlmostEqual(suma2[0], 19)
        self.assertAlmostEqual(suma2[1], 5)
    
    #Casos prueba de la resta
    def test_restacplx(self):
        #Primer caso de prueba
        resta1=lc.restacplx((3,2),(-5,5.2))
        self.assertAlmostEqual(resta1[0], 8)
        self.assertAlmostEqual(resta1[1], -3.2)
        #Segundo caso de prueba
        resta2=lc.restacplx((10,3),(9,2))
        self.assertAlmostEqual(resta2[0], 1)
        self.assertAlmostEqual(resta2[1], 1)

    #Casos prueba de la multiplicación
    def test_multiplicacioncplx(self):
        #Primer caso de prueba
        multi1=lc.multicplx((3,2),(-5,5.2))
        self.assertAlmostEqual(multi1[0], -25.4)
        self.assertAlmostEqual(multi1[1], 5.6)
        #Segundo caso de prueba
        multi2=lc.multicplx((10,3),(9,2))
        self.assertAlmostEqual(multi2[0], 84)
        self.assertAlmostEqual(multi2[1], 47)

    #Casos prueba de la división
    def test_divisioncplx(self):
        #Primer caso de prueba
        div1=lc.divcplx((5,10),(4,3))
        self.assertAlmostEqual(div1[0], 2)
        self.assertAlmostEqual(div1[1], 1)
        #Segundo caso de prueba
        div2=lc.divcplx((-4,-4),(-4,4))
        self.assertAlmostEqual(div2[0], 0)
        self.assertAlmostEqual(div2[1], 1)
    
    #Casos de prueba del módulo
    def test_modulocplx(self):
        #Primer caso de prueba
        mod1=lc.modulocplx(0,-2)
        self.assertAlmostEqual(mod1, 2)
        #Segundo caso de prueba
        mod2=lc.modulocplx(3,-1)
        self.assertAlmostEqual(mod2, 3.16227766)

    #Casos de prueba del conjugado
    def test_conjugado(self):
        #Primer caso de prueba
        con1=lc.conjugadocplx(5,-5)
        self.assertAlmostEqual(con1[0], 5)
        self.assertAlmostEqual(con1[1], 5)
        #Segundo caso de prueba
        con2=lc.conjugadocplx(34,345)
        self.assertAlmostEqual(con2[0], 34)
        self.assertAlmostEqual(con2[1], -345)

    #Casos de prueba conversión polar a cartesiano
    def test_convptoc(self):
        #Primer caso de prueba
        ptoc1=lc.conversptoccplx(2,120)
        self.assertAlmostEqual(ptoc1[0], -1)
        self.assertAlmostEqual(ptoc1[1], 1.732050808)
        #Segundo caso de prueba
        ptoc2=lc.conversptoccplx(2,-75)
        self.assertAlmostEqual(ptoc2[0], 0.517638090)
        self.assertAlmostEqual(ptoc2[1], -1.93185165)

    #Casos de prueba conversión cartesiano a polar
    def test_convctop(self):
        #Primer caso de prueba
        ctop1=lc.conversctopcplx(1,(3**(1/2)))
        self.assertAlmostEqual(ctop1[0], 2)
        self.assertAlmostEqual(ctop1[1], 60)
        #Segundo caso de prueba
        ctop2=lc.conversctopcplx(-1,-(3**(1/2)))
        self.assertAlmostEqual(ctop2[0], 2)
        self.assertAlmostEqual(ctop2[1], 240)
    
    #Casos de prueba retorno de fase de un número complejo
    def test_fasecplx(self):
        #Primer caso de prueba
        fase1=lc.fasecplx(-1,-(3**(1/2)))
        self.assertAlmostEqual(fase1, 240)
        #Segundo caso de prueba
        fase2=lc.fasecplx(1,(3**(1/2)))
        self.assertAlmostEqual(fase2, 60)

if __name__ == '__main__':
    unittest.main()
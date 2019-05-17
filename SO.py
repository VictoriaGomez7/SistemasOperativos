class SistemasOperativos:
    def PedirNumeros(self):
        self.num1=int(input('Ingrese primer numero: '))
        self.num2 = int(input('Ingrese segundo numero: '))
       
    def Suma(self):
        suma=self.num1+self.num2
        print "La suma es:",suma
        
        

S=SistemasOperativos()
S.PedirNumeros()
S.Suma()

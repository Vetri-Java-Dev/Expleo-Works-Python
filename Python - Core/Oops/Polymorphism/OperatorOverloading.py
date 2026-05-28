class Complex:
    def __init__(self, r, i):
        self.r=r
        self.i=i
    
    def __add__(self, sec):
        r=self.r+sec.r
        i=self.i+sec.i

        return Complex(r,i)
    
    def __str__(self):
        return str(self.r)+" + "+str(self.i)+"i"
    
c1=Complex(5,3)
c2=Complex(3,5)

print(c1+c2)

        
class Base:
    p0=[0,0]
    p1=[0,0]
class Cytosine(Base):
    def __init__(self,canvas):
        self.canvas=canvas        
    def Visualize(self):
        self.create_rectangle(1,1,5,5)
        self.create_text('C')
    pass
class Adenine(Base):
    pass
class Thyrosine(Base):
    pass
class Urasil(Base):
    pass
class Guanine(Base):
    pass



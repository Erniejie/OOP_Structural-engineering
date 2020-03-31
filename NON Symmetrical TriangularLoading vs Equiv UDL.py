
#### EXAMPLE 2
"""  CASE - SIMPLY SUPPORTED BEAM: NON-SYMMETRICAL TRIANGULAR LOADING : Equivalent UDL  = (2/3)*peakDL   Page 18"""
"""  all examples based on the book: Structural Engineering Art and Approximation by Hugh Morrison-Manchester UK"""

class EquivalentUDL():      ####CASE 1: Equivalent UDL
    ### CONNECTORS
    def __init__(self,span,UDL,youngModulus,momentOfInertia):
        self.span  = span                       ####Span in meters
        self.UDL =UDL                           ###  UDL in kN.m
        self.youngModulus = youngModulus        #### E in N/mm^2
        self.momentOfInertia = momentOfInertia  ## I in mm^4

    ### METHODOLOGY

    def MaxShearLoad(self):
        return (1/3)*self.UDL*self.span
    def MaxBendingMoment(self):
        return (1/12)*(self.UDL*self.span**2)
    def MaxDeflection(self):
        return (1e12)*(5/576)*(self.UDL*self.span**4)/(self.youngModulus*self.momentOfInertia)


class NonSymmetricalTriangularDL():          # CASE 2 - ACTUAL STRUCTURE
     ### CONNECTORS
    def __init__(self, span, PeakDL, youngModulus, momentOfInertia):
        self.span = span                        ####Span in meters
        self.PeakDL = PeakDL                    ### Triangular Distributed load in kN.m
        self.youngModulus = youngModulus        #### E in N/mm^2
        self.momentOfInertia = momentOfInertia  ## I in mm^4

     ### METHODOLOGY

    def MaxShearLoad(self):
       return (1/3)*self.PeakDL*self.span

    def MaxBendingMoment(self):
        return (pow(3,1/2)/ 27) * (self.PeakDL*self.span **2 )

    def MaxDeflection(self):
        return (1e12) * (1 / 154) * (self.PeakDL * self.span ** 4) / (self.youngModulus * self.momentOfInertia)


    ### OUTPUT

x =EquivalentUDL(3,4,205000,615000000)

x.span = 10                        ### in m.
x.UDL = 15                        ### in kN.m
print(x.MaxShearLoad())              #### in kN
print(x.MaxBendingMoment())          ### kN.m
print(x.MaxDeflection())             ### in mm


y = NonSymmetricalTriangularDL(3,4,205000,615000000)

y.span = 10                          ### in m.
y.PeakDL = 15                     ### in kN
print(y.MaxShearLoad())              #### in kN
print(y.MaxBendingMoment())          ### kN.m
print(y.MaxDeflection())             #### in mm
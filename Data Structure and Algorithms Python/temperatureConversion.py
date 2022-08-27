def tempconversion(t):

    class Temperature:

        def __init__(self,t):
            self.t=t

        def convertcelsius(self):
            print(round((self.t-32)*5/9,2),"degree celsius")

        def convertfahrenheit(self):
            print(round((9*self.t/5 +32),2),"degree fahrenheit")

    temp=Temperature(t)
    temp.convertcelsius()
    temp.convertfahrenheit()

    

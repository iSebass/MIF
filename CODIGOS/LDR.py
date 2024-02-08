#this class created a ldr method that return read value


#import necesary modules


from machine import Pin,ADC

class LDR:
    
    #init a pin adc   
    def __init__(self,numero_pin):        
        self.Ldr = ADC(Pin(numero_pin))
        
    #get value LDR
    def getLdrValue(self):
        return self.Ldr.read_u16() * 100000 / 65535
        
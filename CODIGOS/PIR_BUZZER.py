from machine import Pin

class PIR:

    def __init__(self,numero_pin_pir):        
        self.PIR = Pin(numero_pin_pir,Pin.IN)
    
    def get_Value(self):
        return self.PIR.value()
    

      
        
    
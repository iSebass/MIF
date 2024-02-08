from machine import ADC,Pin 

class RELAY:
    
    def __init__(self,list_relays):        
        self.relays = [Pin(numberPin,Pin.OUT)for numberPin in list_relays]
        
    def set_relay(self,number):
        self.relays[number].on()
        
    def clear_relay(self,number):
        self.relays[number].off()
        


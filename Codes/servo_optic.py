import utime

from machine import Pin, PWM

from machine import Pin, PWM
 
 
class Servo:
    """ A simple class for controlling a 9g servo with the Raspberry Pi Pico.
 
    Attributes:
 
        minVal: An integer denoting the minimum duty value for the servo motor.
 
        maxVal: An integer denoting the maximum duty value for the servo motor.
 
    """
 
    def __init__(self, pin: int or Pin or PWM, minVal=2500, maxVal=7500):
        """ Creates a new Servo Object.
 
        args:
 
            pin (int or machine.Pin or machine.PWM): Either an integer denoting the number of the GPIO pin or an already constructed Pin or PWM object that is connected to the servo.
 
            minVal (int): Optional, denotes the minimum duty value to be used for this servo.
 
            maxVal (int): Optional, denotes the maximum duty value to be used for this servo.
 
        """
 
        if isinstance(pin, int):
            pin = Pin(pin, Pin.OUT)
        if isinstance(pin, Pin):
            self.__pwm = PWM(pin)
        if isinstance(pin, PWM):
            self.__pwm = pin
        self.__pwm.freq(50)
        self.minVal = minVal
        self.maxVal = maxVal
 
    def deinit(self):
        """ Deinitializes the underlying PWM object.
 
        """
        self.__pwm.deinit()
 
    def goto(self, value: int):
        """ Moves the servo to the specified position.
 
        args:
 
            value (int): The position to move to, represented by a value from 0 to 1024 (inclusive).
 
        """
        if value < 0:
            value = 0
        if value > 1024:
            value = 1024
        delta = self.maxVal-self.minVal
        target = int(self.minVal + ((value / 1024) * delta))
        self.__pwm.duty_u16(target)
 
    def middle(self):
        """ Moves the servo to the middle.
        """
        self.goto(512)
 
    def free(self):
        """ Allows the servo to be moved freely.
        """
        self.__pwm.duty_u16(0)



       
s1 = Servo(0)       # Servo pin is connected to GP0
led_pin = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
 
def servo_Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
def servo_Angle(angle):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    s1.goto(round(servo_Map(angle,0,180,0,1024))) # Convert range value to angle value
    
if __name__ == '__main__':
    while True:
        if led_pin.value() == 1:
            print("Turn left ...")
            for i in range(0,180,10):
                servo_Angle(i)
                utime.sleep(0.02)
            
        else:        
            print("Turn right ...")
            for i in range(180,0,-10):
                servo_Angle(i)
                utime.sleep(0.02)
            
             

        if led_pin.value() == 1:
            print("OK")
        else:
             print("ani hovno")





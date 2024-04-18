from machine import Pin,PWM
import time


buzzer = Pin(14,Pin.OUT)

buzzer_pwm = PWM(buzzer)
buzzer_pwm.freq(3145)

def buzz(duration):
    buzzer_pwm.duty_u16(32768)
    time.sleep(duration)
    buzzer_pwm.duty_u16(0)
buzz(5)    
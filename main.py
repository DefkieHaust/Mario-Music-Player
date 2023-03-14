from machine import Pin, PWM
import utime

E7 = 2637
F7 = 2794
C7 = 2093
G7 = 3136
G6 = 1568
E6 = 1319
A6 = 1760
B6 = 1976
AS6 = 1865
A7 = 3520
D7 = 2349

signal_intake = Pin(15, Pin.IN, Pin.PULL_DOWN)
output = Pin(0, Pin.OUT)
buzzer = PWM(output)
buzzer.duty_u16(0)
buzzer.freq(300)
mario = [
  E7, 
  E7,    
  0,   
  E7,  
  0,    
  C7,    
  E7,   
  0,       
  G7, 
  0,    
  0,    
  0,     
  G6,       
  0,
  0,
  0,    
  C7,  
  0,
  0,
  G6,
  0,
  0,
  E6,
  0,
  0,
  A6,
  0,
  B6,
  0,
  AS6,
  A6,
  0,
  G6,
  E7,
  0,
  G7,
  A7,
  0,
  F7,
  G7,
  0, 
  E7, 
  0, 
  C7,
  D7,
  B6,
  0,
  0,
  C7,
  0, 
  0, 
  G6,
  0, 
  0, 
  E6, 
  0,
  0,
  A6,
  0, 
  B6,
  0, 
  AS6,
  A6, 
  0, 
  G6, 
  E7, 
  0, 
  G7,
  A7,
  0, 
  F7,
  G7, 
  0, 
  E7, 
  0, 
  C7,
  D7,
  B6,
  0, 
  0, 
]

while True: 
  if signal_intake.value() == 1:
    for i in mario: 
      if i == 0:
        buzzer.duty_u16(0)  
      else:  
        buzzer.freq(i)   
        buzzer.duty_u16(32768)  
      utime.sleep(0.15)

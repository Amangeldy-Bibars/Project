import serial
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(3, GPIO.IN, initial=GPIO.LOW)
GPIO.setup(5, GPIO.IN, initial=GPIO.LOW)

# lsusb
# dmesg

# "/dev/ttyUSB0"

# "/dev/ttyACM0"

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=4800,
    timeout=1,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

packet = [0xF8, 0x55, 0xCE, 0x01, 0x00, 0x23, 0x00, 0x00]

byte_array = bytearray(packet)

while True:
    ser.write(packet)

    value=ser.read(16)

    print("value : ", end='')
    print(value)

    a = bytearray(b'')
    a.append(value[6])
    a.append(value[7])
    a.append(value[8])
    a.append(value[9])

    print(" a : ", end='')
    print(int.from_bytes(a, byteorder='little'))

    val_mass = int.from_bytes(a, byteorder='little')
    print(" val_mass : ", end='')
    print(val_mass)

    ser.close()

    #start pushbutton - start dosing - open the valve
    if (GPIO.input(3) == True):
        GPIO.output(8, GPIO.HIGH)

    #emergency stop
    if (GPIO.input(5) == True):
        GPIO.output(8, GPIO.LOW)

    #if there is a dosing process, we monitor
    if (GPIO.input(8) == True):
        if a > 1500 :
            GPIO.output(8, GPIO.LOW) # stop the dosing

    #sleep(1) # Sleep for 1 second

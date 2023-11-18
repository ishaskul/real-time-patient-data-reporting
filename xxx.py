import time
import serial

ser=serial.Serial(

port='/dev/ttyACM0',
baudrate=9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)
#counter="60"
#ser.write(counter)
#time.sleep(5)



while ser.is_open:
        if ser.inWaiting()>0:
            read_serial=ser.readline()
	#s[0] = str(int(ser.readline(),16))
	#print (s[0])
	#print (type(read_serial))
#	value=read_serial
#	if(value==""):
#            print("i got you")
#        else:
            print(read_serial)
        
        
        
        
        
        
ser.close()
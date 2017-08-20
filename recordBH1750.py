""" 
    Este programa lee la informacion del sensor conectado al arduino y la
    guarda en un archivo llamado datos.csv 
    
"""
import time
import argparse

from serial import Serial
from threading import Thread

def empty_serial_buffer(uart):
    while uart.inWaiting():
        rubish = uart.read()

class SerialReader(object):
    def __init__(self, port, time_interval):
        self._port = port
        self._time_interval = time_interval
        self._input_queue = []
        self._is_running = False
                
    def start(self):
        self._is_running = True
        self._uart = Serial(port=self._port, baudrate=9600, timeout=0.1)
        time.sleep(2)
        Thread(target=self._serialRead).start()
        Thread(target=self._serialWrite).start()
        
    def get_last_reading(self):
        return self._input_queue.pop(0)
        
    def in_waiting(self):
        return len(self._input_queue)

    def is_running(self):
        return self._is_running

    def stop_serial(self):
        self._is_running = False     
    
    def _serialWrite(self):
        initial = time.time()
        while self._uart.isOpen():
            if time.time() - initial >= self._time_interval:
                self._uart.write([0x7A])
                initial = time.time()
                
    def _serialRead(self):
        while self._uart.isOpen():
            if self._is_running:
                header = self._uart.read()
                if header:
                    if ord(header) == 0x6A:
                        tiempo = time.asctime().split(' ')[-2]
                        if self._uart.inWaiting() >= 2:
                            byte1 = self._uart.read(size=1)
                            byte2 = self._uart.read(size=1)
                            value = (ord(byte2) << 8) + ord(byte1)
                            self._input_queue.append((tiempo, value))
                    else:
                        empty_serial_buffer(self._uart)
            else:
                empty_serial_buffer(self._uart)
                self._uart.close()
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    description="generate datasets to test imputers")
    
    parser.add_argument('puerto',
                        help="nombre del puerto de comunicacion")
    parser.add_argument('-dt', '--dt',
                        help="intervalo de muestreo en segundos",
                        type=int,
                        default=30)
    args = parser.parse_args()
            
    reader = SerialReader(port=args.puerto, time_interval=args.dt)
    reader.start()
    
    counter = 0
    print("Saving time every {} seconds ...".format(args.dt))
    
    with open('datos.csv', 'a') as file:
        try: 
            while reader.is_running():
                if reader.in_waiting():
                    tiempo, value = reader.get_last_reading()
                    file.write(tiempo+','+str(value)+'\n')
                    counter += 1
                    print("Tiempo: {:10},".format(tiempo),
                          "Lux: {:6},".format(value),
                          "lecturas guardadas: {:10}".format(counter),
                          end='\r')
        except KeyboardInterrupt:
            reader.stop_serial()
                

                
                
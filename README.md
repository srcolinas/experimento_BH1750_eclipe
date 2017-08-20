# experimento_BH1750_eclipe
Este repositorio contiene el código para registrar con un fotómetro casero el eclipse del 21 de agosto de 2017.

**Materiales**
+ [Arduino](https://www.arduino.cc/)
+ Sensor BH1750 [opción 1](https://www.ardobot.com/catalogsearch/result/?q=BH1750&cat=) [opción 2](http://www.didacticaselectronicas.com/index.php/sensores/modulo-sensor-de-luz-detail)
+ Otros necesarios para hacer el soporte del fotómetro

**Requisitos de software**
+ Arduino IDE (para descargar el programa readBH1750.ino al Arduino)
+ Python 3.x (para guardar los datos en un archivo datos.csv)

**Nota:** El archivo recordBH1750.py se ha testeado en Python 3.5.2 únicamente, pero debe funcionar sin muchas dificultades en otras versiones

## Instrucciones
0. Instale la librería para usar el sensor [BH1750 con arduino](https://github.com/claws/BH1750)
1. Descargue los archivos de este repositorio
2. Abra el archivo readBH1750.ino que se encuentra dentro de la carpeta readBH1750 con el IDE the Arduino, compílelo y descárguelo a su Arduino
3. Desde su interfaz de línea de comandos diríjase a la carpeta dónde descargó el archivo recordBH1750.py (por ejemplo, escribiendo cd Downloads)
4. Ejecute el archivo de la siguiente manera: python recordBH1750.py [puerto]. Por ejemplo: python recordBH1750.py COM13

**Nota:** Por defecto, el programa recordBH1750.py registra los datos cada 30 segundos, pero esto se puede modificar utilizando el comando completo: python recordBH1750.py [puerto] -dt [intervalo de tiempo en segundos]. Por ejemplo, python recordBH1750.py COM13 -dt 2.


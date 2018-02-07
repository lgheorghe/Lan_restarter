# Lan_restarter
Stuff related to the Lan Restarter board of sensors

A quick guide to the Lan restarter board can be found <a href="https://wifimag.ro/pic/detail/lan-controller-v2-big.jpg">here</a>: 

![alt text](https://raw.githubusercontent.com/lgheorghe/Lan_restarter/lan-controller-v2.jpg)

The Lan restarter board has one DS18B20 temperature sensor mounted on the PCB, 3 external DS18B20 temperature sensors and a DHT22 temperature & humidity sensor attached to it.
A sample python script is provided that reads the xml data from the Lan restarter board (temperature and humidity values) and sends it to a socket on the emonPi that logs it to Emoncms.

# Lan_restarter
Stuff related to the Lan Restarter board of sensors

A quick guide to the Lan restarter board can be found <a href="https://wifimag.ro/pdf/lan-controller-v20-short-manual.pdf">here</a>.

![alt text](https://wifimag.ro/pic/detail/lan-controller-v2-big.jpg)

The Lan restarter board I am using has one DS18B20 temperature sensor mounted on the PCB, 3 additional external DS18B20 temperature sensors and a DHT22 temperature & humidity sensor attached to it.

A simple python script is used to read the xml data from the Lan restarter board (temperature and humidity values) and send it to a socket on the my emonPi that logs it to Emoncms.
From Emoncms I can graph the data into usefull dashboards.

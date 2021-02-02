# highfinesse_wavemeter
Python code to interface with HighFinesse WS8 wavemeter in server-client configuration for Linux

This code is to be used when a Windows computer is acting as a server and running wlmDataServer.exe, as supplied by HighFinesse. 
This code also assumes that the wlmData.so library supplied by HighFinesse has been installed on the server linux computer. 

To allow multiple computers to connect to the wavemeter simultaneously, a zmq socket is used to handle requests. 

Windows server:
running HighFinesse wavemeter Windows software
running wlmDataServer.exe

Linux server: 
running wavemeter_wrapper.py

Clients:
run wavemeter.py


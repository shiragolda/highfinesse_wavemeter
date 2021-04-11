# highfinesse_wavemeter
Python code to interface with HighFinesse WS8 wavemeter with support for server-client configuration for Linux

This code requires a Windows computer running the HighFinesse software with the wavemeter connected.  

To allow multiple computers to connect to the wavemeter simultaneously, a zmq socket is used to handle requests on a server computer running wavemeter_handler.py. 

If the server computer is NOT the same computer that is running the HighFinesse software:
  - the wavemeter computer must be running wlmDataServer.exe (supplied by HighFinesse). 
  - the server computer must have the wlmData.dll library installed (Windows) or wlmData.so library installed (Linux). These libraries are supplied by HighFinesse. 



# Requirements

python packages ctypes and zmq. Can be installed with
```
pip install ctypes, pyzmq
```


wavemeter.py can optionally stream data to an additional zmq port as a publisher.  

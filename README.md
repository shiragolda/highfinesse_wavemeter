# highfinesse_wavemeter
Python code to interface with HighFinesse WS8 wavemeter with support for server-client configuration for Linux

This code requires a Windows computer running the HighFinesse software. 

For use in server-client configuration, the Windows server computer must also be running wlmDataServer.exe (supplied by HighFinesse). 
The linux client must have the wlmData.so library installed (supplied by HighFinesse). 

To allow multiple computers to connect to the wavemeter simultaneously, a zmq socket is used to handle requests. 


# Requirements

python packages ctypes and zmq. Can be installed with
```
pip install ctypes, pyzmq
```


wavemeter.py can optionally stream data to an additional zmq port as a publisher.  

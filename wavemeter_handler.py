import zmq
import time
import socket

from ctypes import *

import os
#if __name__=='__main__':
#    os.chdir("/home/labuser/Insync/electric.atoms@gmail.com/Google Drive/code/highfinesse_wavemeter")

# wlmData.dll related imports
import wlmData
import wlmConst


##
def get_ip():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255',1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
    
    
##


class wmHandler:
    def __init__(self,port=9000):
        zmq_context = zmq.Context()
        self.port = port
        
        
        try:
            
            self.socket = zmq_context.socket(zmq.REP)
            self.socket.bind("tcp://*:%s"%self.port)
            self.ip = get_ip()

            print("Handling requests on %s:%s"%(self.ip,self.port))
            print('')
            
            try:
                self.dll = wlmData.LoadDLL()
                print("Loaded library")
                time.sleep(1)
            except Exception as e:
                print("Error loading wlmData library")
                print(e)
            
            
            while(True):
                self.handle()
        
        
        except Exception as e:
            if zmq.zmq_errno()==100:
                print("Handler already started")
            else:
                print(e)
                print('here')
        
    def handle(self):
        message = self.receive()
        
        returned = ""
        loc = {'self':self}
        
        try:
            exec('returned = self.dll.%s'%message,{},loc) #loc passes the dictionary of local variables. neccesary because exec() doesn't return anything
            returned = str(loc['returned'])
        except Exception as e:
            print(e)
        
        self.reply(returned)
        
    def receive(self):
        message = self.socket.recv()
        if isinstance(message,bytes): message = message.decode()
        return message #string

    def reply(self,message):
        #print(message)
        if isinstance(message,str): message = message.encode()
        self.socket.send(message) #send as bytes
        
    def close(self):
        self.socket.close()
    


        
if __name__=='__main__':
    handle = wmHandler()

def data_get():
   g = nextCmd(SnmpEngine()
   , CommunityData('public', mpModel=1)
   , UdpTransportTarget(('demo.snmplabs.com', 161))
   , ContextData()
   , ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysObjectID', 0)))
   for errorIndication, errorStatus, errorIndex, varBinds in g:  

       if errorIndication:    
           print(errorIndication)
       elif errorStatus:
           print('%s at %s' % (
   errorStatus.prettyPrint(),
   errorIndex and varBinds[int(errorIndex) - 1][0] or '?'
)
)
   else:


       for varBind in varBinds:

           print(' = '.join([x.prettyPrint() for x in varBind])) 
def data_set():
   g = getCmd(SnmpEngine()
   , CommunityData('public', mpModel=1)
   , UdpTransportTarget(('demo.snmplabs.com', 161))
   , ContextData()
   , ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysORDescr', 1)))
   errorIndication, errorStatus, errorIndex, varBinds = next(g)
   for varBind in varBinds:

      print(' = '.join([x.prettyPrint() for x in varBind]))



########################################################################
import socket
from pysnmp.hlapi import*
host, port =('', 5556)
serveur= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((host, port))
print("le serveur est demarré...")

while True:
    serveur.listen(5)
    conn, addr = serveur.accept()
    print("En écoute...")

    while True:  
       se=SnmpEngine() 
       data1= conn.recv(1024)
       data1= data1.decode("utf8")
       print (data1)   
       if data1=='get':
          a=data_get()
          print(a)
       if data1== 'set':
          a=data_set()
          print(a)

conn.close()
socket.close()

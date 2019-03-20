##Ruben Guzman
##A client setup that will handle data transfer from leap motion server
import os, sys, inspect, thread, time, select, msvcrt, struct
import csv
import subprocess
import re
import socket
import cPickle as pickle

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name #replace the IP with your host desktop IP
host = "10.0.0.17"                          

#use port 9999
port = 9999

# connection to hostname on the port.
s.connect((host, port))

print 'Connected to Leap Motion Server...Data will stream from host after recording is done'                              

#create csv in current path
dir = os.path.dirname(os.path.realpath(__file__))
csv = open(str(dir.replace("\\","/")) + "/animDataClient.csv", 'w+b')

#Receive no more than 1024 bytes  
data = s.recv(1024)                                  
while (data):
	#handling the file transfer
	print "Receiving Leap Motion Data..."
	csv.write(data)
	data = s.recv(1024)

print "Press a key to finish"

try:
	sys.stdin.readline()
except KeyboardInterrupt:
	pass
finally:
	print "Closing"
	csv.close()
	s.close()
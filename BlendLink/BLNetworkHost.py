import socket
import threading
from flask import Flask
from flask_restful import Resource, Api

class BLNetworkHost:
    
    NodeAddress = ""
    ServerAddress = ""
    NodePort = 0
    LocalStatus = "uninitialized"
    LocalType = "uninitialized"
    
    def __init__(self, nodeType, nodePort, remoteServer):
        
        self.NodeAddress = socket.gethostbyname(socket.gethostname())
        self.LocalType = nodeType
        self.NodePort = nodePort
        if self.LocalType == "SERVER_TYPE_MAIN":
            self.ServerAddress = self.NodeAddress
        else:
            self.ServerAddress = remoteServer
        
        # Start flask/restful 
        self.HostApp = Flask(__name__)
        self.HostApi = Api(self.HostApp)

        self.SetupHostServer()

    def SetupHostServer(self):
        self.HostApi.add_resource(PingEndpoint, '/ping')
        self.ApiThread = threading.Thread(target=lambda: self.HostApp.run(self.NodeAddress, self.NodePort, False))

class PingEndpoint(Resource):
    
    def get(self):
        jsonResponse = { "online" : True, "status" : "idle"  }
        return jsonResponse, 200
    

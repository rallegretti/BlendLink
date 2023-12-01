import sys
import platform
import socket
import logging
import PySimpleGUI as sg

class BLNode:
    NodeAddress = ""
    NodeName = "uninitialized"
    NodeOS = "agnostic"
    NodeCores = -1
    NodeStatus = "OFFLINE"
    NodeType = ""
    NodePort = 0
    MainNodeAddress = ""
    
    def __init__(self):
        self.NodeAddress = socket.gethostbyname(socket.gethostname())
        self.NodeName = socket.gethostname()
        self.NodeOS = platform.system()
    
    def SetupNode(self):
        # Prompt for Server Type
        self.PromptNodeType()
        
        # Prompt for Server Port
        self.PromptNodePort()
        
        # Prompt for Server Address (maybe)
        if self.NodeType == "SERVER_TYPE_REMOTE":
            self.PromptServerAddress()
        else:
            self.MainNodeAddress = self.NodeAddress

        # Set up Main Window

        # Set up Local API

        # Register with Main Server (if applicable)

        return self
    
    def PromptNodeType(self):
        server_type_controls = [
            [sg.Text("Each system should only have one Main type node.", key="lbl_server_type_buttons", expand_x=True)],
            [sg.Button("Main", key="SERVER_TYPE_MAIN")],
            [sg.Button("Remote",key="SERVER_TYPE_REMOTE")]
        ]
        
        server_type_layout = [
            [sg.Frame("Server Type?", server_type_controls, key="frm_server_type_buttons", expand_x=True)]
        ]
        
        window = sg.Window("Select Server Port", server_type_layout, size=(600,200))
        event, values = window.Read()
        window.close()
        logging.info("PromptServerType Return:", event)
        self.NodeType = event
        return event
    
    def PromptNodePort(self):
        server_port_controls = [
            [sg.Text("The port to use for main/remote server communication.", key="lbl_server_port_field", expand_x=True)],
            [sg.Text("Port:", key="btn_server_port_text", expand_x=True)],
            [sg.Input("",key="server_port_input_value", expand_x=True)],
            [sg.Button("Set Port",key="btn_server_port_submit", expand_x=True)]
        ]
        
        server_port_layout = [
            [sg.Frame("Server Port?", server_port_controls, key="frm_server_port_controls", expand_x=True)]
        ]
        
        window = sg.Window("Select Server Port", server_port_layout, size=(600,200))
        event, values = window.Read()
        window.close()
        logging.debug("PromptServerPort Return:", values['server_port_input_value'])
        self.NodePort = values['server_port_input_value']
        return values['server_port_input_value']
    
    def PromptServerAddress(self):
        server_addr_controls = [
            [sg.Text("The IP address of the main server.", key="lbl_server_addr_field", expand_x=True)],
            [sg.Text("Address:", key="btn_server_addr_text", expand_x=True)],
            [sg.Input("",key="server_addr_input_value", expand_x=True)],
            [sg.Button("Set Address",key="btn_server_addr_submit", expand_x=True)]
        ]
        
        server_addr_layout = [
            [sg.Frame("Server Address?", server_addr_controls, key="frm_server_addr_controls", expand_x=True)]
        ]
        
        window = sg.Window("Select Server Address", server_addr_layout, size=(600,200))
        event, values = window.Read()
        window.close()
        logging.debug("PromptServerAddress Return:",values['server_addr_input_value'])
        self.MainNodeAddress = values['server_addr_input_value']
        return values['server_addr_input_value']
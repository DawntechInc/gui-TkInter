import logging
import sys
import socket
import threading
import os
import asyncio
import tkinter
import tkinter.messagebox
import webbrowser
import ctypes
import webbrowser
import signal

from tkinter import font

class ServerGui(tkinter.Tk):

    def __init__(self, parent, port):
        self.port = port
        tkinter.Tk.__init__(self, parent)
        self.parent = parent


def run(port):
    App = ServerGui(None, port) # Start the gui
    App.title("GUI")

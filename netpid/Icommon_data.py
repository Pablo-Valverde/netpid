from typing import Iterable
from netstat import netstat


NETSTAT = netstat()
WELL_KNOWN = list(range(1,1023)) 
REGISTERED_PORTS = list(range(1024,49151))
DYNAMIC_PORTS = list(range(49152,65535))

ALL_TRUE = [True,True,True,True,True,True,True]
DIR_TRUE = [False,False,False,False,False,True,True]

class config:
    def __init__(self) -> None:
        self.ports = WELL_KNOWN.copy() + DYNAMIC_PORTS.copy() + REGISTERED_PORTS.copy()
        self.show = [True,True,True,True,True,True,True]
        self.check = [True,True]
        self.arg_queue = []

conf = config()
class udp:
    def __init__(self, local, remote, pid) -> None:
        self.protocol = "UDP"
        local = str(local)[::-1].split(':',1)
        self.local = direction(local[1][::-1], local[0][::-1])
        remote = str(remote)[::-1].split(':',1)
        self.remote = direction(remote[1][::-1], remote[0][::-1])
        self.pid = str(pid)

    def __str__(self) -> str:
        return self.protocol + " " + str(self.local) + " " + str(self.remote) + " " + self.pid

class tcp(udp):
    def __init__(self, local, remote, status, pid) -> None:
        super().__init__(local, remote, pid)
        self.protocol = "TCP"
        self.status = str(status)
    
    def __str__(self) -> str:
        return self.protocol + " " + str(self.local) + " " + str(self.remote) + " " + self.status + " " + self.pid

class direction:
    def __init__(self, ip, port) -> None:
        self.ip = str(ip)
        self.port = str(port)

    def __eq__(self, o: object) -> bool:
        if o.__str__() == self.__str__():
            return True
        return False

    def __str__(self) -> str:
        return self.ip + ":" + self.port
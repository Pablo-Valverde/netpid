from connection import udp,tcp


class netstat:

    __open_con : str
    __open_con_formatted : list
    __tcp : list
    __udp : list
    __all : list

    def __init__(self) -> None:
        self.update()

    def update(self) -> None:
        import os
        import re
        self.__open_con = os.popen("netstat -ano").read()
        __con_list = self.__open_con.split("\n")
        self.__open_con_formatted = []
        for con in __con_list:
            con = re.split("\s{2,10000}", con, flags=re.UNICODE)[1:]
            self.__open_con_formatted.append(con)
        self.__open_con_formatted = self.__open_con_formatted[4:]
        self.__create_dicts()

    def get_tcp(self) -> list:
        return self.__tcp

    def get_udp(self) -> list:
        return self.__udp

    def get_all(self) -> list:
        return self.__all

    def get_pid(self, pid) -> list:
        result = []
        pid = str(pid)
        for con in self.__all:
            if con.pid == pid:
                result.append(con)
        return result

    def get_local(self, local) -> list:
        result = []
        local = str(local)
        for con in self.__all:
            if con.local.ip == local:
                result.append(con)
        return result

    def get_remote(self, remote) -> list:
        result = []
        remote = str(remote)
        for con in self.__all:
            if con.remote.ip == remote:
                result.append(con)
        return result

    def __create_dicts(self) -> None:
        self.__tcp = []
        self.__udp = []
        for con in self.__open_con_formatted:
            if con.__len__() == 0:
                continue
            if con[0] == 'TCP':
                self.__tcp.append(tcp(con[1], con[2], con[3], con[4]))
            else:
                self.__udp.append(udp(con[1], con[2], con[3]))
        self.__all = self.__tcp + self.__udp
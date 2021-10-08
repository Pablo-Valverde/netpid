from Icommon_data import NETSTAT, conf, config

opt = conf
opt:config

def get_status() -> list:
    result = []
    for status in opt.arg_queue:
        for con in __check_cons(NETSTAT.get_all()):
            if con.protocol == "TCP" and con.status.upper() == str(status).upper():
                result.append(con)
    return result

def get_tcp() -> list:
    return __check_cons(NETSTAT.get_tcp())

def get_udp() -> list:
    return __check_cons(NETSTAT.get_udp())

def get_remote() -> list:
    result = []
    for remote in opt.arg_queue:
        result += __check_cons(NETSTAT.get_remote(remote))
    return result

def get_all() -> list:
    return __check_cons(NETSTAT.get_all())

#Get all the conections that live on the specified pid, called with "-pid".
def get_pid() -> list:
    result = []
    for pid in opt.arg_queue:
        for con in __check_cons(NETSTAT.get_all()):
            if con.pid == pid:
                result.append(con)
    return result

#Get all the conections that focus on the specified local direction, called with "-local".
def get_local() -> list:
    result = []
    for local in opt.arg_queue:
        result += __check_cons(NETSTAT.get_local(local))
    return result

def __check_cons(cons) -> list:
    result = []
    for con in cons:
        if int(con.local.port) in opt.ports and opt.check[0] or not con.remote.port == '*' and (int(con.remote.port) in opt.ports and opt.check[1]):
            result.append(con)
    return result

#Output opt, executed last.
options = {
    "pid":get_pid,
    "local":get_local,
    "remote":get_remote,
    "all":get_all,
    "tcp":get_tcp,
    "udp":get_udp,
    "status":get_status
}
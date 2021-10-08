from io import StringIO
from typing import Callable
from Ioptions import options as opt
from Iconfig_options import config_options
from time import sleep
from Icommon_data import conf, config

options = conf
options:config

#Checks the arguments and give the output.
def analyze(*args) -> None:
    #Initial check, search for the functionality options and execute them first.
    for arg in args:
        arg = str(arg)
        if not arg[0] == '-':
            options.arg_queue.insert(0, arg)
            continue
        arg = arg[1:]
        try:
            __get_conf(arg.split(":")[0])()
        except KeyError:
            pass
        options.arg_queue.clear() 
    #Last check, execute the non-functionality options, giving the desired output.
    result = __get_opt("all")()
    first = True
    for arg in args:
        arg = str(arg)
        if not arg[0] == '-':
            options.arg_queue.insert(0, arg)
            continue
        arg = arg[1:]
        try:
            if first:
                result = __get_opt(arg)()
                first = False
            else:
                aux = __get_opt(arg)()
                result = list(set(result) & set(aux))               
        except KeyError:
            try:
                __get_conf(arg)
            except KeyError:
                raise Exception("Invalid option '" + arg + "'")
        finally:
            options.arg_queue.clear()

    if not result.__len__() > 0:
        print("No connection found")
        sleep(10)
        return
    line = __as_string(result)
    print(line)

def __as_string(result) -> str:
    line = ""
    for con in result:
        if options.show[0]:
            line += con.protocol + " "
        if options.show[1]:
            if options.show[5]:
                line += con.local.ip
            if options.show[5] and options.show[6]:
                line += ":" + con.local.port
            elif options.show[6]:
                line += con.local.port
            line += " "
        if options.show[2]:
            if options.show[5]:
                line += con.remote.ip
            if options.show[5] and options.show[6]:
                line += ":" + con.remote.port
            elif options.show[6]:
                line += con.remote.port
            line += " "
        if options.show[3] and con.protocol == "TCP":
            line += con.status + " "
        if options.show[4]:
            line += con.pid + " "
        line += "\n"
    line = line[:line.__len__()-1]
    return line

def __get_opt(option) -> Callable:
    return opt[option]

def __get_conf(option) -> Callable:
    return config_options[option]
from Icommon_data import conf, config

options = conf
options:config


#Specifies the port that the program must check, called with "-port".
def set_ports() -> None:
    from Icommon_data import WELL_KNOWN, DYNAMIC_PORTS, REGISTERED_PORTS
    global options
    options.ports = []
    for port in options.arg_queue:
        try:
            if not int(port) in options.ports:
                options.ports.append(int(port))
        except:
            port:str
            if port.upper() == "WELL" or port.upper() == "KNOWN" or port.upper() == "WELLKNOWN":
                options.ports = list(set(options.ports) | set(WELL_KNOWN.copy()))
                continue
            if port.upper() == "DYNAMIC" or port.upper() == "PRIVATE" or port.upper() == "EPHEMERAL":
                options.ports = list(set(options.ports) | set(DYNAMIC_PORTS.copy()))
                continue
            if port.upper() == "REGISTERED":
                options.ports = list(set(options.ports) | set(REGISTERED_PORTS.copy()))
                continue
            if port.upper() == "ALL":
                options.ports = WELL_KNOWN.copy() + DYNAMIC_PORTS.copy() + REGISTERED_PORTS.copy()
                return
            option = port.split(':')
            command = option[0]
            if command == "check":
                options.check[0] = False
                options.check[1] = False
                if not option.__len__() > 1:
                    continue
                args = option[1]
                for arg in args.split(','):
                    if arg.upper() == "LOCAL":
                        options.check[0] = True
                    elif arg.upper() == "REMOTE":
                        options.check[1] = True
                    elif arg.upper() == "ALL":
                        options.check[0] = True
                        options.check[1] = True

    if options.ports.__len__() == 0:
        from time import sleep
        print("No valid port has been given, looking well known ports.")
        sleep(3)
        options.ports = WELL_KNOWN.copy()
        return

#Changes the output of the program, called with "-options.show".
def set_format() -> None:
    from Icommon_data import ALL_TRUE, DIR_TRUE
    global options
    if options.arg_queue.__len__() == 0:
        options.show = ALL_TRUE.copy()
        return
    options.show = DIR_TRUE.copy()
    for arg in options.arg_queue:
        arg = str(arg)
        if arg.upper() == "LONG" or arg.upper() == "L":
            options.show = ALL_TRUE.copy()
            return
        elif arg.upper() == "SHORT" or arg.upper() == "S":
            options.show = ALL_TRUE.copy()
            return
        elif arg.upper() == "PROTOCOL":
            options.show[0] = True
        elif arg.split(":")[0].upper() == "DIRECTION" or arg.split(":")[0].upper() == "DIR":
            arg = arg.split(':')
            options.show[5] = False
            options.show[6] = False
            if arg.__len__() > 1:
                dir = arg[1].split(',')
                for opt in dir:
                    if opt.upper() == "IP":
                        options.show[5] = True
                    elif opt.upper() == "PORT":
                        options.show[6] = True
        elif arg.upper() == "LOCAL":
            options.show[1] = True
        elif arg.upper() == "REMOTE":
            options.show[2] = True
        elif arg.upper() == "STATUS":
            options.show[3] = True
        elif arg.upper() == "PID":
            options.show[4] = True
    if [val for val in options.show if val == True]:
        return
    options.show = ALL_TRUE.copy()

#Functionality options, modify the program output and other program caracteristics.
config_options = {
    "port":set_ports,
    "show":set_format
}
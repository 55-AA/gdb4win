import os
import re
import gdb

def gdb_exec(command):
    return gdb.execute(command, to_string=True)

def gdb_pid(procname):
    filelines = os.popen("ps -x|grep " + procname, "r")
    for line in filelines:
        if not line:
            continue
        line, count = re.subn('^\s+', '', line)
        results = re.split("\s+", line)
        if procname == results[4]:
            return results[0]

    return None

HEXSTR = "0123456789abcdef"
def ishex(data):
    data = data.lower()
    if '0x' == data[:2]:
        data = data[2:]
    for x in data:
        if x not in HEXSTR:
            return None
    return '*0x' + data

REGSTR = (
    "al", "ah", "ax", "eax", "rax",
    "cl", "ch", "cx", "ecx", "rcx",
    "dl", "dh", "dx", "edx", "rdx",
    "bl", "bh", "bx", "ebx", "rbx",
    "si", "esi", "rsi",
    "di", "edi", "rdi",
    "bp", "ebp", "rbp",
    "sp", "esp", "rsp",
    "ip", "eip", "rip",
    "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15",
    "r8d", "r9d", "r10d", "r11d", "r12d", "r13d", "r14d", "r15d"
    )

def isreg(data):
    data = data.lower()
    if data not in REGSTR:
        return None
    return '$' + data

class Mod(gdb.Command):
    """print modules infomation."""

    def __init__(self):
        gdb.Command.__init__(self, "mod", gdb.COMMAND_OBSCURE)

    def invoke(self, arg, from_tty):

        procinfo = gdb_exec("info proc")
        lines = procinfo.split("\n")
        pid = ""
        for line in lines:
            if("process " == line[:8]):
                pid = line[8:]
                break

        os.system("cat /proc/%s/maps" % pid) 

Mod()

class Oep(gdb.Command):
    """Prints the entry point address of the target and stores it in the variable entry_point."""

    def __init__(self):
        gdb.Command.__init__(self, "oep", gdb.COMMAND_OBSCURE)

    def invoke(self, arg, from_tty):

        fileinfo = gdb_exec("info files")
        lines = fileinfo.split("\n")
        for line in lines:
            divstr = line.split("Entry point:")
            if(2 == len(divstr)):
                if "noprint" != arg:
                    print(line)
                EntryPoint = divstr[1]
                gdb_exec("set $entry_point_address = " + EntryPoint)
                break

Oep()

class Atn(gdb.Command):
    """
    Attach process by name.
    Example:
        atn babyuse
    """

    def __init__(self):
        gdb.Command.__init__(self, "atn", gdb.COMMAND_OBSCURE)

    def invoke(self, arg, from_tty):
        pid = gdb_pid(arg)
        if not pid:
            print('cannot found "' + arg + '" to attach.')
            return

        print("attach to \"%s\" (pid=%s)." % (arg, pid))            
        gdb.execute("attach " + pid)

Atn()

class Db(gdb.Command):
    """
    Display 8 lines of a hex dump of address starting at ADDR.
    Example:
        db eax
        db 0xB7FFF918
        db main    
    """
    def __init__(self):
        gdb.Command.__init__(self, "db", gdb.COMMAND_OBSCURE)

    def invoke(self, arg, from_tty):
        addr = isreg(arg)
        if not addr:
            addr = arg
        gdb.execute("_db " + addr)

Db()

class Dd(gdb.Command):
    """
    Display 8 lines of a hex dump of address starting at ADDR.
    Example:
        dd eax
        dd 0xB7FFF918
        dd main    
    """
    def __init__(self):
        gdb.Command.__init__(self, "dd", gdb.COMMAND_OBSCURE)

    def invoke(self, arg, from_tty):
        addr = isreg(arg)
        if not addr:
            addr = arg
        gdb.execute("_dd " + addr)

Dd()

class Dq(gdb.Command):
    """
    Display 8 lines of a hex dump of address starting at ADDR.
    Example:
        dq eax
        dq 0xB7FFF918
        dq main    
    """

    def __init__(self):
        gdb.Command.__init__(self, "dq", gdb.COMMAND_OBSCURE)

    def invoke(self, arg, from_tty):
        addr = isreg(arg)
        if not addr:
            addr = arg
        gdb.execute("_dq " + addr)

Dq()

class Uu(gdb.Command):
    """diassembly 8 instruction of address starting at ADDR."""

    def __init__(self):
        gdb.Command.__init__(self, "uu", gdb.COMMAND_OBSCURE)

    def invoke(self, arg, from_tty):
        addr = isreg(arg)
        if not addr:
            addr = arg
        gdb.execute("_uu " + addr)

Uu()

class Bp(gdb.Command):
    """
    Set a normal breakpoint.
    Example:
        bp eax
        bp 0xB7FFF918
        bp main
    """

    def __init__(self):
        gdb.Command.__init__(self, "bp", gdb.COMMAND_OBSCURE)

    def invoke(self, arg, from_tty):
        addr = ishex(arg)
        if not addr:
            addr = arg
        gdb.execute("_bp " + addr)

Bp()

class Bpt(gdb.Command):
    """
    Set a temporary breakpoint.
    Example:
        bpt eax
        bpt 0xB7FFF918
        bpt main
    """

    def __init__(self):
        gdb.Command.__init__(self, "bpt", gdb.COMMAND_OBSCURE)

    def invoke(self, arg, from_tty):
        addr = ishex(arg)
        if not addr:
            addr = arg
        gdb.execute("_bpt " + addr)

Bpt()

class Bph(gdb.Command):
    """
    Set a hardware breakpoint.
    Example:
        bph eax
        bph 0xB7FFF918
        bph main
    """

    def __init__(self):
        gdb.Command.__init__(self, "bph", gdb.COMMAND_OBSCURE)

    def invoke(self, arg, from_tty):
        addr = ishex(arg)
        if not addr:
            addr = arg
        gdb.execute("_bph " + addr)

Bph()

class Bpht(gdb.Command):
    """
    Set a temporary hardware breakpoint.
    Example:
        bpht eax
        bpht 0xB7FFF918
        bpht main
    """

    def __init__(self):
        gdb.Command.__init__(self, "bpht", gdb.COMMAND_OBSCURE)

    def invoke(self, arg, from_tty):
        addr = ishex(arg)
        if not addr:
            addr = arg
        gdb.execute("_bpht " + addr)

Bpht()

class Bpm(gdb.Command):
    """
    Set a read/write breakpoint.
    Example:
        bpm eax
        bpm 0xB7FFF918
        bpm main
    """

    def __init__(self):
        gdb.Command.__init__(self, "bpm", gdb.COMMAND_OBSCURE)

    def invoke(self, arg, from_tty):
        addr = ishex(arg)
        if not addr:
            addr = arg
        gdb.execute("_bpm " + addr)

Bpm()
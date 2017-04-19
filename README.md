# gdb4win

gdb4win is running in linux，unix and mac x86 platform.

## Introduction

This tool is a extend for linux gdb, so that the Windbg command style can be uesd. In addition, there are some binary debug utils with python extend.

## How to start

Copy local.gdbinit.x64 or local.gdbinit.x86 to ～/.gdbinit, and copy pygdb.py to ～/pygdb.py.

## Example

+ Type "myhelp" to get suppurted command list. Type "help command" to get more detial information.

> 
    (gdb) myhelp
        goep
        init start cstart main
        bp bpt bph bpht bpm bl bc be bd
        db dd dq dsp dpc
        nn ss gg
        uu upc
        reg
        mod
        oep
        pret
        atn
        Type 'help <cmd>' to get more detial information.
    (gdb) help atn
        Attach a running process by name.
        Example:
            atn ./babyrun
    (gdb)

+ Lunch a program and break at entry point.

>
    (gdb) goep
    => 0x80000ca0:	xor    ebp,ebp
       0x80000ca2:	pop    esi
       0x80000ca3:	mov    ecx,esp
       0x80000ca5:	and    esp,0xfffffff0
       0x80000ca8:	push   eax
       0x80000ca9:	push   esp
       0x80000caa:	push   edx
       0x80000cab:	call   0x80000cd2
    (gdb)


+ Set break point.
>
    (gdb) bp 0x80000ca0
    Breakpoint 3 at 0x80000ca0
    (gdb)

+ Step over a x86 instruction.
>
    (gdb) nn
    0x80000ca2 in ?? ()
    => 0x80000ca2:	pop    esi

+ Step into a x86 instruction.
>
    (gdb) ss
    0x80000ca3 in ?? ()
    => 0x80000ca3:	mov    ecx,esp
    (gdb)

+ Display memory.
>
    (gdb) db 0x80000ca0
    [0x007B:0x80000CA0]-------------------------------------------------------[data]
    0x80000CA0 : 31 ED 5E 89 E1 83 E4 F0 - 50 54 52 E8 22 00 00 00 1.^.....PTR."...
    0x80000CB0 : 81 C3 F4 32 00 00 8D 83 - 9C D7 FF FF 50 8D 83 3C ...2........P..<
    0x80000CC0 : D7 FF FF 50 51 56 FF B3 - 58 00 00 00 E8 67 FF FF ...PQV..X....g..
    0x80000CD0 : FF F4 8B 1C 24 C3 66 90 - 66 90 66 90 66 90 66 90 ....$.f.f.f.f.f.
    0x80000CE0 : 8B 1C 24 C3 66 90 66 90 - 66 90 66 90 66 90 66 90 ..$.f.f.f.f.f.f.
    0x80000CF0 : E8 17 01 00 00 81 C2 AF - 32 00 00 8D 8A 64 00 00 ........2....d..
    0x80000D00 : 00 8D 82 67 00 00 00 29 - C8 83 F8 06 76 17 8B 82 ...g...)....v...
    0x80000D10 : 28 00 00 00 85 C0 74 0D - 55 89 E5 83 EC 14 51 FF (.....t.U.....Q.
    (gdb) dd eax
    [0x007B:0xB7FFF918]-------------------------------------------------------[data]
    0xB7FFF918 : 80000000 B7FFFC04 80003E9C B7FFFC08
    0xB7FFF928 : 00000000 B7FFF918 00000000 B7FFFBF8
    0xB7FFF938 : 00000000 80003EA4 80003F14 80003F0C
    0xB7FFF948 : 00000000 80003EE4 80003EEC 00000000
    0xB7FFF958 : 00000000 00000000 80003EF4 80003EFC
    0xB7FFF968 : 80003EAC 80003EB4 00000000 00000000
    0xB7FFF978 : 00000000 80003F2C 80003F34 80003F3C
    0xB7FFF988 : 80003F1C 80003F04 80003F44 80003F24
    (gdb) dq edi
    [0x007B:0x80000CA0]-------------------------------------------------------[data]
    0x80000CA0 : 00000000895EED31 00000000E8525450
    0x80000CB0 : 0000000032F4C381 00000000FFFFD79C
    0x80000CC0 : 0000000050FFFFD7 0000000000000058
    0x80000CD0 : 000000001C8BF4FF 0000000090669066
    0x80000CE0 : 00000000C3241C8B 0000000090669066
    0x80000CF0 : 00000000000117E8 000000008D000032
    0x80000D00 : 0000000067828D00 0000000006F883C8
    0x80000D10 : 0000000000000028 0000000083E58955
    (gdb) dd esp
    [0x007B:0xBFFFF750]-------------------------------------------------------[data]
    0xBFFFF750 : 00000001 BFFFF87E 00000000 BFFFF89A
    0xBFFFF760 : BFFFF8AB BFFFF8BB BFFFF8C6 BFFFF8E6
    0xBFFFF770 : BFFFF8F9 BFFFF903 BFFFFE8B BFFFFE97
    0xBFFFF780 : BFFFFED9 BFFFFEED BFFFFEFC BFFFFF13
    0xBFFFF790 : BFFFFF24 BFFFFF2D BFFFFF38 BFFFFF40
    0xBFFFF7A0 : BFFFFF52 BFFFFF5F BFFFFF91 BFFFFFC4
    0xBFFFF7B0 : 00000000 00000020 B7FD9DA4 00000021
    0xBFFFF7C0 : B7FD9000 00000010 0FABFBFF 00000006
    (gdb) dd esp+10
    [0x007B:0xBFFFF760]-------------------------------------------------------[data]
    0xBFFFF760 : BFFFF8AB BFFFF8BB BFFFF8C6 BFFFF8E6
    0xBFFFF770 : BFFFF8F9 BFFFF903 BFFFFE8B BFFFFE97
    0xBFFFF780 : BFFFFED9 BFFFFEED BFFFFEFC BFFFFF13
    0xBFFFF790 : BFFFFF24 BFFFFF2D BFFFFF38 BFFFFF40
    0xBFFFF7A0 : BFFFFF52 BFFFFF5F BFFFFF91 BFFFFFC4
    0xBFFFF7B0 : 00000000 00000020 B7FD9DA4 00000021
    0xBFFFF7C0 : B7FD9000 00000010 0FABFBFF 00000006
    0xBFFFF7D0 : 00001000 00000011 00000064 00000003

+ List modules information.
>
    (gdb) mod
    80000000-80003000 r-xp 00000000 08:01 327211     /root/babyrun
    80003000-80004000 r--p 00002000 08:01 327211     /root/babyrun
    80004000-80005000 rw-p 00003000 08:01 327211     /root/babyrun
    80005000-8002a000 rw-p 00000000 00:00 0          [heap]
    b7c18000-b7c1a000 rw-p 00000000 00:00 0 
    b7c1a000-b7c36000 r-xp 00000000 08:01 394499     /lib/i386-linux-gnu/libgcc_s.so.1
    b7c36000-b7c37000 rw-p 0001b000 08:01 394499     /lib/i386-linux-gnu/libgcc_s.so.1
    b7c37000-b7c8a000 r-xp 00000000 08:01 394529     /lib/i386-linux-gnu/libm-2.23.so
    b7c8a000-b7c8b000 r--p 00052000 08:01 394529     /lib/i386-linux-gnu/libm-2.23.so
    b7c8b000-b7c8c000 rw-p 00053000 08:01 394529     /lib/i386-linux-gnu/libm-2.23.so
    b7c8c000-b7e39000 r-xp 00000000 08:01 394462     /lib/i386-linux-gnu/libc-2.23.so
    b7e39000-b7e3b000 r--p 001ac000 08:01 394462     /lib/i386-linux-gnu/libc-2.23.so
    b7e3b000-b7e3c000 rw-p 001ae000 08:01 394462     /lib/i386-linux-gnu/libc-2.23.so

+ diassembly instruction.
>
    (gdb) uu 0x80000ca0
       0x80000ca0:	xor    ebp,ebp
       0x80000ca2:	pop    esi
    => 0x80000ca3:	mov    ecx,esp
       0x80000ca5:	and    esp,0xfffffff0
       0x80000ca8:	push   eax
       0x80000ca9:	push   esp
       0x80000caa:	push   edx
       0x80000cab:	call   0x80000cd2

+ attach a running program.
>
    (gdb) atn ./babyrun
    attach to "./babyrun" (pid=7204).
    0xb773fdad in __kernel_vsyscall ()

## Reference

+ [https://github.com/gdbinit/Gdbinit/blob/master/gdbinit](https://github.com/gdbinit/Gdbinit/blob/master/gdbinit)
+ [https://sourceware.org/gdb/current/onlinedocs/gdb/Python-API.html](https://sourceware.org/gdb/current/onlinedocs/gdb/Python-API.html)

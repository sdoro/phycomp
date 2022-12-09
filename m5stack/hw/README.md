
### Alcune note imparate 'sul campo'


Se si vuole reimpostare 'da zero' la box occorre un erase della flash
prima del burn. Questo ricostruirà la key e cancellerà o reimposterà
la configurazione WiFi.

$ esptool.py -p /dev/ttyUSB0 erase_flash


Nei sistemi linux dove potrebbe essere installato Python versione 2
è bene lanciare il comando:

	sudo ln -s /usr/bin/python3 /usr/bin/python

questo permette di risolvere il problema in M5Burner di terminare
con errore quando si imposta il WiFi.

### in data 24.11.2021

Ho provato a installare UIFlow per Core2 e ha funzionato!
Funziona anche l'immagine Core2_Tools

## in data 09.12.2022

Ho provato (Ubuntu 22.04), dopo un read_mac, ad attivare REPL
e funziona:

	picocom /dev/ttyUSB0 -b115200
picocom v3.1

port is        : /dev/ttyUSB0
flowcontrol    : none
baudrate is    : 115200
parity is      : none
databits are   : 8
stopbits are   : 1
escape is      : C-a
local echo is  : no
noinit is      : no
noreset is     : no
hangup is      : no
nolock is      : no
send_cmd is    : sz -vv
receive_cmd is : rz -vv -E
imap is        : 
omap is        : 
emap is        : crcrlf,delbs,
logfile is     : none
initstring     : none
exit_after is  : not set
exit is        : no

Type [C-a] [C-h] to see available commands
Terminal ready
00:22:57

rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
configsip: 188777542, SPIWP:0xee
clk_drv:0x00,q_drv:0x00,
>>>

# Un CTRL-D provoca questo output
MPY: soft reboot

       _  __ _               
 _   _(_)/ _| | _____      __
| | | | | |_| |/ _ \ \ /\ / /
| |_| | |  _| | (_) \ V  V / 
 \__,_|_|_| |_|\___/ \_/\_/  

APIKEY: B81F9D52
MicroPython 15314de58-dirty on 2021-12-31; M5Stack with ESP32
Type "help()" for more information.



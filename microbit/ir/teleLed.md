
power:  0x00ff 02fd
avanti: 0x00ff 827d
down:   0x00ff ba45
up:     0x00ff 3ac5

red:    0x00ff 1ae5
green:  0x00ff 9a65
blue:   0x00ff a25d
white:  0x00ff 22dd

da notare che l'ultimo byte è il penultimo complementato.
Per complementare:

>a = b'\x02'
>print('%x' % (~a[0] & 0xff) )
fd

o anche:

> hex(~0x22 & 0xff)
'0xdd'


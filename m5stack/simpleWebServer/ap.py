try:
    import usocket as socket
except:
    import socket
  
import network
import esp
import uos

uname = uos.uname()

ap = network.WLAN(network.STA_IF)
ap.active(True)

ssid = "SSID"
password = "secret"
ap.scan()
ap.connect(ssid, password)
while not ap.isconnected() :
    pass


print('Web Server Active')
print("Visit: " + ap.ifconfig()[0] + ":80")

res_01 = """<html>
    <head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body>
    <h1>Hello, MicroPython@ESP32!</h1>"""
res_02= """
    </body>
    </html>"""

res_something = "sysname: " + uname.sysname + "<br/>"\
    "nodename: " + uname.nodename + "<br/>" +\
    "release: " + uname.release + "<br/>" +\
    "version: " + uname.version + "<br/>" +\
    "machine: " + uname.machine + "<br/>"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    youraddr = str(addr)
    request = conn.recv(1024)

    conn.send(res_01)
    conn.send(res_something)
    conn.send("<br/><br/>")
    conn.send(youraddr)
    conn.send("<br/><br/>")
    conn.send(request)
    conn.send(res_02)
    conn.close()

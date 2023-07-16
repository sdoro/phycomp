
```
apt install mosquitto mosquitto-clients -y
systemctl enable mosquitto.service
systemctl status mosquitto.service
```

In /etc/mosquito/mosquito.conf:
```
[...]
listener 1883
allow_anonymous false
[...]
```

Assume mosquito server has pi4 name:
```
mosquitto_sub -v -h pi4 -t test/message
```

```
mosquitto_pub -t test/message -m "Hello MQTT!"
```


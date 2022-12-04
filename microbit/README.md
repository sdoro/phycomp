


# flashing

Per il flashing delle immagini (ad esempio di OutOfBoxExperience.hex
o di 0255_kl27z_microbit_0x8000.hex) non ho usato il tasto di reset
e quindi la scheda NON è andata in MAINTENANCE.
Ma attenzione che poi da errore 528 che si risolve con il flash del
primo programma.

Il copy (comando cp) sulla cartella MICROBIT automagicamente lancia il reset
della scheda al su termine.


# OutOfBoxExperience

When you first unbox and plug in a brand new micro:bit, it runs a special demonstration program that shows off some of its features in a playful way. We call this the 'out of box experience' program (https://microbit.org/get-started/user-guide/out-of-box-experience/)

# printing

Per vedere le eventuali chiamate a print occorre andare in REPL e dare un CTRL-D
che realizza un soft-reboot e dunque si vedranno.


# Chrome (https://python.microbit.org/v/3)

Per farlo funzionare occorre inserire una regola udev su un nuovo file,
ad esempio /etc/udev/rules.d/50-microbit.rules:

# Create rule
sudo cat << EOF >> /etc/udev/rules.d/50-microbit.rules
SUBSYSTEM=="usb", ATTR{idVendor}=="0d28", MODE="0664", GROUP="dialup"
EOF

# Add current user to plugdev group
sudo usermod -a -G dialup $USER

# Reload udev rules
sudo udevadm control --reload-rules


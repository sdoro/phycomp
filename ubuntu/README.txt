

-- environment Chrome

Alla partenza di Chrome si apre un fastidioso popup dove chiede la password dell'utente
locale per accedere al keyring con il quale proteggere le password (se salvate) dei siti.
É una funzionalità che non ha senso in laboratorio e quindi viene disabilitata.

1. cp /usr/share/applications/google-chrome.desktop ~/.local/share/applications
2. vi ~/.local/share/applications/google-chrome.desktop
3. cerca OGNI riga che inizia per 'Exec' e aggiungi '--password-store=basic' come
   ad esempio:
       Exec=/usr/bin/google-chrome-stable --password-store=basic %U

Fare il clone della home con 'tar czf /tmp/stu.tgz /home/studentestem', copiare il file
su '/root/stu.tgz', copiare il file su un secondo pc e infine verificare il corretto
funzionamento su quest'ultimo pc. Al termine copiare il file '/root/stu.tgz' su tutte
le stazioni.



-- environment udev

Per permettere a Chrome di usare i dispositivi USB con l'API WebUSB tramite javascript
occorre che il dispositivo appartenga allo stesso gruppo a cui appartiene l'utente.
Nei sistemi Ubuntu (e altri) il gruppo si chiama 'dialout'.
A questo scopo si procede così:
1. si associa l'utente al gruppo 'dialout' con: adduser $USER dialout
2. si costruisce la regola che all'inserimento del particolare dispositivo USB
   gli associa il gruppo 'dialout'
3. si riavvia il gestore delle regole in modo che rilegga la configurazione

I dispositivi che per ora utilizzeremo sono i micro:bit e i LEGO Spike e le
due regole e i due commenti sono:

----------------------------------------------------------------------
# micro:bit
SUBSYSTEM=="usb", ATTR{idVendor}=="0d28", MODE="0664", GROUP="dialout"
# LEGO:
SUBSYSTEM=="usb", ATTR{idVendor}=="0694", MODE="0664", GROUP="dialout"
----------------------------------------------------------------------

Le precedenti quattro righe saranno memorizzate in un file di nome 'stem.rules'
e caricato nella directory '/etc/udev/rules.d/'

Prima di inserire il nuovo dispositivo si riavvia il demone:
'udevadm control --reload-rules' o si aspetta il prossimo riavvio.

Per verificare se il dispositivo è stato associato al gruppo corretto,
si può utilizzare il comando 'ls -l /dev/bus/usb/' per vedere la proprietà del device.



-- environment $USER create STEM user

Per i corsi STEM verrà creato un apposito utente di nome 'studentestem' in tutte
le stazioni e sarà aggiunto al gruppo 'dialout':

------------------------------------------------------------------------------------------
# deluser --remove-all-files studentestem
adduser --gecos "Studente STEM" --disabled-password --home /home/studentestem studentestem
echo -e "XXXXXXXX\nXXXXXXXX" | passwd studentestem
adduser studentestem dialout
------------------------------------------------------------------------------------------






-- environment $USER restore previous setting student's home

Nel laboratorio gli utenti accedono alle stazioni locali senza password
ma l'utente selezionato sul login deve essere 'studente STEM'.
Ogni volta si esegue il riavvio della macchina, l'utente in questione
deve essere ripristinato con la rimozione di tutte le tracce dell'attività
eseguita precedentemente dall'utente.

Per questo scopo ad ogni boot la cartella viene totalmente rimossa
e viene ripristinata una cartella predefinita all'inizio del corso.

Il lancio dello script di nome 'stem-scritp.sh' residente nel percorso '/usr/local/bin'
e con permessi di esecuzione a tutti con 'chmod a+rx /usr/local/bin/stem-script.sh'
viene attivato come service costruendo un file di nome 'home-restore.service'
all'interno della cartella '/etc/systemd/system' con il seguente contenuto:

---------------------------------------
[Unit]
Description=home student restore at boot time
After=network.service

[Service]
User=root
ExecStart=/usr/bin/bash /usr/local/bin/stem-script.sh
Type=simple

[Install]
WantedBy=default.target
---------------------------------------

e abilitando il service con 'systemctl enable home-restore.service'


-- environment $USER auto login

Per abilitare l'auto login senza password per l'utente 'studentestem' occorre mettere
come prima riga:

auth sufficient pam_succeed_if.so user ingroup studentestem

nel file di configurazione di lighdm: /etc/pam.d/lightdm
o nel file di configurazione di gdm: /etc/pam.d/gdm-password


### Il data storage di `Docker`

Il data storage di Docker è residente in `/var/lib/docker` e 
può essere di dimensioni di decine di GByte.
Dal suo nome deriva che è residente nella partizione di
sistema e quindi può facilmente essere full.
In questi casi occorre spostare la radice del data store
in una zona (partizione) che abbia più spazio.

Ci sono due metodi (tra molti) che vengono suggeriti:
1. muovere il data storage in un'altra posizione e
cambiare nel file di configurazione di docker
`/etc/default/docker` (in Ubuntu)
2. sostituire con un link simbolico ad una zona più
capiente il data storage.

Vediamo in sequenza le operazioni:


#### fermo il servizio:

	systemctl stop docker.socket

#### sposto lo storage base

	mv /var/lib/docker /home/docker

#### edit file /etc/default/docker e cambio:

	DOCKER_OPTS="-g /home/docker"

#### restart del servizio:

        systemctl start docker.socket

Un altro metodo (con gli stessi accorgimenti di stop) è con un symlink:

	ln -s /home/docker /var/lib/docker

Riferimento da cui abbiamo preso spunto: https://askubuntu.com/questions/631450/change-data-directory-of-docker


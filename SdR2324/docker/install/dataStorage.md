### Il data storage di `Docker`

Il data storage di Docker è residente in `/var/lib/docker` e 
può essere di dimensioni di decine di GByte.
Dal suo nome deriva che è residente nella partizione di
sistema e quindi può facilmente essere full.
In questi casi occorre spostare la radice del data store
in una zona (partizione) che abbia più spazio.

Il metodo che abbiamo usato non modifica il file
di configurazione del servizio e sposta semplicemente
con un link simbolico la radice del data store.

Le operazioni in sequenza:

#### fermo il servizio:

	systemctl stop docker.socket

#### sposto lo storage base

	mv /var/lib/docker /home/docker

#### costruisco un symlink:

	ln -s /home/docker /var/lib/docker

#### restart del servizio:

        systemctl start docker.socket

Riferimento da cui abbiamo preso spunto: https://askubuntu.com/questions/631450/change-data-directory-of-docker


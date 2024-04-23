### Il data storage di `Docker`

Il data storage di Docker è residente in `/var/lib/docker` e 
può essere di dimensioni di decine di GByte.
Dal suo `path` ne consegue che è residente nella partizione di
sistema e quindi può facilmente saturarla.
In questi casi occorre spostare la radice del data store
in una zona (partizione) che abbia più spazio.

Il metodo che abbiamo usato non modifica il file
di configurazione del servizio e sposta semplicemente
con un link simbolico la radice del data store
in un posto abbastanza capiente (ad esempio `/home`).

Le operazioni da fare in sequenza:

#### fermo il servizio:

	sudo systemctl stop docker.socket

#### sposto lo storage base

	sudo mv /var/lib/docker /home/docker

#### costruisco un symlink:

	sudo ln -s /home/docker /var/lib/docker

#### restart del servizio:

	sudo systemctl start docker.socket

Riferimento da cui abbiamo preso spunto:
https://askubuntu.com/questions/631450/change-data-directory-of-docker


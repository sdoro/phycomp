
### install virtualenv

	apt install virtualenv

### create a virtual env: ~/mu-editor

	mkdir ~/mu-editor
	virtualenv ~/mu-editor

### activate virtualenv (~/mu-editor) and install mu editor

	source ~/mu-editor/bin/activate
	pip install -r requirements.txt

### run mu editor

	mu-editor

### deactivate virtual env: ~/mu-editor

	deactivate


### upgrade

	source ~/mu-editor/bin/activate
	# edit requirements.txt as needed
	pip install --upgrade -r requirements.txt


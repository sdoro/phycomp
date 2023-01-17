# adduser (before deluser to erase)
# deluser --remove-all-files studentestem
adduser --gecos "Studente STEM" --disabled-password --home /home/studentestem studentestem
echo -e "XXXXXXXX\nXXXXXXXX" | passwd studentestem
adduser studentestem dialout

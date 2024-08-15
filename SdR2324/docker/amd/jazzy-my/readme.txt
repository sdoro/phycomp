
apt install vim mc less -y


ho provato a installare alcuni pacchetti di Gazebo:

apt install ros-jazzy-ros-gz ros-jazzy-ros-gz-sim 


(ho provato:)
apt install ros-jazzy-ros-gz ros-jazzy-ros-gz-sim  ros-jazzy-gz-common-vendor ros-jazzy-gz-dartsim-vendor ros-jazzy-gz-fuel-tools-vendor ros-jazzy-gz-gui-vendor ros-jazzy-gz-msgs-vendor ros-jazzy-gz-ogre-next-vendor ros-jazzy-gz-physics-vendor ros-jazzy-gz-plugin-vendor ros-jazzy-gz-rendering-vendor ros-jazzy-gz-sensors-vendor ros-jazzy-gz-sim-vendor ros-jazzy-gz-tools-vendor ros-jazzy-gz-transport-vendor ros-jazzy-image-transport-plugins ros-jazzy-ros-gz ros-jazzy-ros-gz-bridge ros-jazzy-ros-gz-image ros-jazzy-ros-gz-interfaces ros-jazzy-ros-gz-sim ros-jazzy-ros-gz-sim-demos




poi serve:

apt install ros-jazzy-controller-manager


nota: usando:
gz sim --verbose
in almeno due casi (NAO e TugboT + empty) funziona lo start di gazebo.
Il file e il pacchetto sono:
# which gz
/opt/ros/jazzy/opt/gz_tools_vendor/bin/gz
# dpkg -S /opt/ros/jazzy/opt/gz_tools_vendor/bin/gz
ros-jazzy-gz-tools-vendor: /opt/ros/jazzy/opt/gz_tools_vendor/bin/gz

per poter partire occorre correggere il path


in un secondo esperimento la correzione del path l'ho realizzata con
dei link simbolici:

cd /home
ln -s /mnt/share/site user
ln -s /mnt/share/site simulations
cd /simulations
ln -s ros2_ws  ros2_sims_ws

ma comunque non funziona



Invece funzionano i some examples in the ign_ros2_control_demos package
installati con il comando:

apt install ros-jazzy-gz-ros2-control-demos

per farli partire si segue:

https://github.com/ros-controls/gz_ros2_control/blob/c21f472743dfd1993c5e8d5952f1109ba248d0df/doc/index.rst#ign_ros2_control_demos

ma attenzione a cambiare, ad esempio, ign_ros2_control_demos in gz_ros2_control_demos in tutte le stringhe.



dopo aver installato:

apt install ros-jazzy-ros2-control

funziona il giorno D3!



source /opt/ros/jazzy/setup.bash

ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=/rosbot_xl_base_controller/cmd_vel

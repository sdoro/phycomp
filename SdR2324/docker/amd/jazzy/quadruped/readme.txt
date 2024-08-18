
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
source ~/.bashrc

YouTube video:
How to Export a 3D Robot Model to ROS2 | Onshape CAD to URDF
https://www.youtube.com/watch?v=TJeCpGnX508

Web page:
https://www.theconstruct.ai/how-to-export-a-3d-robot-model-to-ros2-onshape-cad-to-urdf/

Project:
https://app.theconstructsim.com/l/5ee7cc96/


Codice OnShape identificativo: d78284e6184fe09f36f141e9
https://cad.onshape.com/documents/d78284e6184fe09f36f141e9/

Per le key delle API, dopo il login su onshaper, occorre andare su:

https://dev-portal.onshape.com/

---

apt update
sh /mnt/share/install.sh
apt install -y vim mc less
apt install -y pip
# Install onSHape to Urdf python module
pip install --break-system-packages onshape-to-robot


# Install Dependencies
apt install -y software-properties-common
add-apt-repository ppa:openscad/releases
# change noble in focal (DOVREBBE FUNZIONARE ANCHE SENZA)
vi /etc/apt/sources.list.d/openscad-ubuntu-releases-noble.sources
apt update
apt install -y openscad
apt install -y meshlab


--- urdf ---
apt install -y ros-jazzy-urdf ros-jazzy-urdfdom ros-jazzy-urdfdom-headers ros-jazzy-urdfdom-py ros-jazzy-sdformat-urdf ros-jazzy-urdf-parser-plugin ros-jazzy-urdf-tutorial
--- xacro ---
apt install -y ros-jazzy-xacro ros-jazzy-webots-ros2-importer ros-jazzy-robotiq-description




# Add the OnShapeKeys to the `keys.sh` file
source /mnt/share/keys.sh

mkdir -p /home/user
export HOME=/home/user
cd ~
tar zxf /mnt/share/onshape-to-ros2.tgz
cd ~/ros2_ws/src
rm -rf quadruped_description
ros2 pkg create --build-type ament_cmake quadruped_description --dependencies urdf xacro
cd quadruped_description
mkdir quadruped
touch quadruped/config.json
mkdir launch rviz
# ------------------domanda su id (privato?)
cp /mnt/share/config.json quadruped/config.json
cp /mnt/share/CMakeLists.txt ~/ros2_ws/src/quadruped_description/CMakeLists.txt
# cd ~/ros2_ws/src/quadruped_description
onshape-to-robot quadruped
vi quadruped/robot.urdf    ontop: <?xml version="1.0"?>
# cd ~/ros2_ws/src/quadruped_description
touch launch/quadruped.launch.py
touch launch/start_rviz.launch.py
touch rviz/quadruped.rviz

cp /mnt/share/quadruped.launch.py launch/quadruped.launch.py
cp /mnt/share/start_rviz.launch.py launch/start_rviz.launch.py


cd ~/ros2_ws/
source install/setup.bash
# c'è un errore e quindi aggiungo a mano: "source ./install/local_setup.bash"
colcon build --packages-select quadruped_description
source install/setup.bash

# Launch Generated system
cd ~/ros2_ws/
source install/setup.bash
ros2 launch quadruped_description quadruped.launch.py


export HOME=/home/user
cd ~/ros2_ws/
source install/setup.bash
ros2 launch quadruped_description start_rviz.launch.py



export HOME=/home/user
cd ~/ros2_ws/
source install/setup.bash
ros2 run joint_state_publisher_gui joint_state_publisher_gui


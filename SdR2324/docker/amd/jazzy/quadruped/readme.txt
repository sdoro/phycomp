
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
apt install -y vim mc less
apt install -y pip
pip install --break-system-packages onshape-to-robot

apt install -y software-properties-common
sudo add-apt-repository ppa:openscad/releases

# change noble in focal (DOVREBBE FUNZIONARE ANCHE SENZA)
vi /etc/apt/sources.list.d/openscad-ubuntu-releases-noble.sources
apt update



sudo apt update
sudo apt install -y openscad
sudo apt install -y meshlab


source /mnt/share/keys.sh
sh /mnt/share/install.sh

cd
tar zxf /mnt/share/onshape-to-ros2.tgz
cd ~/ros2_ws/src
rm -rf quadruped_description
ros2 pkg create --build-type ament_cmake quadruped_description --dependencies urdf xacro
cd quadruped_description
mkdir quadruped
touch quadruped/config.json
mkdir launch rviz
cp /mnt/share/config.json quadruped/config.json
cp /mnt/share/CMakeLists.txt ~/ros2_ws/src/quadruped_description/CMakeLists.txt
cd ~/ros2_ws/src/quadruped_description
onshape-to-robot quadruped
vi quadruped/robot.urdf    ontop: <?xml version="1.0"?>
cd ~/ros2_ws/src/quadruped_description
touch launch/quadruped.launch.py
touch launch/start_rviz.launch.py
touch rviz/quadruped.rviz



cd ~/ros2_ws/
source install/setup.bash
ln -s ~ /home/user 




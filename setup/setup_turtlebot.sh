
echo -e "\n\n\n"
echo ==========================================
echo " ROSパッケージインストール "
echo ==========================================
sudo apt -y install ros-kinetic-joy ros-kinetic-teleop-twist-joy ros-kinetic-teleop-twist-keyboard ros-kinetic-laser-proc ros-kinetic-rgbd-launch ros-kinetic-depthimage-to-laserscan ros-kinetic-rosserial-arduino ros-kinetic-rosserial-python ros-kinetic-rosserial-server ros-kinetic-rosserial-client ros-kinetic-rosserial-msgs ros-kinetic-amcl ros-kinetic-map-server ros-kinetic-move-base ros-kinetic-urdf ros-kinetic-xacro ros-kinetic-compressed-image-transport ros-kinetic-rqt-image-view ros-kinetic-gmapping ros-kinetic-navigation ros-kinetic-interactive-markers
sudo apt -y install ros-kinetic-navigation-stage


echo -e "\n\n\n"
echo ==========================================
echo " turtlebot_wsセットアップ "
echo ==========================================
sudo apt -y install git
mkdir -p ~/ros_ws/robot/turtlebot_ws/src
cd ~/ros_ws/robot/turtlebot_ws/src
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
cd ~/ros_ws/robot/turtlebot_ws/ && catkin_make
cd ~/ros_ws/robot/turtlebot_ws/ && catkin_make
cd ~/ros_ws/robot/turtlebot_ws/ && catkin_make



echo -e "\n\n\n"
echo ==========================================
echo " TurtleBot環境設定用bashファイル用意 "
echo ==========================================
rm ~/ros_ws/robot/turtlebot_ws/setting.sh
touch ~/ros_ws/robot/turtlebot_ws/setting.sh
echo 'export ROS_MASTER_URI=http://192.168.0.1:11311' >> ~/ros_ws/robot/turtlebot_ws/setting.sh
echo 'export ROS_HOSTNAME=192.168.0.1' >> ~/ros_ws/robot/turtlebot_ws/setting.sh
echo 'export TURTLEBOT3_MODEL=burger' >> ~/ros_ws/robot/turtlebot_ws/setting.sh
cat ~/ros_ws/robot/turtlebot_ws/setting.sh


echo -e "\n\n\n"
echo ==========================================
echo " 追加セットアップ "
echo ==========================================
sudo apt -y install ros-kinetic-navigation-stage
sudo apt -y install ros-kinetic-teleop-twist-keyboard
sudo apt -y install ros-kinetic-uvc-camera
sudo apt -y install ros-kinetic-image-proc
sudo apt -y install ros-kinetic-opencv-apps

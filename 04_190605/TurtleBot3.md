# TurtleBot3 超簡易マニュアル

## 事前準備
* 右上のネットワークアイコンをクリック→「Enable Wi-Fi」のチェックを外す→「toTurtleBot3」をクリック
* TurtleBotの電源を入れる

## 最初にやってみよう！
### Terminal1
```
$ source ~/ros_ws/upm/turtlebot/setting.sh
$ roscore
```

### Terminal2
```
$ ssh turtlebot@192.168.0.2 または ssh turtlebot302@192.168.0.2 または ssh turtlebot304@192.168.0.2
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

### Terminal3
```
$ source ~/ros_ws/turtlebot/setting.sh
$ rostopic pub cmd_vel geometry_msgs/Twist “linear :
	x : 1.0
	y : 0.0
	z : 0.0
　　angular :
	x : 0.0
	y : 0.0
	z : 0.0”
　＜ Ctrl + C ＞
 $ rostopic pub cmd_vel geometry_msgs/Twist “linear :
	x : 0.0
	y : 0.0
	z : 0.0
　　angular :
	x : 0.0
	y : 0.0
	z : 0.0”
```

## 次にやってみよう！
### Terminal1
```
$ source ~/ros_ws/upm/turtlebot/setting.sh
$ roscore
```

### Terminal2
```
$ ssh turtlebot@192.168.0.2 または ssh turtlebot302@192.168.0.2
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

### Terminal3
```
$ source ~/ros_ws/upm/turtlebot/setting.sh
$ source ~/ros_ws/upm/turtlebot/turtlebot_ws/devel/setup.bash
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
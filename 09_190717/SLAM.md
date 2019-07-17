# TurtleBot3 オンラインSLAM実行マニュアル

## 事前準備
* 右上のネットワークアイコンをクリック→「Enable Wi-Fi」のチェックを外す→「toTurtleBot3」をクリック
* TurtleBotの電源を入れる
* sshでTurtleBotに繋いで時刻同期をする
  * ssh：`$ ssh turtlebot@192.168.0.2 または ssh turtlebot302@192.168.0.2 または ssh turtlebot304@192.168.0.2`
  * 時刻を合わせるコマンド： `$ sudo date -s "2019/7/17 20:44:10"`

## 地図を作ってみよう！
### Terminal1　：roscoreを立てる
```
$ source ~/ros_ws/upm/turtlebot_ws/setting.sh
$ roscore
```

### Terminal2　：TurtleBotのシステムを起動する
```
$ ssh turtlebot@192.168.0.2 または ssh turtlebot302@192.168.0.2 または ssh turtlebot304@192.168.0.2
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

### Terminal3　：SLAMのシステムを立ち上げる
```
$ source ~/ros_ws/upm/turtlebot_ws/setting.sh
$ source ~/ros_ws/upm/turtlebot_ws/devel/setup.bash
$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```

### Terminal4　：テレオペ用のソフトを立ち上げる
```
$ source ~/ros_ws/upm/turtlebot_ws/setting.sh
$ source ~/ros_ws/upm/turtlebot_ws/devel/setup.bash
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

## 地図を保存してみよう！
* 「地図を作成してみよう！」のコマンドを叩き，ロボットを動かして地図を作り終えたら，下記を実行する

### Terminal5　：地図を保存する
```
$ source ~/ros_ws/upm/turtlebot_ws/setting.sh
$ rosrun map_server map_saver -f ~/map
```
# 第8回講習
## テキスト
|内容|資料|URL|
|:-|:-|:-|
|ROSで画像を扱う|テキスト||
||||


|TFについて学ぶ|ROS wiki: tf を用いたロボットのセットアップ ／ Setting up your robot using tf|[日本語](http://wiki.ros.org/ja/navigation/Tutorials/RobotSetup/TF) [English](http://wiki.ros.org/navigation/Tutorials/RobotSetup/TF)|
|TFを静的にパブリッシュしてみる|ROS wiki: tf Package Summary ／ tf Package Summary|[日本語](http://wiki.ros.org/ja/tf#A.2BMMEw5TD8MMgw6jCiMOs-) [English](http://wiki.ros.org/tf#A.2BMMEw5TD8MMgw6jCiMOs-)|
|TFを動的にパブリッシュしてみる|ROS wiki: tfのbroadcasterを書く(Python) ／ Writing a tf broadcaster (Python)|[日本語](http://wiki.ros.org/ja/tf/Tutorials/Writing%20a%20tf%20broadcaster%20%28Python%29) [English](http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20broadcaster%20%28Python%29)|
|TFの座標を確認してみる|ROS wiki: tf listenerを書く (Python) ／ Writing a tf listener (Python)|[日本語](http://wiki.ros.org/ja/tf/Tutorials/Writing%20a%20tf%20listener%20%28Python%29) [English](http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20listener%20%28Python%29)|

## 課題
1. static_tf.launchを作成し，画像のようなTFを静的に発行するコードを書いてください．
2. [tf_listener.py](https://github.com/yuma116/ros_lecture19/blob/master/07_190614/tf_listener.py)をダウンロードし，動作を確認してください．
3. [tf_listener.py](https://github.com/yuma116/ros_lecture19/blob/master/07_190614/tf_listener.py)を改造して，link1フレームから見たときのlink4フレームの座標を求めてください．

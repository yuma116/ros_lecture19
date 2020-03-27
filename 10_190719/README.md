# 第10回講習 オフラインSLAMとナビゲーション
## テキスト
|内容|資料|URL|
|:-|:-|:-|
|SLAMについて学ぶ  |カーロボ資料（SLAM）     ||
|SLAMについて学ぶ  |ROSの活用による屋外の歩行者空間に適応した自律移動ロボットの開発| [English](https://www.slideshare.net/hara-y/ros-slam-navigation-rsj-seminar) |
|SLAMを動かしてみる|TurtleBot e-Manual : SLAM|[English](http://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#run-slam-nodes)|
|ナビゲーションを動かしてみる|TurtleBot3 ナビゲーション実行マニュアル|[日本語](Navigation.md)|

## 課題
1. 第9回で作成した地図を用いて，ナビゲーションシステムを動かしてください．
2. RVIZ上で「2D Pose Estimate」を使用し，ロボットの位置を初期化してください．
3. RVIZ上で「2D Nav Goal」を使用し，ロボットに「ナビゲーションさせて」ください．ロボットが自動でゴール地点へ向かって動き出し，停止したら成功です．[このページ](http://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/#ros-1-navigation)の「10.3. Send Navigation Goal」を参照すること．
4. [Navigation.py](Navigation.py)を使用して，「3.」をプログラムに自動でさせてください．なお，必要があればプログラム中のパラメタを調整してください．



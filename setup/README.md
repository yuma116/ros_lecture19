# 環境セットアップ手順書（HMA外のPC用）

## 前提条件
1. Ubuntu16.04がインストール済みである（Ubuntu16.04をDLできるサイト：[日本語版](https://www.ubuntulinux.jp/News/ubuntu1604-ja-remix) [英語版](http://releases.ubuntu.com/16.04/)）
2. ROS kineticがインストール済みである（[参考サイト](http://wiki.ros.org/kinetic/Installation/Ubuntu)）

## セットアップ方法
1. Terminalを起動する．
2. `$ wget https://github.com/yuma116/ros_lecture19/raw/master/setup/setup_tertlebot.sh`コマンドを実行する
3. `$ bash setup_tertlebot.sh`コマンドを実行する
4. `$ rm setup_tertlebot.sh`コマンドを実行する

## 備考
- インターネットに接続した環境で実行してください．
- 「turtlebot_wsセットアップ」のステップでは，エラーが表示されるかもしれません．エラーが表示されても問題ない構造なので，気にしないでください．
- 上記以外の部分でエラーが出たら，吉元までエラーのコマンドを送ってください．対応します．

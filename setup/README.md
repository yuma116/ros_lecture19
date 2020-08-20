# 環境セットアップ手順書（HMA外のPC用）

## 前提条件
1. Ubuntu16.04がインストール済みである（Ubuntu16.04をDLできるサイト：[日本語版](https://www.ubuntulinux.jp/News/ubuntu1604-ja-remix) [英語版](http://releases.ubuntu.com/16.04/)）
2. ROS kineticがインストール済みである（[参考サイト](http://wiki.ros.org/kinetic/Installation/Ubuntu)）

## セットアップ方法
### 主要ソフトのインストール
1. Terminalを起動する．
2. `$ wget https://github.com/yuma116/ros_lecture19/raw/master/setup/setup_turtlebot.sh`コマンドを実行する
3. `$ bash setup_turtlebot.sh`コマンドを実行する
4. `$ rm setup_turtlebot.sh`コマンドを実行する

### ネットワーク設定の追加 (要：管理者権限)
1. 画面右上のネットワークアイコンをクリック
2. 「Edit Connections...」をクリック
3. 「Network Connections」ウィンドウで「Add」をクリック
4. 次のように設定する

```
Connection name: TurtleBot3
IPv4 Settingタブ
  Method: Manual
  Address
    Address: 192.168.0.1
    Netmask: 24
    Gateway: 255.255.255.0
上記を入力して「Add」ボタンをクリック
その後「Save」をクリック
```

ウィンドウをすべてクローズ



## 備考
- インターネットに接続した環境で実行してください．
- 「turtlebot_wsセットアップ」のステップでは，エラーが表示されるかもしれません．エラーが表示されても問題ない構造なので，気にしないでください．
- 上記以外の部分でエラーが出たら，吉元までエラーのコマンドを送ってください．対応します．

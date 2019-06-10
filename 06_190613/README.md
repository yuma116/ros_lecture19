# 第5回講習

|内容|資料|URL|
|:-|:-|:-|
|C++でActionLibを扱う書き方を学ぶ|ROS wiki： コールバックを用いてシンプルなアクションサーバーを書く ／ Writing a Simple Action Server using the Execute Callback|[日本語版](http://wiki.ros.org/ja/actionlib_tutorials/Tutorials/SimpleActionServer%28ExecuteCallbackMethod%29) [English](http://wiki.ros.org/actionlib_tutorials/Tutorials/SimpleActionServer%28ExecuteCallbackMethod%29)|
|C++でActionLibを扱う書き方を学ぶ|ROS wiki： シンプルなアクションクライアントを書く ／ Writing a Simple Action Client|[日本語](http://wiki.ros.org/ja/actionlib_tutorials/Tutorials/SimpleActionClient) [English](http://wiki.ros.org/actionlib_tutorials/Tutorials/SimpleActionClient)|
|C++でActionLibを扱う書き方を学ぶ|ROS wiki： アクションクライアントとサーバーを実行する ／ Running an Action Client and Server|[日本語](http://wiki.ros.org/ja/actionlib_tutorials/Tutorials/RunningServerAndClient) [English](http://wiki.ros.org/actionlib_tutorials/Tutorials/RunningServerAndClient)|
|PythonでActionLibを扱う書き方を学ぶ|ROS wiki： Pythonでコールバックを用いてシンプルなアクションサーバーを書く ／ Writing a Simple Action Server using the Execute Callback (Python)|[日本語](http://wiki.ros.org/ja/actionlib_tutorials/Tutorials/Writing%20a%20Simple%20Action%20Server%20using%20the%20Execute%20Callback%20%28Python%29) [English](http://wiki.ros.org/actionlib_tutorials/Tutorials/Writing%20a%20Simple%20Action%20Server%20using%20the%20Execute%20Callback%20%28Python%29)|
|PythonでActionLibを扱う書き方を学ぶ|ROS wiki： Pythonでシンプルなアクションクライアントを書く ／ Writing a Simple Action Client (Python)|[日本語](http://wiki.ros.org/ja/actionlib_tutorials/Tutorials/Writing%20a%20Simple%20Action%20Client%20%28Python%29) [English](http://wiki.ros.org/actionlib_tutorials/Tutorials/Writing%20a%20Simple%20Action%20Client%20%28Python%29)|


## 課題
1. C++版，皿を洗うコード（白い本PP.50-51）を用意しました．[simple_action_server.cpp](https://github.com/yuma116/ros_lecture19/blob/master/06_190613/simple_action_server.cpp)と[simple_action_client.cpp](https://github.com/yuma116/ros_lecture19/blob/master/06_190613/simple_action_client.cpp)をlecture_pkg内の適切な場所に配置し，CMakeList.txtを書き換え，ビルドを通して実行してください．なお，本コードは白い本の丸写しであるので，環境の違いからそのままでは動きません．適切に修正してください．
2. 前回のコードは，皿を洗った枚数を数えるものでした．サーバ側のソフト（simple_action_server.py or .cpp）を，「皿を1枚洗う毎に，feedbackで何枚洗ったか返す」ようなコードに変更してください．なお，クライアント側のソフトを修正する必要はありません．完成したら，適切なROSコマンドで結果を確認してください．
3. 「2.」について，もう一方も同様に実施してください．

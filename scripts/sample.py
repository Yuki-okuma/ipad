# -*- coding:utf8 -*-
import time
from roslibpy import Message, Ros, Topic
def main():
    
    # roscoreを実行しているサーバーへ接続
    ros_client = Ros('192.168.11.96', 9090)
    # Publishするtopicを指定
    publisher = Topic(ros_client, '/turtle1/cmd_vel', 'geometry_msgs/Twist')
    def start_sending():
        while True:
            if not ros_client.is_connected:
                break
            
            # 送信するTwistメッセージの内容
            publisher.publish(Message({
                'linear': {
                    'x': -3.0,
                    'y': 0,
                    'z': 0
                },
                'angular': {
                    'x': 0,
                    'y': 0,
                    'z': 1.8
                }
            }))
            time.sleep(0.1)
        publisher.unadvertise()
    # Publish開始
    ros_client.on_ready(start_sending, run_in_thread=True)
    ros_client.run_forever()
if __name__ == '__main__':
    main()
# TASK1 

__Subtask1__: Capture The Message

Since we had subscribe to start here, I first went to source folder of ctm_ws and went to the solution.py file to subscribe to start/here 
I took the subscription code from ROS2 documention :


import rclpy

from rclpy.node import Node

from std_msgs.msg import String

class Subscriber(Node):

    def __init__(self):
        super().__init__('Rathneesh_Solver')
        self.start_here = self.create_subscription(String,'start_here',self.start_here_callback,10)
        self.start_here

    def start_here_callback(self, msg):
        print('The message received from topic /start_here is ' + msg.data)

def main(args=None):

    rclpy.init(args=args)
    
    minimal_subscriber = Subscriber()
    
    rclpy.spin(minimal_subscriber)
    
    minimal_subscriber.destroy_node()
    
    rclpy.shutdown()


if __name__ == '__main__':
    main()

After this , I added the line 'solution=capture_the_msg.solution:main' to the setup.py file![](https://github.com/rathneesh06/abhiyaan-app/blob/main/setup(.py).png)
After this I ran the following commands which gave the following hint ![](https://github.com/rathneesh06/abhiyaan-app/blob/main/task1_subtask1_1.png)
Me being a curious mf searched it up on only to find ![](https://github.com/rathneesh06/abhiyaan-app/blob/main/dadjoke1.png)

Since "you are welcome" is our next hint , I repeat the same process. So I subscirbed to "you are welcome"
I repeated this process!!!
![](ithub.com/rathneesh06/abhiyaan-app/blob/main/dadjoke2.png)
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/dadjoke2_1.png)
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/dadjoke2_2.png)
One more round of searching!!!
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/dadjoke2_3.png)
__Pasta wayyyyyyy!!!!!!!!!!__ 

__After Searching so much, even the search bar is starting to blush__

ALl the answers to the hints I found are :

1. Bison
   
2. Oops
   
3. Rebooted

__After all the intense smashing of the keyboard for almost 20 mins , here is the final termial with the end result!!!__
   ![](https://github.com/rathneesh06/abhiyaan-app/blob/main/enddadjoke.png)

__Here is the end script__
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/task1ss_1.png)
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/task1ss_2.png)

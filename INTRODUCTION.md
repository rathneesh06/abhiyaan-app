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

After this , I added the line 'solution=capture_the_msg.solution:main' to the setup.py file![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q1/setup(.py).png)
After this I ran the following commands which gave the following hint ![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q1/task1_subtask1_1.png)
Me being a curious mf searched it up on only to find ![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q1/dadjoke1.png)

Since "you are welcome" is our next hint , I repeat the same process. So I subscirbed to "you are welcome"
I repeated this process!!!
![](ithub.com/rathneesh06/abhiyaan-app/blob/main/Q1/dadjoke2.png)
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q1/dadjoke2_1.png)
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q1/dadjoke2_2.png)
One more round of searching!!!
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q1/dadjoke2_3.png)
__Pasta wayyyyyyy!!!!!!!!!!__ 

__After Searching so much, even the search bar is starting to blush__

ALl the answers to the hints I found are :

1. Bison
   
2. Oops
   
3. Rebooted

__After all the intense smashing of the keyboard for almost 20 mins , here is the final termial with the end result!!!__
   ![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q1/enddadjoke.png)

__Here is the end script__
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q1/task1ss_1.png)
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q1/task1ss_2.png)


# TASK 3

__Subtask A__:
The three main elements for football  are :

1. Coordination: Every bot has to coordinate with each other bot to play .
    
2. Cooperation : Every robot has to cooperate with each other , for exaample if one fails , the others have to take 
    initiative and fill in the roll of the failed robot 
    
3. Collaboration: The 3 robots have to act complementary to each other
Taxonomy:

Taxonomy in breif describes the Architecture , type of communications , heterogenity
To select the Type of Architecture , we need to consider two possibilties :

 1. One player in the team has the ball: In this case the architecture has to be centralized and decentralized . This is because the other players have to coordinate with the player having the ball if he's gonna pass it or if he is gonna shoot . And analysing the below communication topolgies , this case needs a fully connected network .
     
2. No player in the team has the ball : In this case it is too we need a fully connected network . Since , each player has to coordinate with the other player and simultaneously approach the ball while still maintaining a seperation between each other.

 Type of Communication:

Both implicit and explicit methods of communcation have to be done. For example, if a robot fails , before it does , it has to explicitly (communicate the unobservale stats) communicate.And implicit communication  involves communicating the observable states. 

There is no heterogeneity as all the bots are the same.  

![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q2/task3_subtaskA.png)
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q2/subtaska_task3.png)

One more major factor in football is the Formation Control:

![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q2/formation%20control.png)
 
Considering all these factors into consideration we finally conclude the following :

Case 1: 

In the case below , the system wokrs in a leader referenced formation control. Where the player nearest to the ball is the leader. And relative to him , other two players allot their position . Two players communicate with the player nearest to the ball,hence, dynamically allocate their positions.This follows a Star Tropology network with a centralized architecture here as the player closest to the ball has to give commands to the other two players on where to go. .Dotted lines show future path.
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q2/case1_1.jpeg)

Case 2:

In the case below , the next position of the player with the ball is a straight line path to the goal post (disconsidering any opponents in front) .The system wokrs in a leader referenced formation control. Where the player with the ball acts as the leader. And relative to thim , other two players allot their position . The way the other two player allocate thier positions is  in such a way that it will become easier for player with the ball to pass the ball and move towards the goal post. The two players coordinate with each other and have to allocate the best position for the other player to pass the ball. This follows a Star Trpology network with a centralized architecture here as the player with the ball has to give commands to the other two players on where to go.Dotted lines show future path.
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q2/case2_3.jpeg)

Case 3:

In the case below , the player nearest to the opponent with the ball , has to start approaching the opponent to steal/defend .The other two players have to position themselves in such a way that if the opponent with the ball tries passing it to any of his teammates , we should be able to steal the ball.Dotted lines represent their future paths
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q2/case3.jpeg)



 __Subtask B__:
 
 [here](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q2/task3_subtask_b.mov) is the simulation
 
 [here](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q2/task3_subtaskb.py) is the code

# TASK 4

__Let us crack the pixelated mystaery__

Firstly I have found the zooming velocity accelerations , path of the blue ball in [here](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q4/task4_vid_1.py)

[Here](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q4/task4_sr.mov) is the video 

__Video containing multiple balls__:
My ideation: The when the balls are together (not seperate) the code is not able to identiify the contours as seperate. So i have broken down the video into parts where the balls are actually seperate . But I was only able to find three long enough videos among all clips where all the balls actually seperate.
The three videos are:
[1.](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q4/check.mp4)
[2.](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q4/final.mp4)
[3.](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q4/god.mp4)
My idea was to find the velocties and accelerations of these 3 videos and then extrapolate that. But It was not possible because at every frame , the acceleration and velocity are changing and I couldnt come up with a method of doing the extraplation. 
[Here](https://github.com/rathneesh06/abhiyaan-app/blob/main/Q4/task4_2_1.py) is the code

One more idea that came to my mind was to consider the velocties and acceleration of the two balls who are together to be the same . I wanted to try this out too but my video editing software couldnt crop the video as the time of each clip is very less :( :(


# TASK 5

THe model that i have used for semantic segmentation is U-Net . It involved two  major parts . First part is the encoder and the next part is decoder .  The dowsamling part contains mupltiple layers of Double convolution and max pooling .The upsampling part contains multiple conv transpose layers .  During the downsampling , we successfully extract out the features in the image and we upsample to get back the resolution of the image . Skip connections are also used in in unet . By introducing skip connections in the encoder-decoded architecture, fine-grained details can be recovered in the prediction 

This is the code for my model (https://colab.research.google.com/drive/1LAwXmjEeL_imS46asyMVAOvb0CYzVTZq?usp=sharing)



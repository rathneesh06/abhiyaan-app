__Name__:
P.S.Rathneesh 

__Roll No__:
ME23B055

__Previous Experience__:
Took part in paid workshops of robotics in school 

__Made a small robot in school which worked with a controller__

__AI Club Deputy Coordinator__:

         Learnt Python Basics for ML
 
         Worked on  Different regression , classificaton models , the math behind them and the codes
        
        Ensembling methods and SVMs
        
        Participated in an AI club internal hackathon and came 5th.
        
        Worked on Neural Networks , their math and implementations ,KNN.
        
        Worked on CNNs
        
__AI Club Mini project__:

        CNNs
        
        Unet Architechture
        
        GANs-went through a research paper
        
__Current PoRs__:

None

__Why I want to be a part of Team Abhiyaan__:

My first experience of a robot was when I was in school and we had a paid workshop on making a robot . We were given a ready made code and we were made to fix the Rdiuno ,wires,wheels,mmotors, through out the workshop the one thing which made me think and question the robot's functioning was how the code worked ? ANd , how the were signals being transferred through the wires and how was it functioning. This happened in multple workshops until I had bought the whole set up once on my own and tried everything on my own . I was successful in making a small remote control robot . Then came covid the most painful time of my life during which I could explore nothing , but then came a subject in my school called AI . Every class of it seemed very interesting and even tho I had only learnt very basic theory , that was enough to kick in the passion of AI in me . Then after 2 years of hard jee prep and joining IITM ,I was exposed to more AI . I saw all the projects around and it was very fascinating. This lead me to apply for the position of DC in the AI Club. That  was when I explored and learnt about ML MODELS ,  Neural neetworks ,CNN. But one thing that caught my mind immediately was Computer Vision . I searched up online on what ot was and it really made me interested in it, this lead to me picking my mini project under the subtopic of Computer Vision . I had learnt the theory behind CNN and Unet and read the releavent codes related to Unet , which basically does semantic segmentation , and i loved every part of it . As time passed on I got to know what Abhiyaan is as a team and the work that they do . So , after i've thought of all the events that took place till now , the childhood robots that i made and the AI that i discovered , i have realised that  Abhiyaan is the only thing that has all that i am interested in and it involves everything i've liked till now . Also , I have interacted with few seniors who are in abhiyaan well before i knew that abhiyaan existed and i have gotten a very positive and a good vibe from them and it will be a great experience for me to learn and improve my skills among all the learned and skilled people in the team . 

__Relevant Courses__:

Institute

__CS1100__ - Passed

Online

CNN course from youtube 

Not a course , but have worked on Unet in AI Club

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
__ After Searching so much, even the search bar is starting to blush__
ALl the answers to the hints I found are :

1. Bison
   
2. Oops
   
3. Rebooted
   ![]()


  __Subtask2__: Turtle ping-pong
Firstly after downloading turtlesim , i ran the command:
ros2 run turtlesim turtlesim_node

Then I ran the command: ros2 run turtlesim turtle_teleop_key
Through this I was able to control the turtle

After using th rqt command to spawn the second turtle 
 I used the following command on another terminal  :ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=turtle_2/cmd_vel
This enabled me to control the second spawned turtle 

Here's a bit of loaf!!

![Bit of loaf!](https://github.com/rathneesh06/abhiyaan-app/blob/main/task1_subtask_2_turtlesim.png)


Even though i was successful enough in doing so , I could not figure out how to run the ping - pong game . 
What I understood from the video given was that ,
the first turtle is given a specific direction and constant speed .
Whereas the other turtle is controlled by us . I could’nt majorly figure out , what commands to give in order for:
A single turtle attaining and maintaining a constant speed.

Simultaneously we are controlling the second turtle 

After one turtle encounters the other turtle , the first turtle changes direction . 

SInce I could’nt figure out how to do that on turtlesim , I wrote a python script which does the same thing . 

[Task 1 Subtask 2 code](https://github.com/rathneesh06/abhiyaan-app/blob/main/task_1_subtask_2.py)

[Here](https://github.com/rathneesh06/abhiyaan-app/blob/main/task1_subtask2_sim.mov) is the running code


# TASK 3

__Subtask A__:
The three main elements for football  are :

1. Coordination: Every bot has to coordinate with each other to play
    
2. Cooperation : Every robot has to cooperate with each other , for exaample if one fails , the others have to take 
    initiative and fill in the roll of the failed robot 
    
3. Collaboration: The 3 robots have to act complementary to each other
Taxonomy:

Taxonomy in breif describes the Architecture , type of communications , heterogenity
To select the Type of Architecture , we need to consider two possibilties :

 1. One player in the team has the ball: In this case the architecture has to be centralized and decentralized . This is because the other players have to coordinate with the player having the ball if he's gonna pass it or if he is gonna shoot . And analysing the below comunication topolgies , this case needs a fully connected network .
     
2. No player in the team has the ball : In this case it is too we need a fully connected network . Since , each player has to coordinate with the other player and simultaneously approach the ball while still maintaining a seperation beyween each other.

 Type of Communication:

Both implicit and explicit methods of communcation have to be done. For example, if a robot fails , before it does , it has to explicitly (communicate the unobservale stats) communicate.And implicit communication  involves communicating the observable states. 

There is no heterogeneity as all the bots are the same.  

![](https://github.com/rathneesh06/abhiyaan-app/blob/main/task3_subtaskA.png)
![](https://github.com/rathneesh06/abhiyaan-app/blob/main/subtaska_task3.png)

One more major factor in football is the Formation Control:

1. If one player has the ball , then the formation scheme will be a mixture of leader referenced and neighbor refernced . This is because , all the other 2 players need to follow and coordinate wiith the player having the ball while also coordinating with the neighbors to maintain a particualr seperation.
    
2. If no one player of the team has the ball , the scheme will be a mixture of Unit-centered and neighbor referenced. This is because the players need to allocate their positions based on the balls position which is the centre in this case and at the same time , ccoordinte nd maintain the seperation with the neighbor .  

![](https://github.com/rathneesh06/abhiyaan-app/blob/main/formation%20control.png)

One major thing we have'nt considered till now is the opponents.
If one player has the ball:

 The opponents have to be considered at obstacles and the robot has to cross/dodge the opponent or pass it to a neighbor which is closest to us and at the same time who is farthest away from an opponent. 

If no player in the team has the ball:

 The teams approach should be a mixture of Unit-centered and Neighbor referenced scheme of formation control. 


 __Subtask B__:
 

# TASK 4 

__Let us crack the pixelated mystaery__

Firsstly I have found the zooming velocity accelerations , path of the blue ball in [here](https://github.com/rathneesh06/abhiyaan-app/blob/main/task4_vid_1.py)







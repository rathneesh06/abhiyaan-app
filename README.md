Name:
P.S.Rathneesh 

Roll No:
ME23B055

Previous Experience:
Took part in paid workshops of robotics in school 

Made a small robot in school which worked with a controller

AI Club Deputy Coordinator:

         Learnt Python Basics for ML
 
         Worked on  Different regression , classificaton models , the math behind them and the codes
        
        Ensembling methods and SVMs
        
        Participated in an AI club internal hackathon and came 5th.
        
        Worked on Neural Networks , their math and implementations ,KNN.
        
        Worked on CNNs
        
AI Club Mini project:

        CNNs
        
        Unet Architechture
        
        GANs-went through a research paper
        
Current PoRs:

None

Why I want to be a part of Team Abhiyaan:

My first experience of a robot was when I was in school and we had a paid workshop on making a robot . We were given a ready made code and we were made to fix the Rdiuno ,wires,wheels,mmotors, through out the workshop the one thing which made me think and question the robot's functioning was how the code worked ? ANd , how the were signals being transferred through the wires and how was it functioning. This happened in multple workshops until I had bought the whole set up once on my own and tried everything on my own . I was successful in making a small remote control robot . Then came covid the most painful time of my life during which I could explore nothing , but then came a subject in my school called AI . Every class of it seemed very interesting and even tho I had only learnt very basic theory , that was enough to kick in the passion of AI in me . Then after 2 years of hard jee prep and joining IITM ,I was exposed to more AI . I saw all the projects around and it was very fascinating. This lead me to apply for the position of DC in the AI Club. That  was when I explored and learnt about ML MODELS ,  Neural neetworks ,CNN. But one thing that caught my mind immediately was Computer Vision . I searched up online on what ot was and it really made me interested in it, this lead to me picking my mini project under the subtopic of Computer Vision . I had learnt the theory behind CNN and Unet and read the releavent codes related to Unet , which basically does semantic segmentation , and i loved every part of it . As time passed on I got to know what Abhiyaan is as a team and the work that they do . So , after i've thought of all the events that took place till now , the childhood robots that i made and the AI that i discovered , i have realised that  Abhiyaan is the only thing that has all that i am interested in and it involves everything i've liked till now . Also , I have interacted with few seniors who are in abhiyaan well before i knew that abhiyaan existed and i have gotten a very positive and a good vibe from them and it will be a great experience for me to learn and improve my skills among all the learned and skilled people in the team . 

Relevant Courses:

Institute

CS1100 - Passed

Online

CNN course from youtube 

Not a course , but have worked on Unet in AI Club

Task 1:

Subtask2: Turtle ping-pong
Firstly after downloading turtlesim , i ran the command:
ros2 run turtlesim turtlesim_node

Then I ran the command: ros2 run turtlesim turtle_teleop_key
Through this I was able to control the turtle

After using th rqt command to spawn the second turtle 
 I used the following command on another terminal  :ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=turtle_2/cmd_vel
This enabled me to control the second spawned turtle 

![Bit of loaf!](https://github.com/rathneesh06/abhiyaan-app/blob/main/task1_subtask_2_turtlesim.png)


Even though i was successful enough in doing so , I could not figure out how to run the ping - pong game . 
What I understood from the video given was that , the first turtle is given a specific direction and constant speed . Whereas the other turtle is controlled by us . I could’nt majorly figure out , what commands to give in order for:
A single turtle attaining and maintaining a constant speed.
Simultaneously we are controlling the second turtle 
After one turtle encounters the other turtle , the first turtle changes direction .   
SInce I could’nt figure out how to do that on turtlesim , I wrote a python script which does the same thing . 

[Task 1 Subtask 2 code](https://github.com/rathneesh06/abhiyaan-app/blob/main/task_1_subtask_2.py)

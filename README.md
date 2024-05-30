## Motor_control


### Description & Code Snippets

  * The goal of the assignment was to control motor with the speeding button. 
  * I accomplish to my goal by using goal and ask firend for help and using my idea also I take a step by step top accomplish to my goial.
  * motors can draw a lot more juice (current) than LEDs.  In fact, they draw so much current, we don't want to power them directly from the Arduino.  That might fry the Arduino.  So, we will power our motor directly from a 6 V battery pack.




```
    import time
    import board
    import pwmio
    from analogio import AnalogIn
    from digitalio import DigitalInOut, Direction, Pull

    motor = pwmio.PWMOut(board.D9, frequency=50)




   pot = AnalogIn(board.A1)



while True:
     print(pot.value)
     time.sleep(0.1)
     motor.duty_cycle=pot.value
```
  
### Evidence

  
   * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/5d562fad-3a4a-4833-9f7a-eaea2fdb499e)





### Wiring

   * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/f6ea0824-a370-4ba4-8cf4-1b1a726c3167)





### Reflection


  * It is very helpful to using something like Motor because it can go forward and backward when I was use the Motor it was fun for me because it is going forward and backward but it is more when you are using the Motor on your projects. whenever I have projcet I use motor control or tt motor. However the motor control is something to use in your project. It was little hard to find the wiring but the code was easy to find for motor control it was very short code for motor control.





____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Practice Design from Drawings: The Hanger




### Description 

   * The purpose of this assignment is to build or design the Hanger and practice with onshape and getting using to onshape and you have match the mass from your design to the assingment mass.
   * Create this part in Onshape.


### Evidence

  * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/508a6c6d-a3ff-46ce-995b-408123b356a4)
  * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/da543c39-ca4e-47ab-975c-9d1b6e2f0cbe)
  * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/7ea1309a-fd1d-49ad-a757-514dc12dc578)



### Part Link 

   * https://cvilleschools.onshape.com/documents/7a3762d556f61fc3dc62d882/w/b3b7689a296f9a2abbe75745/e/0e37ce298fa604f1b41dd69f?renderMode=0&uiState=652575a29e55ae7675793fa3



### Reflection


  * The Hanger was easy to build and design it was fun to because I whited too long for this type of assinmnets. It is very fun to get use to onshape and design something nice. In this assignment thanks to the teacher because the teacher help us with some of the details to make this assingment easily for us. In this assignment you can help with friend and classmade.




____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Onshape Certification Prep: The Swing Arm




### Description

   * The purpose of this assignment is to build or design the swing arm and practice with onshape and getting using to onshape and you have match the mass from your design to the assingment mass. the swomg arm should be done with the right mass and design.
   * Create this part in Onshape.



### Evidence

   * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/7054272b-738a-440e-9c22-1e16bc67199a)\
   * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/e097f2b5-f6b8-4066-a616-f3c2741158af)
   * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/3fc97015-61f3-40cb-aafc-8f0594b3edaa)




### Part Link 

   * https://cvilleschools.onshape.com/documents/a498ce7f3ced3445f05b924e/w/a171c8d9b7a63e24ff2b5968/e/b90332f0cfd616d71bed4f90?configuration=List_BTYWYw502p6AGK%3DDefault&renderMode=0&uiState=652568262b7a2b2847eefe72


### Reflection



 * This is assignment  I have to work on the  Designing Swing Arm I work on it for 3 hours to do it. To make everything I use a lot of new tools because it makeing easy for me and  i don't have to use line tool there are other tool that make mach easy  and yeah this is everything i did in this assignment just make the Designing the swing arm. This assignment was kind of easily for me to do because my first reason is that you just copy and it show you what to do. My next reason is that you don't have build same thing for different size you can just use the configurations tool to help you with it. In this assignment it will be very easily if you use the tool call configurations it is very helpful. It can help you with a lot different things. For example, it helps you with different size and different colors.


____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
## Photointerrupters


### Description & Code Snippets

  * The goal of the assignment was to use the Photointerrupters. 
  * I accomplish to my goal by using my ideas and ask firend for help and using my friend idea also I take a step by step top accomplish to my goial.
  * Photointerrupters Wire up a circuit that will turn on when something is in between the legs of the photointerrupter.

```

  * from digitalio import DigitalInOut, Direction, Pull
import time
import board

interrupter = DigitalInOut(board.D7)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

counter = 0

photo = False
state = False

max = 1
start = time.time()

while True:
    photo = interrupter.value
    if photo and not state:
            counter += 1
    state = photo

    remaining = max - time.time()

    if remaining <= 0:
        print("Interrupts:", str(counter))
        max = time.time() + 1
        counter = 0

```
 
### Evidence




https://github.com/IANDORA87/engineer3/assets/143534987/2e41991f-bfab-4699-8bdd-c615dfe43a61







### Wiring


  * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/a7029ac8-77a8-4157-ad6c-509af27e89be)
  * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/963a9b84-47e7-4da9-94eb-015809329444)



### Reflection

  * This assignment is not easy and not hard because when I start this assignment it take me a lot of time because of coding  so the thing was that my coding was right but the Photo-interrupters was not working and I pet so many different coding but the thing was that my coding was not working I ask for help from  teacher and the teacher tell me that my Photo Interrupters was not working.




____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## CircuitPython Servo
 


### Description & Code Snippets

  * Get a 180° micro servo to slowly sweep back and forth between 0 and 180°. Spicy part: Now control the servo with 2 buttons. The servo only moves if you are pushing a button.


```

  * import time
import board
from digitalio import DigitalInOut, Direction, Pull

btn1 = DigitalInOut(board.D9)
btn1.direction = Direction.INPUT
btn1.pull = Pull.DOWN

btn2 = DigitalInOut(board.D10)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN

while True:
    if  btn1.value:
        print("BTN1 is pressed")

    if  btn2.value:
        print("BTN2 is pressed")
       

    time.sleep(0.1) # sleep for debounce

   ```
 
### Evidence
    

 * https://github.com/IANDORA87/engineer3/assets/143534987/f64bdfcf-f195-4a30-8554-ea14470a2cd4



### Wiring


  * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/5c4af0d8-5d09-405a-83b1-e99f6da88e4a)



### Reflection

 

  * I learn that how to do the code for this assingment. It take me 2 day because of the coding and I didn't do coding for long now this was the frist assingment for this year.I work on my code for 2 day. I found that my 1 wire was on pule than I fix my wire and I did my coding and other things as will. One things that I used help a lot of time from Mr. David.



____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
### CircuitPython Distance Sensor
 


### Description & Code Snippets

  * I've broken the assignment into 3 stages, to make your life easier:

  * Use the HC-SR04 to measure the distance to an object and print that out to your serial monitor or LCD in cm.
    Next, you will get the neopixel to turn red when your object is less than 5cm, and green when its 35cm.  Ignore the blue and 20cm for now, let's just keep it simple.
    For your final version of this code, you'll smoothly shift the color of the onboard neopixel, corresponding to the distance, according to the graphic below.
    (Neopixel should stay red when below 5cm and green when above 35cm)


```
     * import time
     import board

     import adafruit_hcsr04

     sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)


while True:
      try:
           print((sonar.distance,))
    except RuntimeError:
           print("Retrying!")
        pass
    time.sleep(0.1)
       

    time.sleep(0.1) # sleep for debounce ****
```
 
### Evidence

 

 * https://github.com/IANDORA87/engineer3/assets/143534987/f2597999-57a9-4170-a937-4a6be8cfaa36



### Wiring

 * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/21dbde8e-a2a1-4571-a597-396530ac50ab)




### Reflection


 * This was an assignment that I did in engineer 2 and I did once again. However, I want to make something fun and work on something in my class time in engineer so I work on this in my class time. This year the code was much different.



____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Multi-Part Design Studios - Practice



### Description 

   * The purpose of this assignment is to build or design the Multi and practice with onshape and getting using to onshape and you have match the mass from your design to the assingment mass.
   * Create this part in Onshape.
   * Make a copy of this document.Links to an external site. Rename the and replace COpy with your name. Create all of the parts needed for the assembly.  The cylinder is given as a starting point. Answer the 4 questions below.  There is a question         about the initial assembly and then one for each of the three revisions to the product. You should be able to complete this assignment in 1 hour.


### Evidence

   ![Screenshot 2023-11-02 2 23 25 PM](https://github.com/IANDORA87/engineer3/assets/143534987/683f07dd-0b24-402b-953e-2895de20650a)
   ![Screenshot 2023-11-02 2 24 27 PM](https://github.com/IANDORA87/engineer3/assets/143534987/83d13280-dd4c-4f96-809d-a6844ff1a7e2)
   ![Screenshot 2023-11-02 2 25 16 PM](https://github.com/IANDORA87/engineer3/assets/143534987/af257b65-8056-4631-a85e-e7d534e59df4)

    



 
### Part Link 

[https://cvilleschools.onshape.com/documents/c0b0d21d9816f0cc3227ca95/w/4d1053f94fb2b740f1917346/e/dc1d462e49ce69e18c07431f?renderMode=0&uiState=6543e9c8c034e00cd6034d28
](https://cvilleschools.onshape.com/documents/c0b0d21d9816f0cc3227ca95/w/4d1053f94fb2b740f1917346/e/dc1d462e49ce69e18c07431f?renderMode=0&uiState=6543e9c8c034e00cd6034d28)

### Reflection


  * The Multi was easy and hard to build or design it but it was also fun too because I whited too long for this type of assinmnets. It is very fun to get use to onshape and design something good and using new tools. In this assignment thanks to the teacher because the teacher help us with some of the details to make this assingment easily for us. In this assignment you can help with friend and classmade. 


__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Onshape Certification Prep - Single Part



### Description 

   *OPEN THIS DOCUMENT: CLICK HERELinks to an external site.

    Follow the instructions for each question. Refer to the Certified Onshape Associate Practice Exam if needed.Download Refer to the Certified Onshape Associate Practice Exam if needed.

    Record the mass from the following options detailed in the instructions. 

    Enter the masses into this quiz.
 

### Evidence

  
   * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/914c5275-341d-4440-b741-122cc5d9d3e2)
   * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/53ab13db-6c13-4dd0-a5a3-96c16a9f297c)
   * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/f2538623-1fe2-4e20-a86e-0a2bd63b83f5)




 
### Part Link 

   * https://cvilleschools.onshape.com/documents/106a883062ba2d5ee06b2ea0/w/c3d20bc00dd398fb26426412/e/5765b5a06809f5c5e3e749fa?renderMode=0&uiState=6543bc139e69cb3f67d21e1f
  

### Reflection

   * This is the Onshape Certification Prep - Single Part in this assignment we have to build and then  we have to see if the mass is the same what they told us in assingment. However in this assingment it takes me more hours to finish everything but using  onshape is very fun for me more than coding. Coding is kind of hard for me because I have to write but in onshape  it is vary easy because you just have to look at the drawing and just draw it on onshape is kind like art class you just have to draw on onshape.


__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


##  Onshape CAD Challenge: Alignment Plate


### Description 

 The Onshape CAD Challenges are a great way to practice for the Onshape Certification Exam. These challenges record the time you spent designing your Onshape document and allow you to compare your results with the average amount of time spent. It also checks your work automatically when you record the mass of a part. 


### Evidence

  
 * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/7fecc7b0-47dc-4263-918d-1955bf799fed)
 * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/70764eb7-f120-46a2-8095-ee33b0889633)
 * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/41f28d14-b765-405b-b3d7-71d3ae3b4253)



 

 
### Part Link 

(https://cvilleschools.onshape.com/documents/39271a25eca3ea6bfb86461b/w/f584e9172593ab46c305ede7/e/e3cdbba71d3b4d7f9e6d0d9b?renderMode=0&uiState=654d083369578f18e2823aca)    
  

### Reflection

 In this assignment I learn something new something I didn't know before. It was very eassy and fun I enjoy working on this assignmet. It helped me to get use to Onshape and  how to Submit something in Onshape or how to start assingment in Onshape.
__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

##  Onshape Certification Prep 2: Multi-Part


### Description 

OPEN THIS DOCUMENT: CLICK HERELinks to an external site.

Follow the instructions for each question. Refer to the Certified Onshape Associate Practice Exam if needed.Download Refer to the Certified Onshape Associate Practice Exam if needed.

Record the mass from the following options detailed in the instructions.

Enter the masses into this quiz. 

 

### Evidence

  
![image](https://github.com/IANDORA87/engineer3/assets/143534987/093fb1e9-ccb5-4fe0-9d1a-1ec1c0c5e6b7)
![image](https://github.com/IANDORA87/engineer3/assets/143534987/1975dfbe-f1cd-4e37-ac28-5b88527a4a6c)
![image](https://github.com/IANDORA87/engineer3/assets/143534987/903ccdbb-5249-4cd9-ba6d-73e37fe929f2)
![image](https://github.com/IANDORA87/engineer3/assets/143534987/24e77464-0c93-4192-8a6b-7fd439eb7d18)

 
### Part Link 

  https://cvilleschools.onshape.com/documents/d1af293027a195be63d0ab1b/w/4a159a7d0ac7df8a525a8f1b/e/e667394a888e90dd3414fc7b?renderMode=0&uiState=654d0a94b9fc7e7f814686b0
  



### Reflection

This assignment was very straightforward but I still learned a lot.  I learned how to use the Onshape tools which is a great way to see what is happening to my degin.  I also learned about using how to submit in Onshape. This is going to be a challenging class but I know if I put in the effort and ask for help when needed, I will succeed.



__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
## Onshape Certification Prep - Assemblies 


### Description 

OPEN THIS DOCUMENT: CLICK HERELinks to an external site.

Follow the instructions for each question. Refer to the Certified Onshape Associate Practice Exam if needed.Download Refer to the Certified Onshape Associate Practice Exam if needed.

Record the answer from the following options detailed in the instructions.

Enter the answer into this quiz. 

### Evidence


 
>![image](https://github.com/IANDORA87/engineer3/assets/143534987/5f3c3d81-1a87-4fe4-8187-8aa9c122336e)
 >![image](https://github.com/IANDORA87/engineer3/assets/143534987/1548c966-5cbf-4f4d-8db8-6fc8cbff92bb)


 
### Part Link 

  
https://cvilleschools.onshape.com/documents/673a5044c29999b47cfc0d74/w/0043391907221b6fbc70a543/e/394ab18a008fadafc11ef8eb?renderMode=0&uiState=655ceda663a1b95144112756



### Reflection

The  Certification Prep - Assemblies was kind of hard for me to put it togther. But I had fun time working on it and enjoy that how hard was it. it was more challenging and more hard for me but I did. And speend my time on it.



____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
## Robot Gripper Design


### Description 


Your assignment is to design a basic gripper for a robot arm. There are three major requirements. 
Requirements:
    The gripper must close using only one actuator (one servo, one solenoid, one motor, etc)
    The jaws of the gripper must be able to fully close.
    All parts of the gripper must be able to be 3D printed, laser cut, or already exist in the engineering lab
    The gripper must be fully assembled in Onshape with all fasteners, and the assembly must be able to be animated
 

### Evidence


![image](https://github.com/IANDORA87/engineer3/assets/143534987/4af3fb10-ae10-49c9-aea1-170cc0a57cc5)
![image](https://github.com/IANDORA87/engineer3/assets/143534987/58e00f18-6a01-4ad8-9622-594ccae8383c)
![image](https://github.com/IANDORA87/engineer3/assets/143534987/d6085bac-1b2e-45b3-afef-bbe44588d3b4)




 
### Part Link 

  
https://cvilleschools.onshape.com/documents/aa200ee93079dd2ac45327f4/w/58a6ca5dee946519e97edf08/e/9486c7c624c1fd36ecb3eedb?renderMode=0&uiState=65d7762a2eba134f453bc4d2


### Reflection

This Robot Gripper Design was easy and fun. The design is robot arm that can be use for many things and help human to pick up things and make human work easyer robot can Control the position of the gripper finger. I like it but it will be helpful to make whole robot prject and design it and definitely codeing.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

### Rotary Encoder & LCD


### Description & Code Snippets

You assignment is to use a rotary encoder, an LCD, and the on-board NeoPixel LED to create a menu-based traffic light control.
Steps:
Create a list of strings for stop, caution, go. 
Read the rotary encoder to cycle through the menu items and display them on the LCD.
Make the on-board LED turn red, yellow, or green when the rotary encoder is pressed down on the corresponding menu item.



### Evidence


### Wiring


![image](https://github.com/IANDORA87/engineer3/assets/143534987/c74fafe8-ad1b-44f2-b725-a7565e8e2447)



### Reflection
At this assignment I will say that I am not that good at code and I am very slow at code however I did change to this assignment and stop working at stepper motor assignment but I am not done with codeing.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

### Stepper Motors & Limit Switches
 

### Description & Code Snippets

You assignment is to use a stepper motor to turn on a limit switch. 
Steps:
Get the stepper motor to move its arm in one direction to turn on the limit switch.
When the limit switch is ON, the motor arm will move back in the opposite direction. 
This should be looped continuously. 




### Evidence


### Wiring


![image](https://github.com/IANDORA87/engineer3/assets/143534987/f8e5d5cd-b001-4197-861f-610486fa2ea7)
![image](https://github.com/IANDORA87/engineer3/assets/143534987/285123ce-3378-4927-951d-69a287f29799)
![image](https://github.com/IANDORA87/engineer3/assets/143534987/05d551f8-152d-4e7b-b84e-362870ead50e)
![image](https://github.com/IANDORA87/engineer3/assets/143534987/2e103568-07c2-4d99-8250-80fa00c6d0ae)


### Reflection
At this assignment I will say that I am not that good at code and I am very slow at code however I try my best on this assignment and put a lot of time in this assignment yes I dont have Eviedence becuase I start this assignment than change to other one and forget to take a photo.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

### IR Sensors 


### Description & Code Snippets
You assignment is to use an IR sensor to change the color of your board’s NeoPixel LED. 
Steps:
Wire up your IR sensor and have your program keep track of whether it is HIGH (something is nearby) or LOW (nothing is near it). 
When an object or your hand is nearby, your board’s NeoPixel will turn RED.
When nothing is nearby, your board’s NeoPixel will turn GREEN.




### Evidence


### Wiring


![image](https://github.com/IANDORA87/engineer3/assets/143534987/59e630b2-0640-4789-a10f-93f78fc7f82a)


### Reflection

At this assignment I will say that I am not that good at code and I am very slow at code however I try my best on this assignment and put a lot of time in this assignment yes I dont have Eviedence becuase I didnt start this assignment and had the feel of giveing up because my code website was not working no one help.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Robot Arm Planning

## Design Goal

The goal of our robot arm is to be able to pick up an object and place it in a diffrent location based on the person controlling it. We plan to make our robot arm open and close with a screw like sytem powered by dc motors and double A batteries. We plan to 3D print our robot arm and make the wiring out of the materials provided by the engineering lab, which include 3 DC motors, male jumper cabels, Ardiuno, breadboard, other wiring related objects and 3d printed part's. The design is relativily simple with the main motion of the arm opening and closing and going up and down working on the screw sytem, and the arm moving right to left on a pully sytem connected to a frame. The code will make it so we have buttons that will control open close, up down, and side to side. Our goal is to make it work like a arcade claw machine but with buttons.


## Scope

Step 1 - TOP DOWN DESIGN METHOD
• All of the Parts are modeled in the same
Part Studio
• Geometric and dimensional data is shared
between parts
• Design intent is consistent across multiple
parts
• Multiple parts can be edited at the same
time

Step 2 - Create the Sketch of the Base

Step 3 - Create the Sketch of the Gripper
Extrude the Base and the Gripper
Create Actuator Hole in the Base

Step 4 - Create the Swing Arm

Step 5 - Create the Actuator

Step 6 - Create the Control Arm

Step 7 - Assemble the Gripper Parts
Using Mates

Step 8 - Animate the Gripper Action

This design is robot arm the goal of our project we are working on pick and- place robbitic arm picking up objects from one location and placing them in another. 




## Schedule
Week 1 (January 2-5)------------: Continue designs, drawings, initial CAD design .

Week 2 (January 8-12)-----------: Design and CAD ,code for motor.

Week 3 (January 15-19)----------: Continue CAD , Continue code for motor.

Week 4 (January 22-26)----------: Start assembly for onshape parts, motor, Continue coding for motor.

Week 5 (January 29-February 2)--: Continue  for preject, Continue coding.

Week 6 (February 5-9)-----------: Continue assembly for preject, Continue code for motor (work on notebook).

Week 7 (February 12-16)---------: Continue assembly for preject, Continue code for motor (work on notebook).

Week 8 (February 19-23)---------: Continue assembly for preject, Continue code for motor (drwaings of preject).

Week 9 (February 26-March 1)----: Continue assembly for preject, Continue code for motor (drwaings of preject).

Week 10 (March 4-8)-------------: Improve design for motors, strengthen weak points. Add walls and exit point if possible.

Week 11 (March 11-15)-----------: Improve design for motors, strengthen weak points. Add walls and exit point if possible.

Week 12 (March 18-22)-----------: If walls and exit point not added already, add. Perform kinetics tests for the pico, improve cushioning and structure.

Week 13 (March 25-29)-----------: Improve design for motors, strengthen weak points. Add walls and exit point if possible.

Week 15 (April 8-12)------------: Improve drawing and others.

Week 16 (April 15-19)-----------: work on issues for onshape and code.

Week 17 (April 22-26)-----------: Finish with Onshape and code .

Week 18 (April 29-May 3)--------: Finish printing get videos and photos .

week 19 ( May 3, 18)---------: Finish code and onshape and print also assembly.

Week 20 (May 20-30)--------------: Finish documentation.

Week 21 (May 29-31)-------------: Finish documentation. 

## Sketches
![317787767-896c4c5b-4e64-4d1d-b46a-123b3a68b62f](https://github.com/IANDORA87/engineer3/assets/143534987/b466ac69-1554-4689-bd5f-14cb3b67ba49)
![317787933-18be97c7-8c6a-47fe-aa0d-1148cbb50759](https://github.com/IANDORA87/engineer3/assets/143534987/ddc19f84-b8ef-4aa5-ac76-42600269a7d9)

## Pseudocode

```
python
import time 
import board
from analogio import AnalogIn
import pwmio
from digitalio import DigitalInOut

#pins
potentiometerpin = AnalogIn(board.A0)
motorpin = pwmio.PWMOut(board.D7)

while True:
    print(button.value)
    if button.value:  # Button is pressed (remember, we're assuming it's pull-down)
        print("btn1 pressed \t")
        print(current_angle)
        current_angle = current_angle + 10
        current_angle = max(0, min(360, current_angle))
    time.sleep(0.05)  # Small delay to avoid excessive checking

    print(button2.value)
    if button2.value:  # Button is pressed (remember, we're assuming it's pull-down)
        print("btn2 pressed \t")
        print(current_angle)
        current_angle = current_angle - 10
        current_angle = max(0, min(360, current_angle))
        print(potentiometerpin.value)
    time.sleep(0.1)
    motorpin.duty_cycle = potentiometerpin.value

    time.sleep(0.05)  # Small delay to avoid excessive checking
```


## Links

https://cvilleschools.onshape.com/documents/45a013841ca662a47591e1ff/w/3954e8a8cc011ba53df39d5e/e/5a5578e3d4a967c2c8b67bae?renderMode=0&uiState=66589bc30f48217e21d144c4
https://docs.google.com/spreadsheets/d/137HGSNZTTR_IkVGg8gcBn5OXVTHr438-3fES2nv-ZDA/edit#gid=0

## Bill of materials

![image](https://github.com/IANDORA87/engineer3/assets/143534987/e02d3528-53e1-48ed-b444-978b54b90621)


## Risk Mitigation

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!



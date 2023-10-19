____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Motor_control


### Description & Code Snippets

  * The goal of the assignment was to control motor with the speeding button. 
  * I accomplish to my goal by using goal and ask firend for help and using my idea also I take a step by step top accomplish to my goial.
  * motors can draw a lot more juice (current) than LEDs.  In fact, they draw so much current, we don't want to power them directly from the Arduino.  That might fry the Arduino.  So, we will power our motor directly from a 6 V battery pack.

 
### Evidence

    *  https://www.tinkercad.com/things/brGb4NP2EIS-writing-the-code/editel?lessonid=E2IR521ISCBY8RV&projectid=O73WOLIISCC2EWG#/lesson-viewer

    * this is link for tinkercad





### Wiring

   * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/5d562fad-3a4a-4833-9f7a-eaea2fdb499e)
   * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/f6ea0824-a370-4ba4-8cf4-1b1a726c3167)





### Reflection


  * It is very helpful to using something like Motor because it can go forward and backward when I was use the Motor it was fun for me because it is going forward and backward but it is more when you are using the Motor on your projects. whenever I have projcet I use      motor control or tt motor. However the motor control is something to use in your project. It was little hard to find the wiring but the code was easy to find for motor control it was very short code for motor control.





____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Practice Design from Drawings: The Hanger




### Description 

   * The purpose of this assignment is to build or design the Hanger and practice with onshape and getting using to onshape and you have match the mass from your design to the assingment mass. 


### Evidence

   *  blob:chrome-untrusted://media-app/9883afb7-8785-4038-8002-6f930bdf492d
   *  blob:chrome-untrusted://media-app/7d4ad6c8-954f-4423-a3b5-0a8eda5f27ac


### Part Link 

   * https://cvilleschools.onshape.com/documents/7a3762d556f61fc3dc62d882/w/b3b7689a296f9a2abbe75745/e/0e37ce298fa604f1b41dd69f?renderMode=0&uiState=652575a29e55ae7675793fa3



### Reflection


  * The Hanger was easy to build and design it was fun to because I whited too long for this type of assinmnets. It is very fun to get use to onshape and design something nice. In this assignment thanks to the teacher because the teacher help us with some of the details to make this assingment easily for us. In this assignment you can help with friend and classmade.




________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Onshape Certification Prep: The Swing Arm




### Description

   * The purpose of this assignment is to build or design the swing arm and practice with onshape and getting using to onshape and you have match the mass from your design to the assingment mass. the swomg arm should be done with the right mass and design.

### Evidence

   * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/7054272b-738a-440e-9c22-1e16bc67199a)\
   * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/e097f2b5-f6b8-4066-a616-f3c2741158af)
   * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/3fc97015-61f3-40cb-aafc-8f0594b3edaa)




### Part Link 

   * https://cvilleschools.onshape.com/documents/a498ce7f3ced3445f05b924e/w/a171c8d9b7a63e24ff2b5968/e/b90332f0cfd616d71bed4f90?configuration=List_BTYWYw502p6AGK%3DDefault&renderMode=0&uiState=652568262b7a2b2847eefe72


### Reflection



 * This is assignment  I have to work on the  Designing Swing Arm I work on it for 3 hours to do it. To make everything I use a lot of new tools because it makeing easy for me and  i don't have to use line tool there are other tool that make mach easy  and yeah this is everything i did in this assignment just make the Designing the swing arm. This assignment was kind of easily for me to do because my first reason is that you just copy and it show you what to do. My next reason is that you don't have build same thing for different size you can just use the configurations tool to help you with it. In this assignment it will be very easily if you use the tool call configurations it is very helpful. It can help you with a lot different things. For example, it helps you with different size and different colors.


__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Photointerrupters


### Description & Code Snippets

  * The goal of the assignment was to use the Photointerrupters. 
  * I accomplish to my goal by using my ideas and ask firend for help and using my friend idea also I take a step by step top accomplish to my goial.
  * Photointerrupters Wire up a circuit that will turn on when something is in between the legs of the photointerrupter.



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


 
### Evidence


  * C:\Users\iandora87\Downloads\IMG_5041.MOV
    




### Wiring


  * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/a7029ac8-77a8-4157-ad6c-509af27e89be)
  * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/963a9b84-47e7-4da9-94eb-015809329444)



### Reflection

  * This assignment is not easy and not hard because when I start this assignment it take me a lot of time because of coding  so the thing was that my coding was right but the Photo-interrupters was not working and I pet so many different coding but the thing was that my coding was not working I ask for help from  teacher and the teacher tell me that my Photo Interrupters was not working.




_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


## CircuitPython Servo
 


### Description & Code Snippets

  * Get a 180° micro servo to slowly sweep back and forth between 0 and 180°. Spicy part: Now control the servo with 2 buttons. The servo only moves if you are pushing a button.




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

   
 
### Evidence
    


### Wiring


  * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/5c4af0d8-5d09-405a-83b1-e99f6da88e4a)



### Reflection

 

  * I learn that how to do the code for this assingment. It take me 2 day because of the coding and I didn't do coding for long now this was the frist assingment for this year.I work on my code for 2 day. I found that my 1 wire was on pule than I fix my wire and I did my coding and other things as will. One things that I used help a lot of time from Mr. David.



________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

### CircuitPython Distance Sensor
 


### Description & Code Snippets

  * I've broken the assignment into 3 stages, to make your life easier:

  * Use the HC-SR04 to measure the distance to an object and print that out to your serial monitor or LCD in cm.
    Next, you will get the neopixel to turn red when your object is less than 5cm, and green when its 35cm.  Ignore the blue and 20cm for now, let's just keep it simple.
    For your final version of this code, you'll smoothly shift the color of the onboard neopixel, corresponding to the distance, according to the graphic below.
    (Neopixel should stay red when below 5cm and green when above 35cm)

 
### Evidence

 

 * https://github.com/IANDORA87/engineer3/assets/143534987/f2597999-57a9-4170-a937-4a6be8cfaa36



### Wiring

 * ![image](https://github.com/IANDORA87/engineer3/assets/143534987/21dbde8e-a2a1-4571-a597-396530ac50ab)




### Reflection


 * This was assignment that I did in engineer 2 and I did once again. However, I want to make something fun and work on something in my class time in engineer so I work on this in my class time. This year the code was much differet.





# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launchpad 1](#Raspberry_Pi_Launchpad_1)
* [Launchpad 2](#Raspberry_Pi_Launchpad_2)
* [Launchpad 3](#Raspberry_Pi_Launchpad_3)
* [Launchpad 4](#Raspberry_Pi_Launchpad_4)
* [Crash Avoidance 1](#Raspberry_Pi_Crash_Avoidance_1)
* [Crash Avoidance 2](#Raspberry_Pi_Crash_Avoidance_2)
* [Crash Avoidance 3](#Raspberry_Pi_Crash_Avoidance_3)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Raspberry_Pi_Launchpad_1

### Assignment Description

For this assignment we were tasked with creating a countdown from 10 that displayed on the serial moniter, at the end of the countdown, LIFTOFF should be printed.

### Evidence 

![Evidence_launchpad1](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/266376856-d6981811-ca07-442e-838a-f10ebdc2a6cd.gif)

### Code

[My code is here](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/launchpad_1.py)

### Reflection

This was my first time coding in circuit python in a while, and my first time using the pico, so I was bound to run into issues. Thankfully, they were all relatively minor and I was able to figure them out. I had some trouble with the new file organization of the picos, I was trying to run code from a new vs code file, but learned that in order to run code on the picos, you have to use the code.py file found on the actual pico drive. I also had some trouble remembering how to use "for" loops, but after reading over [this site](https://www.w3schools.com/python/gloss_python_for_range.asp) I was able to remember when, and how to use them to help me finish this assignment. 

&nbsp;

## Raspberry_Pi_Launchpad_2

### Assignment Description

For this assignment we built upon [launchpad_1](#Raspberry_Pi_Launchpad_1) where we coded a countdown for a lauchpad, and added 2 LEDs to it. One red LED to blink as it counted down, and one green LED to signify liftoff.

### Evidence 

![Evidence_launchpad2](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/266664910-ea34df20-a0a2-4264-a263-71d09dffac38.gif)

### Wiring

![Wiring_launchpad2](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/IMG-2678.jpg)

### Code

[My code is here](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/launchpad_2.py)

### Reflection
I ran into very few issues while coding this portion of the assignment, and the issues I did encounter were very minor. For example, I had trouble with how to wire the pico, I had the wiring diagram reversed in relation to my board. Another issue I had was forgetting to use ctrl + c to stop running the uploaded code, because I had a loop at the end of my code, it ran indefinitely and prevented me from uploading new code and making changes. All together, it was a relatively quick addition to the previous sections.


&nbsp;

## Raspberry_Pi_Launchpad_3

### Assignment Description

For this assignment we built upon [launchpad_1](#Raspberry_Pi_Launchpad_1) and [2](#Raspberry_Pi_Launchpad_2) where we coded a countdown and 2 LEDs for a launchpad. For this portion we added a button to signal the beginning of the countdown.

### Evidence 

![Evidence_launchpad3](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/266645327-fbb3ac5c-5c73-4c47-8530-02ba06b33c33.gif)

### Wiring

![Wiring_launchpad3](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/IMG-2679.jpg)

### Code

[My code is here](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/launchpad_3.py)

### Reflection
During this section, we modified our code in order to start the countdown when a button was pressed. Although I diddn't  run into any major issues during this portion, I did learn alot of useful information about the picos, their logic systems, and how to effectively wire them. For example, unlike boards we have used in the past, they have an internal pull down resistors, this means that the board is able to do much of the wiring for us. Rather than use an external resistor to wire a button, we can use simply one wire to ground and one to 3v. Although this assignment went pretty quickly, I still feel like I learned alot that will be very useful later in the year.


&nbsp;

## Raspberry_Pi_Launchpad_4

### Assignment Description

For this assignment we built upon [launchpad_1](#Raspberry_Pi_Launchpad_1), [2](#Raspberry_Pi_Launchpad_2), and [3](#Raspberry_Pi_Launchpad_3)where we coded a a button and LEDs to signal a countdown for a launchpad. For this section, we added a servo that would rotate 180&deg; when the countdown reached 0, or liftoff began.
### Evidence 

![Evidence_launchpad4](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/ezgif-3-d803740028.gif)

### Wiring

![Wiring_launchpad4](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/IMG-2680.jpg)

### Code

[My code is here](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/launchpad_4.py)

### Reflection
In this section of the launchpad assignment, we added a servo to the existing code and wiring. Although it was really only  a few lines of code, it was a really good refresher as to how to code servos, and their interactions with other physical and code components. The process of wiring the servo was also relatively straightforward, although I did learn that you need to be very careful when working with 5v on the picos, they have no short-protection, so if you mistake ground and 5v you can easily fry the board.

&nbsp;

## Raspberry_Pi_Crash_Avoidance_1

### Assignment Description

For this assignment we were tasked with linking an accelerometer with the pico using i2c, we were then able to take values for x, y, and z acceleration and print them on the serial moniter.

### Evidence 

![Evidence Accelerometer1](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/ezgif-1-9ddb8fe37b.gif)

### Wiring

![Wiring_Accelerometer1](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/Accelerometer1%20wiring.jpg)

### Code

[My code is here](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/accelerometer.py)

### Reflection
For this assignment I learned quite a lot about I2C devices, and how to use "F strings". Despite the fact that I have used I2C devices before, I have never used them on the pico's so, the setup was quite different, especially since we were initializing it to be compatible with 2 I2C devices on the same pins, namely the OLED screens which we will be adding in the future. Another useful python feature I learned while working through this assignment was how to use "F strings", F strings are a way of printing formated variables in python. [This](https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/) website was incredibly useful in learning how to effectively use F strings.

## Raspberry_Pi_Crash_Avoidance_2

### Assignment Description

On this assignment we built upon the previous crash avoidance system by adding a light which indicates when the accelerometer has been rotated 90&deg;, we also added a external LIPO battery.

### Evidence 

![Evidence Accelerometer2](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/accelerometer2.gif)

### Wiring

![Wiring_Accelerometer2](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/Accelerometer2%20wiring.jpg)

### Code

[My code is here](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/accelerometer2.py)

### Reflection

During this assignment I mostly dealt with concepts I was very familliar with, such as LEDs and wiring external power, but I was able to expand upon my knowledge with these in a way that logically added the next step to the current crash detection. Another new python feature I learned how to use was ``` :.3f``` in order to limit the number of decimals printed. Although this wasnt strictly part of this assignment, it made my output alot neater, and I knew it was a required aspect of the next assignment.  Lots of thanks to [Pinocchio](https://en.wikipedia.org/wiki/Pinocchio?scrlybrkr=973947e4) for help with the wiring on this assignment, at first I found it quite complicated, but he clearly explained it to me.

## Raspberry_Pi_Crash_Avoidance_3

### Assignment Description

For this assignment we expanded both our crash avoidance systems as well as our knowledge of I2C devices by adding a OLED screen to our system that would display values of angular velocity for x,y, and z.

### Evidence 

![Evidence Accelerometer3](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/accelerometer3.gif)

### Wiring

![Wiring_Accelerometer3](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/Accelerometer3.jpg)

### Code

[My code is here](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/accelerometer3.py)

### Reflection

This assignment was the first time I had used an OLED screen, so it brought with it it's own set of challenges, at first I was unable to locate the I2C address of the OLED, this was because I was using 3V3 EN to power my OLED and accelerometer. This was a problem because 3V3 EN is a pin to help debug the pico, and while it does ouput power for some uses ( which is why my accelerometer worked fine ) it does not work to power multiple devices. Another problem I ran into was setting up and printing the angular velocity on the OLED, because it was a new format, I was not used to printing on the OLED and had to re-read the assignment several times.

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

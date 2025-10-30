# NOVA-Future-Engineers
### ***We Are Team The NOVA Engineers***

</p>
<p align="center">
<img width="1024" height="1024" alt="Nova symbol" src="https://github.com/user-attachments/assets/4c8e5975-c9d1-4472-8a33-4b9ffa8786b2" />
</p>



# Content
`3DModels` This folder has the robot’s 3D design and the final rendered version

`Document (PDF form)` Includes a short document with project info from GitHub, saved as a PDF for A4 printing

`FlowChart` This folder includes flow diagrams that represent the logic and structure of the robot’s control system, showing how it interprets sensor data and executes movement decisions during tasks.

`Tables` This folder includes all the tables we used in our project, such as time plans, task schedules, and data organization charts.

`Program` Contains all the code we wrote for the WRO 2024 Future Engineers and some charts that explain it.

`Robot-Photos` Includes multiple photos of the robot from various angles — top, side, and bottom — to provide a full visual overview of the design.

`Schemes`Drawings that show how the robot’s parts and wires are connected.

`Team-Photos` This folder features photos of our team members participating in the WRO 2025 Future Engineers competition.

`Videos` Contains links to videos demonstrating how the robot performs and completes both missions successfully.

`Readme`This README file is divided into three main sections for better organization and understanding of the project’s structure.

  - [About Us](#part-1-about-us)
  - [Mechanical Design](#part-2-mechanical-design)
  - [Obstacle Management](#part-3-obstacle-management)


<p align="center">

# **Part 1: About Us**

## **This is our team**


We are three students from Hebron, Palestine, and we belong to the Programming and Artificial Intelligence clubs under the guidance of our coach, Abeer Al-Jabari. Our team was established with our participation in the Future Engineer program on September 1st. We have also previously participated in programming and STEM clubs.


## **Team name**
The name “NOVA” represents a new star that suddenly shines with renewed energy — symbolizing innovation, brilliance, and growth. It reflects our team’s spirit of creativity and ambition, as we strive to illuminate the field of engineering and technology with fresh ideas that drive progress and inspire excellence.

![team photo](https://github.com/user-attachments/assets/2673ebbf-6e51-4e4e-b58a-4979f9cb4431)


<hr>

## **Introduction to our team**

We are a group of passionate students participating in the Future Engineer competition  
Our goal is to learn, build, and showcase our creativity through robotics and programming
Our team works to distribute tasks in an organized manner that ensures the integration of efforts and the effective achievement of project objectives

**Raghad Wissam Al-Jaabari** 
- From Hebron
- 16 years old
- My hobbies are horse riding and badminton
-  Responsible for assembling the robot and executing programming tasks, integrating mechanical components with software to achieve the required performance and ensure the system operates efficiently
- ragadaljabari1@gmail.com

![ragad aljabari](https://github.com/user-attachments/assets/8b98042b-30b9-448b-9db8-dc492be81815)





**Rasha Islam Al-Fakhouri**
- From Hebron
- 15 years old
- My hobbies are reading, writing and storytelling
- Responsible for technical and organizational aspects, participated in presenting changes in project structures, in addition to continuous follow-up between stops to clarify the overall vision
- rashfakh9@gmail.com

![Rasha AlFakhouri](https://github.com/user-attachments/assets/edfd2734-58f9-4977-b31a-40d831bdf7a7)





**Layan Yousri Amro**
- From Hebron
- 14 years old
- my hobbies are sports and handicrafts
- She is responsible for documenting and writing reports on the project, and works on organizing the content and accurately documenting the work stages and results to present them in a professional and clear manner
- amrolayan95@gmail.com

![layan amro](https://github.com/user-attachments/assets/4e115d07-9c52-4cf7-a3f6-1b3798832854)




Despite our different ages and personal interests, we share a common passion: a love for technology and robotics, and a continuous desire to learn and improve. This passion drives us to participate in the Future Engineer competition and work together as a team

<hr>

### **Our Vision and Goal**
Our vision is to develop an intelligent robot capable of performing smart commands independently. We aim to build a system that can analyze its surroundings, make decisions, and complete tasks efficiently without direct human control. This project represents our first step toward creating innovative solutions that support our community and inspire future technological advancements Through this competition, we have gained valuable experience in robotics, programming, and teamwork. We also developed essential skills such as critical thinking, creativity, and planning In the future, we plan to use what we’ve learned to improve our projects, support younger students, and continue developing technologies that make a positive impact 

</p>

### **Work Schedule**

</p>

We developed a work plan to organize our steps and manage tasks within the team. It outlines what needs to be done each day, helping us set priorities, track our progress, and work with focus and teamwork to achieve our goals efficiently and accurately:
<img width="1291" height="713" alt="Plan_schedule" src="https://github.com/user-attachments/assets/b3b48192-0a4a-46f4-b8da-cc856f5ef26e" />


<hr>
</p>

# **Part 2: MECHANICAL DESIGN**
### **First, an introduction to the parts of the robot**
- **Robot mind**

The Raspberry Pi 4 Model B serves as the Main Processing Unit (MPU), acting as the robot’s central brain. It executes the complex Python code and coordinates all real-time sensory data and actuator commands.
We selected the Raspberry Pi 4 for its high-performance quad-core Cortex-A72 processor (1.8GHz) and 64-bit architecture. This computational power is non-negotiable, as it provides the necessary capacity to simultaneously manage:
- Computer Vision (CV): Processing real-time video frames from the USB Camera using the OpenCV library to detect and track colored obstacles.
- Sensor Fusion: Rapidly integrating data from the IMU (Gyroscope) and the four Ultrasonic Sensors for path correction and obstacle avoidance.
- In compliance with competition rules, the code is loaded onto the Raspberry Pi prior to the start. The entire autonomous routine is initiated by a physical push button connected to a GPIO pin, which activates the main Python script.
![R](https://github.com/user-attachments/assets/7df9a525-2814-4c7d-b86d-4e2bccb98d24)

- **Motor Driver L298N**

L298N Dual H-Bridge Motor Driver: The Power Bridge
The L298N module serves as an essential protective and intermediary power stage between the robot's battery and its drive motor.
The Necessity of a Driver:
The Raspberry Pi (our main controller) operates using low-power signals and cannot safely source or sink the high current required by the DC propulsion motor. Attempting to connect the high-power battery circuit directly to the Pi's low-voltage GPIO pins would result in immediate and irreversible damage to the controller. Therefore, the primary role of the L298N is to act as a current amplifier and insulator, safely handling the large electrical load demanded by the motor.
How the System Works (The Dam Analogy):
The L298N can be visualized as a large, reinforced concrete dam built to manage the powerful current flowing from the 9V battery (the reservoir) to the motor (the turbine). The Raspberry Pi acts as the control mechanism that precisely regulates the dam's sluice gates (via PWM signals). The Pi merely sends low-voltage commands to the L298N, instructing when and how much of the high-power battery current should be directed to the motor, without ever having to handle the power itself.
Component Description:
This module is based on the widely used L298 Dual H-Bridge Integrated Circuit. While the board is capable of controlling two DC motors independently (up to 2A peak current each), our application utilizes only one motor port to drive our single-motor RWD system. The unit is optimized for microcontroller interfacing, requiring only a few digital lines for full control. The board also features essential integrated components, including LED power indicators, internal protection diodes, and an onboard +5V voltage regulator which can supply power to the low-voltage controller (like the Raspberry Pi) for convenience.
Key Technical Data:
- Driver: L298N Dual H-Bridge DC Motor Driver
- Operating Voltage Range: DC 5 V - 35 V (Motor Power)
- Peak Current: 2 Amp per motor
- Input Logic Voltage (Control Signal): 
- Low: -0.3 ≤ Vin ≤ 1.5V (control signal is invalid).
- High: 2.3V ≤ Vin ≤ Vss (control signal active).
- Maximum Power Dissipation: \text{20W} (at T = 75^\circ C)
- On-board Feature: Integrated +5V regulated output supply.
- Approximate Dimensions: 4.3cm × 4.3cm × 2.7cm
![d](https://github.com/user-attachments/assets/9be4d7c9-9bb2-4e9f-9979-cf03fbd57654)

- **Motor DC**

The DC Geared Motor provides the necessary mechanical power to drive the Single-Motor Rear-Wheel Drive (RWD) system. This component is a standard 9V DC motor with an integrated gearbox . The gear reduction is critical; it increases the motor’s torque significantly while reducing the output RPM, providing the crucial force needed for propulsion and enabling precise speed control at lower velocities. The motor is directly controlled by the 9V power output from the L298N Motor Driver, which utilizes PWM signals from the Raspberry Pi to modulate both speed and direction.
For efficient performance and to stay within the L298N driver's safe operating limits, the motor's current draw is estimated to be less than 1.5A under typical load. While specific torque and RPM values are often custom to the supplier, the motor is generally rated for approximately 300 RPM at 9V and provides sufficient torque (estimated at ~ 5-10  kg ٠ cm) to manage the robot's mass and navigate the competition course
![motor](https://github.com/user-attachments/assets/062b6f21-24eb-441e-92e2-49b57b84d322)

- **Servo Motor**

Precise Steering Actuator
The Servo Motor is the critical actuator responsible for translating the path-planning commands from the Raspberry Pi into physical steering motion.
1. Integration with Ackermann Geometry
Function: The servo is connected via a custom linkage to the front wheels, enabling the precise, differential steering angles required by the Ackermann Steering Geometry.
Model: Based on its characteristics (and likely MG996R designation), the model used is a Digital, High-Torque Servo with Metal Gears. The high torque rating (~ 10kg ٠ cm) ensures sufficient force to overcome the mechanical friction and maintain the steering angle under load.
2. Control and Power
Control Protocol: The servo angle is precisely controlled by sending Pulse Width Modulation (PWM) signals from the Raspberry Pi's GPIO header. The duration of the pulse dictates the angular position of the angular position of the wheel.
Power: The servo requires a stable operating voltage typically in the 5V  -  6V range. This power is reliably supplied by the Step-down Module (Voltage Regulator), ensuring steady operation independent of the main 9V battery fluctuations
![servo motor](https://github.com/user-attachments/assets/6f7a34e5-0034-4c64-9280-5f6f9f28bb13)

- **voltage regulator XL4015**

The DC-DC Step-down Module is a non-isolated buck converter based on the widely used LM2596 integrated circuit. It serves as a crucial power conditioning component, managing the transition from the high-power drive system to the sensitive control electronics.
1. Power Regulation Necessity
The robot's propulsion system operates on a 9V battery supply, necessary for the  DC drive motor. However, the sensitive low-voltage components—namely the Raspberry Pi 4 5V/3A minimum), the Servo Motor, and all digital Sensors—require a stable and lower operating voltage.
The primary function of this module is to safely and efficiently step-down the 9V input voltage to a regulated 5V output. This prevents potential damage to the control board and ensures power stability, which is vital for the reliable operation of the Raspberry Pi's CPU and GPIO communications.
2. Key Operational Data
The module accepts a wide input range 4.5V to 40V), easily accommodating the 12V battery output. It is manually tuned to provide a precise 5V output voltage and is rated for a continuous output current of approximately 3A, providing a sufficient power budget for all low-power electronics in the system. The high conversion efficiency (> 80\%) minimizes energy loss as heat, preserving battery life
<img width="634" height="444" alt="voltage regulator XL4015" src="https://github.com/user-attachments/assets/780b0bdf-d0de-46ae-a807-0672d56c7aa9" />

- **gyroscope MPU6050**

Inertial Measurement Unit (IMU): MPU-6050
The MPU-6050 Inertial Measurement Unit (IMU) serves as the primary sensor for motion and orientation tracking, correcting for mechanical and environmental inaccuracies that cannot be managed by vision or distance sensors.

1. Function and Integrated Components
The MPU-6050 is a sophisticated MotionTracking device that integrates a 3-axis gyroscope and a 3-axis accelerometer. It utilizes 16-bit Analog-to-Digital Converters (ADCs) for high-precision data capture.
- Gyroscope (Angular Rate): Measures the rate of rotation around the X, Y, and Z} axes. This is essential for detecting unwanted yaw (heading deviation) and precisely correcting the Ackermann steering angle. The range is user-programmable up to +- 2000⁰/sec.
- Accelerometer (Linear Acceleration): Measures linear acceleration and gravity, used to determine the robot's tilt angle (roll and pitch) and estimate linear distance traveled. The range is programmable up to +-16g.
- Digital Motion Processor (DMP): This integrated hardware unit processes complex 6-axis MotionFusion algorithms. Crucially, the DMP offloads computation from the Raspberry Pi by processing raw sensor data into clean, ready-to-use orientation information directly on the chip.
2. System Integration and Power
The MPU-6050 communicates with the Raspberry Pi 4 using the efficient I2C serial communication protocol. This protocol is highly efficient, requiring a minimum number of dedicated GPIO pins.
- Power: The module operates between 3V to 5V and is safely powered by the 5V} regulated output from the LM2596 module.
3. Role in Navigation
The IMU provides the core data for internal navigation (dead reckoning). Regardless of whether the system implements explicit sensor fusion with the ultrasonic sensors, the highly accurate angular rate and acceleration data are crucial for stabilizing the robot's movement and ensuring that the programmed path is maintained against physical disturbances
![j](https://github.com/user-attachments/assets/ee42bb96-c9a1-4cdc-b19b-56fb1aeb2d33)


- **Ultrasonic**

Ultrasonic Sensors (HC-SR04): Comprehensive ToF Ranging System
The robot is equipped with a total of four HC-SR04 Ultrasonic Sensors that form the primary short-range ranging system. These sensors provide the vehicle with echolocation capabilities, on par with how bats and dolphins locate objects in complete darkness and beneath the water surface. This array is fundamental for robust, real-time obstacle avoidance and precise navigation along the course boundaries.
Strategic Implementation and System Integration
The four HC-SR04 sensors are strategically positioned to maximize situational awareness: one mounted in the front, one in the rear, and one on each of the right and left sides of the chassis. This arrangement minimizes blind spots and provides the angular data necessary for advanced Sensor Fusion.
Power and Interface: The sensors require a stable +5V regulated supply, drawing less than 15mA each. Each sensor utilizes two dedicated GPIO pin (Trigger and Echo) on the Raspberry Pi for control and data acquisition.
Sensor Fusion Role: The simultaneous input from four points allows the control system to accurately determine both the distance and the angular position of an obstacle. This redundancy is vital for high-reliability autonomy, allowing the algorithm to differentiate between a critical frontal obstacle and a simple boundary wall alongside the vehicle.

Principle of Operation and Technical Specification
The HC-SR04 module operates on the principle of measuring the Time-of-Flight (ToF) of an ultrasonic sound wave.
1–Triggering: Measurement begins when the Raspberry Pi sends a minimum 10uS high pulse to the Trigger pin, prompting the transmitter to emit an 8-cycle  burst of ultrasonic sound at 40kHz.
2– Echo Reception: The sound wave reflects off an object, and the duration it takes to return is measured. The sensor outputs a high pulse on the Echo pin, the width of which is directly proportional to the distance.
3– Calculation: The Raspberry Pi measures this pulse width (time), and the distance is calculated using the formula
Distance = Speed × Time, divided by two since the time measured is for the signal's round trip.
The sensor boasts a practical measuring range of 2cm to 400cm and an accuracy that can reach 3mm. This combination of range and precision makes it perfectly suited for the short-range, dynamic obstacle avoidance challenges presented in the competition course
![Introduction-to-HC-SR04](https://github.com/user-attachments/assets/77b78609-52e6-4001-93a0-3b93dd555b82)


- **switch**

This switch controls the connection and disconnection of power between the battery and the robot. Since the rules require cutting off power before operation, we added this switch to comply with that. We soldered the red (positive) wire to the input side of the switch and another red wire to the output side. When the switch is turned on, power flows from the battery to the step-down module and then to the rest of the robot’s components
![switch](https://github.com/user-attachments/assets/2f993690-e7aa-41dd-92d4-d6dc8d43ba04)

### Robot 
**This picture shows our robot in real life, displaying how it looks with all its components assembled**
![2](https://github.com/user-attachments/assets/ba2e5261-6d83-489a-a7eb-884af5177500)

***
### Wiring Diagram and Power Distribution Diagram
- **It shows you the connection of various components to the Raspberry Pi**
![6](https://github.com/user-attachments/assets/4c8421e0-56f3-4bf7-9b27-8d39f5d2d489)

- **It shows the ports of various components connected to the Raspberry Pi, as well as the voltage levels supplied to the Raspberry Pi and its connected components**
![s](https://github.com/user-attachments/assets/76d82b49-d041-4ec6-86dd-2f69c3d83fa3)

***

# **Part 3: Obstacle Management**


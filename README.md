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
- I love reading literature and philosophy, and I enjoy playing badminton
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
 ### **Firstly, the structure of the robot**
- **This car is a self-assembled (DIY) model that is built on a metallic chassis and uses an Ackermann Steering system to simulate the motion of real cars
The components of the car were connected and operated using a Raspberry Pi, programmed in Python to control movement and steering**

**This is the chassis**

![car](https://github.com/user-attachments/assets/e9da738f-8dcb-413c-9adc-34b0215bbf0a)

- Watch this video from the manufacturing source  [click here](https://www.youtube.com/watch?v=w_RRwR02S6U)

<div align="center">
  <a href="https://www.youtube.com/watch?v=w_RRwR02S6U">
  </a>
</div>

<hr>
</p>

**Car size**

![61TixKds-fL _AC_SL1200_](https://github.com/user-attachments/assets/2af9e034-c06c-4479-8742-9a26020d7f70)

<hr>
</p>

- **This car is not a remote-controlled vehicle; rather, it is an experimental platform developed to apply the principles of mechanics, control, and programming in the field of intelligent vehicles.
Thanks to the use of the Ackermann Steering system, the car replicates the actual steering mechanism of real vehicles, unlike the differential steering systems used in many traditional robots**
- **The car was entirely assembled and programmed manually as part of participation in the Future Engineer competition, using the Raspberry Pi platform**

<hr>
</p>

### **Ackermann Steering**

- **This is the servo that controls the wheels using the Ackermann Steering system:**

<img width="824" height="594" alt="servo" src="https://github.com/user-attachments/assets/8098b102-12a8-4a48-ade2-6cbb94b3886c" />

Ackermann Steering Geometry: Precision Path Management
The chassis design of our autonomous vehicle is fundamentally based on the Ackermann Steering Geometry. We implemented a custom-modified version of this linkage system to ensure optimal cornering performance.
1. Principle of Operation
Unlike simpler steering methods (like skid steering), the Ackermann principle ensures that during a turn, the steering axis of all four wheels intersects at a single, momentary center point. This is achieved by ensuring the inner wheel (the wheel closer to the turn’s center) rotates at a sharper angle than the outer wheel.
This difference in rotation angle is critical because it forces the wheels to follow four distinct radii, allowing the inner wheel to travel a shorter path and the outer wheel a longer path, preventing any lateral slippage.
In our RWD system, the front wheels execute the steering motion around their respective pivots, while the single DC motor drives the non-steering rear wheels.

2. Mathematical Description (The Ideal Geometry)

![Ackermann](https://github.com/user-attachments/assets/5d947b3d-9b4c-4ae5-8616-1f56afc65a02)

This diagram illustrates the Ideal Ackerman 
Steering Geometry. This geometry ensures that all four wheels, when steered, trace concentric circles around a single, common point, the Ackerman Center (C_a).
This fundamental relationship is governed by the vehicle's fixed dimensions—the Track Width (T) and the Wheelbase (W)—and the required steering angles:
cot(a_o) - cot(a_i) = T/W
Where a\_i is the inner wheel steering angle and a\_o is the outer wheel steering angle.
In this ideal setup:
The Inner Wheel Angle (a\_i) is always greater than the Outer Wheel Angle (a\_o) (a\_i > a\_o).
The lines drawn perpendicular to the plane of each wheel intersect precisely at C_a, ensuring all wheels roll without excessive side-slip.
Note: Real-world steering systems use a Modified Ackerman principle to optimize performance across the entire steering range, deviating slightly from this ideal formula.


3. Advantages for Our Robotic System:
Implementing the Ackermann geometry was a strategic choice that provided several specific benefits essential for the competition requirements:
Elimination of Tire Slippage: The main advantage is the prevention of tire scrubbing and slippage, which is crucial for accurate path following and maintaining maximum traction on the carpet surface.
Precise Path Management: The system offers high control over the front wheel's angle, allowing for precise steering control necessary to navigate between colored obstacles and adhere to strict course boundaries.
Single-Motor Compliance: This configuration naturally supports the requirement of using only a single DC motor for propulsion, simplifying the mechanical drivetrain while maintaining high maneuverability
Watch this video to understand the system [click here](https://www.youtube.com/watch?v=sF-PfAu50Fo)
<div align="center">
  <a href="https://www.youtube.com/watch?v=sF-PfAu50Fo">
  </a>
</div>

- **Wheels**

The wheels of this smart robot car have specific material and performance characteristics:
Wheel Rims (Hubs): The rim material is ABS (Acrylonitrile Butadiene Styrene). They are purely aesthetic
Tires (Rubber): The tire material is Rubber
Performance: The rubber material provides a large coefficient of friction and strong grip (traction) force. This design is crucial for stable and controlled movement across different surfaces
Internal Structure: All tires are internally fitted with a foam lining (insert). This foam insert provides necessary support and structure to the soft rubber tire, which is essential for consistent performance and shock absorption in RC and robot cars

![61A1H6YRZoL _UF350,350_QL80_](https://github.com/user-attachments/assets/9068ce34-bb8c-4153-b0e0-9433e0bb5ad7)

<hr>
</p>

- **Robot Car Gears**

In our project, we replaced the large gears with smaller gears in the robot car to control its movement speed
Gears are mechanical parts that transfer motion and rotation from the motor to the wheels, affecting both speed and torque
By replacing the large gears with smaller ones, we were able to reduce the car's speed and increase control accuracy, especially when performing precise movements or working with the distance sensor and relay.
- This modification helped make the car's movement more stable and safe, while maintaining the motor's power to drive the wheels smoothly

<img width="927" height="352" alt="1" src="https://github.com/user-attachments/assets/2887284f-e565-4815-9ff5-6f3e8d6506ab" />

***

<img width="766" height="405" alt="part" src="https://github.com/user-attachments/assets/9ae0b720-7180-4fcb-bb56-5eafebaee228" />

### 📦 Bill of Materials (BOM)

| Part Name | Quantity | Description |
|----------|---------|-------------|
| Front metal chassis plate | 1 pcs | Front base for Ackermann steering system |
| Rear metal chassis plate | 1 pcs | Rear base for motor mounting |
| Electronics mounting plate | 1 pcs | Plate for Arduino / controller installation |
| Rubber wheels | 4 pcs | High-traction rubber wheels |
| Suspension spring | 1 pcs | Simple shock absorption system |
| Motor/servo mounting bracket | 1 pcs | Holder for servo or steering mechanism |
| Pulley / gear wheels | 2 pcs | Used in steering / drive linkage |
| Metal rods | Several | Used for steering linkage and frame connection |
| Bearings | Several | To reduce friction and improve smooth steering |
| Rod ends / ball joints | 4 pcs | Steering linkage endpoints |
| Servo mount brackets | 2 pcs | For attaching the steering servo |
| Metal steering arm | 1 pcs | Transfers servo motion to the wheels |
| Servo motor | 1 pcs | Controls front wheel steering |
| Spacer washers | 4 pcs | To maintain spacing between plates |
| Hex standoffs | Multiple | Structural support and spacing |
| L-shaped brackets | 2 pcs | Support brackets for structure |
| Screws (M2 / M3 assorted) | Set | Used for assembly |
| Nuts (M2 / M3 assorted) | Set | Used with screws |
| Metal shafts / pins | Multiple | For wheel/steering mechanism |
| Bearings housings | 2 pcs | Mounting for wheel axles |
| Plastic components | Several | Mechanical support parts |

<hr>
</p>

![71HcujKQaNL _AC_SL1500_](https://github.com/user-attachments/assets/f7be5660-cb13-4402-ad8d-7867f43b7131)

- **Brass Hex Standoffs** 

These brass hex standoffs are used to elevate and support the Raspberry Pi and other electronic components.
They provide extra stability, improve airflow, and help organize the structure of the robot.
We used them to raise the robot’s layers securely, and they come in different sizes depending on the design requirements.

<hr>
</p>

### **Secondly, 3D model pieces**

- **3D machine**

**Creality Ender 5S1**

![Creality Ender 5S1](https://github.com/user-attachments/assets/c0de7cdd-aa2d-4eb0-91d3-47151be23150)

The Ender-5 S1 is an FDM 3D printer with a stable cube-frame structure. It was designed to deliver better performance than previous models in the Ender series, offering faster and more responsive printing capabilities.
It is considered a great option for hobbyists and medium-level prototyping, thanks to its advanced features such as motion acceleration, direct-drive extrusion, and automatic bed-leveling support

#### General Specifications

| Specification            | Value |
|--------------------------|-------|
| Build Volume             | 220 × 220 × 280 mm |
| Nozzle Diameter          | 0.4 mm (standard) |
| Hotend Type              | All-Metal |
| Max Hot-End Temperature  | 300 °C |
| Filament Diameter        | 1.75 mm |
| Supported Filaments      | PLA, PETG, TPU, ABS, ASA |
| Extruder Type            | Sprite Direct-Drive Dual Gear Extruder |
| Max Printing Speed       | 250 mm/s |
| Max Acceleration         | 2000 mm/s² |
| Frame Type               | Cube-frame Cartesian |
| Auto Bed Leveling        | CR-Touch |

### Build Plate Specifications 

| Specification               | Value                                                                 |
|-----------------------------|-----------------------------------------------------------------------|
| Build Plate Surface         | Spring steel sheet with PEI coating (magnetic flexible plate)        |
| Build Plate Size            | 235 × 235 mm                                                          |
| Max Build Plate Temperature | Up to 110 °C                                                          |
| Heating Method              | AC/Heatbed (magnetic heated bed)                                     |
| Compatibility               | Compatible with PC/PEI/Glass plates (optional upgrades available)    |

### Tool Head Specifications 

| Specification               | Value        |
|-----------------------------|-------------|
| Max Speed                   | 500 mm/s    |
| Max Acceleration            | 20 m/s²     |

### Physical Dimensions 

| Specification      | Value                  |
|--------------------|------------------------|
| Printer Dimensions | 425 × 460 × 570 mm     |
| Package Size       | 578 × 474 × 340 mm     |
| Net Weight         | 12.2 kg                |
| Gross Weight       | 14.7 kg                |

### Electrical Requirements 

| Specification       | Value              |
|---------------------|--------------------|
| Voltage             | 100–240 VAC        |
| Frequency           | 50/60 Hz           |
| Rated Power         | ~350W              |
| Power Supply Output | 24V DC             |

<hr>

#### **Filament**: Polylactic Acid or simply known as **PLA**  
![PLA_Family](https://github.com/user-attachments/assets/7bd5eb8a-3b57-4c67-a5d5-f70937c5c195)

PLA (Polylactic Acid) is one of the most widely used filaments in 3D printing. It is a biodegradable thermoplastic derived from renewable resources such as cornstarch or sugarcane. PLA is favored for its ease of printing, low warping, and minimal odor, making it ideal for FDM (fused deposition modeling) 3D printers. This filament is best suited for prototyping, decorative items, and educational projects, offering good strength and surface finish.  

**Diameter:** 0.75 mm  
**Printer Compatibility:** Most FDM 3D printers, including Creality Ender-5 S1

<hr><br>

**Ultrasonic holder**

- We encountered an issue with the ultrasonic sensor readings due to instability during operation. To address this, we designed a custom 3D-printed mount to securely hold the sensor in place

After implementing this design, the ultrasonic readings became significantly more stable and accurate

The final design is shown below:
<table align="center">
  <tr>
    <td align="center">
<img width="996" height="830" alt="1 3d" src="https://github.com/user-attachments/assets/ca5e852a-dc85-4807-9777-395e310c0bf5" />

 <p><a href="https://github.com/rdji5/Eng-NOVA-/blob/main/3D%20model/Ultrasonic%20Holder%20(1).stl" target="_blank">Click here to view 3D model.</a></p>
  </tr>
</table>

**Camera holder**
- Similarly, we faced a challenge in determining the optimal placement for the camera. To solve this, we designed a special 3D-printed mount that allowed us to position the camera securely and achieve the desired angle for accurate image captur

The final designs are shown below:

<table align="center">
  <tr>
    <td align="center">
<img width="685" height="612" alt="camera" src="https://github.com/user-attachments/assets/ff868f99-5acc-427a-a83d-92cceeffbfef" />

 <p><a href="https://github.com/rdji5/Eng-NOVA-/blob/main/3D%20model/Cameraa.stl" target="_blank">Click here to view 3D model.</a></p>
  </tr>
</table>

<hr>
</p>

### **Third, parts of the robot**
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

This motor belongs to the class of DC Geared Motors, specifically the JGA25-370 series, known for providing a necessary trade-off between speed and torque for robotics and automation applications. It is designed to be highly compatible with popular microcontroller platforms such as Arduino, Raspberry Pi, and STM32, utilizing common DC motor driver modules.
- Model Name and Type: JGA25-370 DC Gear Motor. The name implies a 25mm gearbox diameter attached to a 370 series motor.
- Operating Voltage: The nominal operating voltage is 12V DC.
- Output Speed (No-load): It provides an output speed of 210RPM (Revolutions Per Minute) under no-load conditions.
- Torque Capability: The motor delivers up to 12Kg • cm of torque. This makes it suitable for medium-load mechanical motion control projects.
- Gearbox Material: It features a durable all-metal gearbox for enhanced strength and long service life, ensuring stable and reliable continuous operation.
- Output Shaft: The typical output shaft diameter is 6mm.
- Typical Applications: This motor is ideal for building robots, conveyor systems, smart vehicles, and other DIY projects requiring controlled motion.
- Stall Current: The internal motor (before the gearbox) can draw a Stall Current (maximum current draw when the shaft is blocked) of approximately 2.2 Amps at 12V.
- Motor Driver Requirement: This means the chosen motor driver (the module linking the motor to the Raspberry Pi) must have a continuous current rating exceeding 2.2 Amps per channel to safely operate the motor, especially when the car is starting or pushing against an obstacle.
2.3.2) Encoder:
    The motor comes integrated with an encoder to provide closed-loop control of speed and position, which is essential for precise robotic applications.
1) Encoder Type and Output Signal:
- The integrated encoder uses Hall Sensor technology.
- It provides two square wave outputs, designated as Channel A and Channel B.
- The signals are approximately 90° out of phase. This phase difference is crucial for determining the direction of rotation (quadrature encoding).
- The voltage output of the Hall sensor signals ranges from 0V to Vdc (the encoder's supply voltage).
3) Wiring and Physical Characteristics:
- Leads: The encoder assembly is terminated by 6 color-coded leads.
- Connector: These leads are typically terminated into a 6 female header with a 0.1''pitch (standard spacing).
- Length: The lead length is approximately 15cm.
- Mounting: The motor faceplate includes 2 mounting holes for M3 screws. The distance between these mounting holes is 18mm apart.
4) Wire Function (Based on common JGA25-370 Encoders):
- The 6 wires generally correspond to:
1)	Two Wires (Motor): For the 12V motor power (e.g., Red/White or Red/Black).
2)	Four Wires (Encoder): VCC (Encoder Power, usually 5V or 3.3V), GND, and the two signal lines (Channel A and Channel B).
![motor](https://github.com/user-attachments/assets/062b6f21-24eb-441e-92e2-49b57b84d322)
![Encode](https://github.com/user-attachments/assets/803035f0-677a-4387-90a3-af9d1a6f99ce)


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

- **Relay**

A relay is an electronic component used to control the switching ON or OFF of electrical circuits using a small electrical signal from a microcontroller such as the Raspberry Pi
The relay acts as an interface between low-voltage control circuits and high-voltage electrical loads
It operates on the principle of electromagnetism, containing a copper coil (Coil) that creates a magnetic field when current passes through it. This magnetic field pulls a metal armature, changing the connection state between its internal terminals:
- COM (Common): The common contact
- NO (Normally Open): Open by default and closes when the relay is activated
- NC (Normally Closed): Closed by default and opens when the relay is activated
When a signal is sent from the microcontroller to the relay, current flows through the coil, generating a magnetic field that moves the metal armature. This action switches the connected circuit ON or OFF

Relays are used to control devices that require higher current or voltage than the microcontroller can supply, such as:
- Running motors and fans.
- Turning lights or pumps on and off.
- Cutting power in safety or smart control systems.
Thus, the relay allows microcontrollers to safely and efficiently control high-power electrical systems without damaging sensitive electronic components

![relay](https://github.com/user-attachments/assets/7b52c186-1589-4f6e-a9ce-07a3e6804454)


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
<img width="925" height="557" alt="7" src="https://github.com/user-attachments/assets/26daaefd-ef29-4e43-9512-6f1685e3db0e" />


***

# **Part 3: Obstacle Management**

## Open Challenge round

In this stage, the robot is required to navigate the track for three complete laps, where the inner track walls are positioned randomly, all within a 3-minute time limit

### **Open Challenge round (Youtube Link)**

This video shows our robot completing the first round(Open Challenge), you can [click here]() to view the video we created.

<div align="center">
  <a href="">
  </a>
</div>

### **The strategy**

To navigate the initial stage intelligently, we developed a dedicated algorithm that empowered the robot to make autonomous directional decisions, Prior to encountering the first turn, the robot was in a state of uncertainty, unsure whether to proceed clockwise or counterclockwise

We incorporated ultrasonic sensors into the robot’s design to provide it with continuous spatial awareness. These sensors measured the distance to nearby obstacles on both the left and right sides 

**Left Sensor**: Conversely, if the right sensor measured a distance beyond 160 cm, the robot opted to move counterclockwise

<table align="center">
  <tr>
    <td align="center">
      <img width="685" height="612" alt="Counterclockwise" src="https://github.com/user-attachments/assets/a4255cc7-89bc-4cb5-acf7-a1210630334c" />
      <p>This is the counterclockwise rotation of the robot.</p>
    </td>
  </tr>
</table>


**Right Sensor**: If the left ultrasonic sensor detected a distance exceeding 160 cm (indicating ample space on that side), the robot interpreted this as a signal to move clockwise

<table align="center">
  <tr>
    <td align="center">
      <img width="685" height="612" alt="Clockwise" src="https://github.com/user-attachments/assets/bd65084d-5bea-47d2-a92d-cef351460ef4" />
      <p>This is the clockwise rotation of the robot.</p>
    </td>
  </tr>
</table>

<br><hr>

### **Flowchart**

![OpenChallenge](https://github.com/user-attachments/assets/6dca9022-0850-457c-abc6-37278b23cd26)

<hr>

# IDP M1 — Autonomous Delivery Robot

We’re building an automated guided vehicle (AGV) that collects packages from loading bays and delivers them to the correct storage racks without manual control
-

The robot needs to follow marked routes, pick up and carry packages, and detect their magnetic polarity. Packages collected from the left go to rack A; those from the right go to rack B. North-pole packages go to the upper racks and south-pole packages go to the lower racks. It must check that the delivery location is free before unloading.

We’re using MicroPython on a Raspberry Pi Pico 2, with VS Code and MicroPico for development. The software will handle navigation, motors, sensors, package handling and status lights. Detecting traffic lights through IR is an extra feature for the competition.

The goal is to deliver as many packages as possible within five minutes, safely and accurately. The robot also needs to be compact, easy to repair and properly documented.
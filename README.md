# UR5e Robotiq Gripper Visualization in RViz

This ROS 2 package provides a visualization setup for the UR5e robotic arm with a Robotiq gripper using RViz. It includes all necessary configuration files, launch files, and description files to get you started with visualizing the robot in a simulated environment.
![Screenshot from 2024-05-10 23-34-35](https://github.com/Sohaib-Snouber/UR5e_robotiq_gripper_RViz/assets/81733750/ba4a8526-0f9c-4a3d-bfa0-a26c5968265e)
## Features


- UR5e robotic arm and Robotiq gripper integration
- Ready-to-use RViz configuration
- Customizable Xacro files for robot descriptions

## Prerequisites

Before you begin, ensure you have the following installed:
- ROS 2
- RViz2

## Installation

To install the UR5e Robotiq Gripper Visualization package, follow these steps:

```bash
# Source your ROS 2 workspace
source /opt/ros/<ros2_distro>/setup.bash

# Clone the repository into your ROS 2 workspace
cd ~/your_ros2_ws/src
git clone https://github.com/Sohaib-Snouber/UR5e_robotiq_gripper_RViz.git

# Build the package
cd ~/your_ros2_ws
colcon build --packages-select ur5e_robotiq_gripper_visualization

# Source the workspace
source ~/your_ros2_ws/install/setup.bash
```

## Usage

To run the visualization, use the provided launch file:

```bash
ros2 launch ur5e_robotiq_gripper_visualization view_ur5e_gripper.launch.py
```


## License

Distributed under the MIT License. See `LICENSE` for more information.


## Acknowledgments

- Thanks to [Universal Robots](https://github.com/UniversalRobots/Universal_Robots_ROS2_Description) for providing detailed models and documentation of their robotic systems.
- Thanks to [Robotiq](https://github.com/ros-industrial/robotiq) for the open-source gripper models and control software which have been integral to this visualization project.
- Special thanks to all the contributors of the ROS community whose shared insights and code snippets have been invaluable.
```

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.descriptions import ParameterValue

def generate_launch_description():
    # Set up the path to the Xacro file
    ur5e_xacro_path = PathJoinSubstitution([
        FindPackageShare('ur_description'),
        'urdf',
        'ur5e_robot.xacro'
    ])

    # Command to convert Xacro to URDF
    robot_description = {
        'robot_description': ParameterValue(
            Command([
                FindExecutable(name='xacro'),
                ' ',
                ur5e_xacro_path
            ]),
            value_type=str
        )
    }

    # Joint State Publisher Node
    joint_state_publisher_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher'
    )

    # Robot State Publisher Node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[robot_description]
    )

    # RViz Node
    rviz_config_path = PathJoinSubstitution([
        FindPackageShare('ur5e_gripper_visualization'),
        'config',
        'ur5e.rviz'
    ])

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz',
        arguments=['-d', rviz_config_path]
    )

    return LaunchDescription([
        joint_state_publisher_node,
        robot_state_publisher_node,
        rviz_node
    ])


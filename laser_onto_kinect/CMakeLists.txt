cmake_minimum_required(VERSION 2.8.3)
project(laser_onto_kinect)
find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure
  roscpp
  rospy
  tf
)
generate_dynamic_reconfigure_options(
    cfg/config.cfg
)
catkin_package(
  CATKIN_DEPENDS dynamic_reconfigure roscpp rospy tf
)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

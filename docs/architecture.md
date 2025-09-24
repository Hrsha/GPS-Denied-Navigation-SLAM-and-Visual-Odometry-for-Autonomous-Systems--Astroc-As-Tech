# Architecture Overview

Two-layer AI stack:
- **Onboard AI (Jetson Orin):** Visual SLAM/VIO, obstacle avoidance, local mapping, real-time pose output.
- **Cloud AI / SaaS:** Mission analytics, fleet telemetry, long-term mapping and model updates.

Main ROS2 nodes:
- `camera_drivers` -> publishes camera + camera_info topics
- `orb_slam3_ros` -> performs SLAM / VIO, publishes odometry/pose and TF
- `robot_localization` -> EKF fusion of VIO + IMU (and GPS if available)
- `mavros_bridge` -> forwards vision pose / setpoints to PX4
- `obstacle_avoidance` -> local planner (optional plugin)

Integration points:
- Use `/mavros/vision_pose/pose` or `VISION_POSITION_ESTIMATE` MAVLink messages so PX4 can accept external vision pose.

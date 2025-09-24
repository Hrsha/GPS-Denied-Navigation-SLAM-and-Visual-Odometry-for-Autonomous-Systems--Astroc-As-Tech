# Calibration Guide

1. **Stereo / Mono camera intrinsics**
   - Use ROS `camera_calibration` or OpenCV tools to produce `camera_info` yaml files.

2. **IMU ↔ Camera extrinsics**
   - Use Kalibr for precise extrinsic calibration (recommended).
   - If Kalibr is not possible, do manual alignment and verify with visual-inertial test recordings.

3. **Timestamp sync**
   - Use hardware triggers or PTP for accurate timestamping.
   - If not available, ensure software sync and measure time offset.

4. **Storage**
   - Place calibration outputs in `configs/camera_calib/` and document the file names in launch configs.

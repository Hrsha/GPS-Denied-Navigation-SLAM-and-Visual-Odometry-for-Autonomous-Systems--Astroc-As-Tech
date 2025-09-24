#!/usr/bin/env python3
"""
Setup script for GPS-Denied Drone Navigation System
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
current_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="GPS-Denied-Navigation-SLAM-and-Visual-Odometry-for-Autonomous-Systems--Astroc-As-Tech",
    version="0.1.0",
    author="Hrsha-Astroc As Tech",
    author_email="info@astrocastech.in",
    description="GPS-denied navigation system for autonomous drones using computer vision and sensor fusion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hrsha/GPS-Denied-Navigation-SLAM-and-Visual-Odometry-for-Autonomous-Systems--Astroc-As-Tech",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: System :: Hardware :: Hardware Drivers",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "pytest-cov>=2.12.0",
            "black>=21.6.0",
            "flake8>=3.9.0",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=0.5.0",
        ],
        "gpu": [
            "torch>=1.9.0+cu111",
            "torchvision>=0.10.0+cu111",
        ],
        "rpi": [
            "RPi.GPIO>=0.7.0",
            "adafruit-circuitpython-bno055>=5.0.0",
            "adafruit-circuitpython-motor>=3.4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "drone-nav=src.navigation.main:main",
            "calibrate-sensors=scripts.calibrate_sensors:main",
            "run-simulation=scripts.run_simulation:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.yaml", "*.yml", "*.json", "*.txt"],
    },
    zip_safe=False,
    keywords="drone navigation GPS-denied computer-vision SLAM sensor-fusion autonomous-flight",
    project_urls={
        "Bug Reports": "https://github.com/YOUR-USERNAME/gps-denied-drone-navigation/issues",
        "Source": "https://github.com/YOUR-USERNAME/gps-denied-drone-navigation",
        "Documentation": "https://your-username.github.io/gps-denied-drone-navigation/",
    },
)

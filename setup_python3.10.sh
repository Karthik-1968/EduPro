#!/bin/bash

# Update the package lists for the repositories
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install build-essential and other required libraries
echo "Installing essential build tools..."
sudo apt install -y build-essential

# Install libraries for Python development
echo "Installing Python development libraries..."
sudo apt install -y libssl-dev libffi-dev python3-dev

# Install additional dependencies for Python
echo "Installing additional dependencies..."
sudo apt install -y zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev

# Add the deadsnakes PPA repository for newer Python versions
echo "Adding deadsnakes PPA repository..."
sudo add-apt-repository ppa:deadsnakes/ppa

# Update the package lists again after adding the repository
echo "Updating package lists again..."
sudo apt update

# Install Python 3.10
echo "Installing Python 3.10..."
sudo apt install -y python3.10

# Install distutils for Python 3.10 (for pip installation)
echo "Installing Python 3.10 distutils..."
sudo apt install -y python3.10-distutils

# Download and install pip for Python 3.10
echo "Downloading and installing pip..."
wget https://bootstrap.pypa.io/get-pip.py
python3.10 get-pip.py

# Set Python 3.10 as the default version
echo "Setting Python 3.10 as the default Python version..."
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

# Configure the default python3 version
echo "Configuring the default Python 3 version..."
sudo update-alternatives --config python3

# Clean up the downloaded get-pip.py file
echo "Cleaning up..."
rm get-pip.py

# Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv env

# Activate the virtual environment
echo "Activating the virtual environment..."
source env/bin/activate

echo "Python 3.10 and pip installation complete. Virtual environment activated."

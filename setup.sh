#!/bin/bash

# Check if script is run as root
if [[ $EUID -ne 0 ]]; then
   echo -e "\e[91mThis script must be run as root.\e[0m" 
   exit 1
fi

# Install required Python libraries
echo -e "\e[96mInstalling required Python libraries...\e[0m"
pip3 install prettytable colorama 2>&1 | tee /tmp/library_install.log

# Check if there were any installation errors
if grep -q "error" /tmp/library_install.log; then
    echo -e "\e[91mInstallation failed. Trying with apt-get...\e[0m"
    apt-get update
    apt-get install python3-prettytable python3-colorama 2>&1 | tee /tmp/library_install.log
    if grep -q "error" /tmp/library_install.log; then
        echo -e "\e[91mInstallation failed. Please check the log file /tmp/library_install.log for details.\e[0m"
        exit 1
    else
        echo -e "\e[92mInstallation successful using apt-get.\e[0m"
    fi
else
    echo -e "\e[92mInstallation successful using pip3.\e[0m"
fi

# Remove the temporary log file
rm /tmp/library_install.log

# **Room Allocation System**

This is a Python script that allocates rooms to teams randomly from a list of available rooms, and saves the allocations to a CSV file. It also generates a list of unallocated rooms and saves it to another CSV file.

## **Requirements**

- Python 3.6 or higher

-  colorama==0.4.4

-  prettytable==2.2.1

## **Installation**

Clone the repository or download the source code.
Open the command prompt or terminal and navigate to the root folder of the project.
Run the following command to install the required dependencies:
```bash
pip install -r requirements.txt
```
Run the setup.sh script to generate the team and room data files.
```
sudo ./setup.sh
```
## **Usage**

1.  To allocate rooms to teams and save the allocations to a CSV file,
    run the following command:
```
python allocate_rooms.py
```
The script will print the allocations on the console and save them to a
file named allocated_rooms.csv.

2.  To generate a list of unallocated rooms and save it to a CSV file,
    run the following command:
```
python allocate_rooms.py
```
The script will print the list on the console and save it to a file
named unallocated_rooms.csv.

3.  To lookup a team's allocation, run the following command and enter
    the team ID when prompted:
```
python check_allocations.py
```
The script will print the team's allocation on the console.

## **Files**

**teams.txt**: Contains the list of teams in the format team_id
team_name.

**rooms.txt**: Contains the list of available rooms, with each room
number on a separate line.

**allocated_rooms.csv**: Contains the team allocations, with columns
Team ID, Team Name, and Room Number.

**unallocated_rooms.csv**: Contains the list of unallocated rooms, with
a single column Room Number.

**allocate_rooms.py**: The script that allocates rooms to teams and
saves the allocations to a CSV file.

**check_allocations.py**: The script that allows the user to lookup a
team's allocation.

**setup.sh**: The script that generates the teams.txt and rooms.txt
files.

## **Credits**

This project was created by whitedevil.

import random
import csv
from prettytable import PrettyTable

# read team names from file
try:
    with open('teams.txt', 'r') as f:
        team_data = f.readlines()
except FileNotFoundError:
    print("Error: teams.txt file not found.")
    exit()

# extract team ids and names
team_names = []
for data in team_data:
    team_id, team_name = data.split(maxsplit=1)
    team_names.append((team_id, team_name.strip()))

# read room numbers from file
try:
    with open('rooms.txt', 'r') as f:
        all_rooms = set(map(str.strip, f.readlines()))
except FileNotFoundError:
    print("Error: rooms.txt file not found.")
    exit()

# shuffle team names
random.shuffle(team_names)

allocated_rooms = set()
room_allocations = {}
for team_id, team_name in team_names:
    room_number = None
    for i in all_rooms:
        if i not in allocated_rooms:
            room_number = i
            allocated_rooms.add(i)
            break
    if room_number is None:
        print("Error: not enough rooms available for all teams.")
        exit()
    room_allocations[team_id] = (team_name, room_number)

# write allocated room allocations to CSV file
try:
    with open('allocated_rooms.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Team ID", "Team Name", "Room Number"])
        for team_id, (team_name, room_number) in room_allocations.items():
            writer.writerow([team_id, team_name, room_number])
    print("Allocated room allocations saved to allocated_rooms.csv")
except IOError:
    print("Error: unable to write to allocated_rooms.csv file.")
    exit()

# find unallocated rooms
unallocated_rooms = all_rooms - allocated_rooms
unallocated_room_numbers = list(unallocated_rooms)

# write unallocated rooms to CSV file
if unallocated_room_numbers:
    try:
        with open('unallocated_rooms.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Room Number'])
            for room in unallocated_room_numbers:
                writer.writerow([room])
        print("Unallocated rooms saved to unallocated_rooms.csv")
    except IOError:
        print("Error: unable to write to unallocated_rooms.csv file.")
        exit()
else:
    print("All rooms allocated.")

# print allocations using prettytable
table = PrettyTable()
table.field_names = ["Team ID", "Team Name", "Room Number"]
for team_id, (team_name, room_number) in room_allocations.items():
    table.add_row([team_id, team_name, room_number])
print(table)

# print a list of unallocated rooms
if unallocated_rooms:
    print("Unallocated rooms:")
    for room in unallocated_rooms:
        print(room)
else:
    print("All rooms are allocated")



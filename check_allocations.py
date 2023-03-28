import csv
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)


print("")
print (Fore.BLUE + f"██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
print (Fore.BLUE + f"█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░████░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███")
print (Fore.BLUE + f"█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███")
print (Fore.BLUE + f"█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░░░░░░░░░█░░░░▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███")
print (Fore.BLUE + f"█░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░████░░▄▀░░███████████░░▄▀░░███░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░████░░▄▀░░███")
print (Fore.BLUE + f"█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░████░░▄▀░░░░░░░░░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███")
print (Fore.BLUE + f"█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███")
print (Fore.BLUE + f"█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░████░░▄▀░░░░░░░░░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███")
print (Fore.BLUE + f"█░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░████░░▄▀░░███████████░░▄▀░░███░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████")
print (Fore.BLUE + f"█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██████████░░▄▀░░████░░▄▀░░█████████░░░░▄▀░░░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█")
print (Fore.BLUE + f"█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░████░░▄▀░░█████████░░▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█")
print (Fore.BLUE + f"█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░████░░░░░░█████████░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█")
print (Fore.BLUE + f"██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
print ("")
print (Fore.RED + f"---------------------------------------------------------c̶o̶d̶e̶d̶ b̶y̶ w̶h̶i̶t̶e̶d̶e̶v̶i̶l̶--------------------------------------------------------------------------------------------------")


unallocated_rooms_file = 'unallocated_rooms.csv'
allocated_rooms_file = 'allocated_rooms.csv'

unallocated_rooms = []
with open(unallocated_rooms_file) as f:
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    for row in reader:
        if row:
            room_number = int(row[0])
            unallocated_rooms.append(room_number)

print(Fore.YELLOW + f"Unallocated rooms from {unallocated_rooms_file}: " + Fore.GREEN + f"{unallocated_rooms}")

allocated_rooms = []
with open(allocated_rooms_file) as f:
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    allocated_rooms = [int(row[0]) for row in reader if row and row[1]]

#print(Fore.YELLOW + f"Remaining unallocated rooms from {allocated_rooms_file}: " + Fore.GREEN + f"{allocated_rooms}")

def get_team_info(team_id):
    with open(allocated_rooms_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row['Team ID']) == team_id:
                team_name = row['Team Name']
                room_number = row['Room Number'] or 'unallocated'
                return team_name, room_number
    return None, None

while True:
    team_id = input("Enter team ID (or 000 to quit): ")
    if team_id == '000':
        break
    try:
        team_id = int(team_id)
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a numeric team ID.")
        continue
    team_name, room_number = get_team_info(team_id)
    if team_name:
        print(Fore.YELLOW + f"Team {team_name} ({team_id}) is in room " + Fore.GREEN + f"{room_number}")
    else:
        print(Fore.RED + f"Team {team_id} not found")


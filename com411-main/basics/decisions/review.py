# Ask Beep for the direction
print("Towards which direction should I go (up, down, left or right)?")
direction = input()

# Determine which message to display
if direction == "up":
    print("I am going in the upward direction!")
elif direction == "down":
    print("I am going in the downward direction!")
elif direction == "left":
    print("I am going in the leftward direction!")
elif direction == "right":
    print("I am going in the rightward direction!")
else:
    print("Not sure which direction I am going in!")

# Ask Beep for battery details
print("What type of battery do you have Beep?")
battery_type = input()

# Display appropriate message
if battery_type == "nuclear":
    print("Is the nuclear battery working fine?")
    nuclear_battery = input()

    if nuclear_battery == "yes":
        print("That's great! You should still have energy for 10 more years!")
    else:
        print("That's not good! You might need a battery replacement!")
else:
    print("Lithium Ion batteries need to be recharged or you will turn off!")

# Ask Beep for the type of arm upgrade he wants
print("What type of arm upgrade should I get?")
arm_upgrade = input()

# Determine what message to display
if (arm_upgrade == "Metal") or (arm_upgrade == "Cheap"):
    print("Machine upgrading your arm to a brand new metal arm!")
elif (arm_upgrade == "Titanium") or (arm_upgrade == "Expensive"):
    print("Machine upgrading your arm to a brand new titanium arm!")
else:
    print("No arm upgrade wanted.")

# Ask Beep for what he has seen and heard
print("What have you heard?")
hear = input()

print("What have you seen?")
see = input()

# Determine what message to display
if (hear == "machinery") and (see == "upgrade machine"):
    print("There was an upgrade machine and I upgraded my robot parts!")
else:
    print("I haven't done anything, it's all the same as before.")
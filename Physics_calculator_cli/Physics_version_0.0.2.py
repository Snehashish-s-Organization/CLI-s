# Made By Snehashish Laskar
# Made on 06-03-2021
# This can be used to calculate usefull things using physics formulae
# This can be used By teachers if they want to correct the exam pappers easily and without doing any calculations!
'''
	Instructions:
	-> Please follow the notes written below for help!
	-> Please do not enter the Units of the numbers below!
'''


def validcommands():
    print("Here are all all the valid commands with their functions:")
    print("type b bellow to calculate acceleration from force and mass:")
    print("type c bellow to calculate acceleration from velocity and time: ")
    print("type d bellow to calculate average speed:")
    print("type e bellow to calculate momentum: ")
    print("type f bellow to calculate distance from speed and time: ")
    print("type g bellow to calculate distance from acceleration and time: ")
    print("type h bellow to calculate impulse: ")


def calculate_acceleration_with_force():

    # it can be used to calculate acceleration from net force and mass
    force = int(input("Please enter the net force acting on the object: "))
    mass = int(input("please enter the mass of the object:  "))
    equation1 = force/mass
    print(f"The acceleratin is equal to : {equation1} m/s squared")


def calculate_acceleration_with_velocity():
    # Please give the velocity in m/s
    # This can be used to calculate the acceleration from change in velocity and time intervals
    velocity = int(input("Please enter the change in verlocity:  "))
    time = int(input("Please enter the time:  "))
    equation2 = velocity/time
    print(f"acceleration is equal to {equation2} m/s squared")


def calculate_avg_speed():
    # Please give the distance in meters only
    # This can be used to calculate average speed from toatl distamce and time
    distance = int(input("Please enter the distance traveled:  "))
    time = int(input("please enter the time:  "))
    equation3 = distance/time
    print(f" the average speed is equal to {equation3}m/s ")


def calculate_momentum():
    # Please give mass on Kg's only!
    # this Function can be used to calaculate the momentum of an object from its velocity and mass!
    mass = int(input("please enter the mass of the object:  "))
    velocity = int(input("please enter the velocity of the object:  "))
    equation4 = mass*velocity
    print(f"The momentum of this object is {equation4} kg m/s")


def calculate_distance():
    # Please give speed in m/s only!
    # This Function can be used to calculate the distance from Average speed and time
    avg_speed = int(input("Please enter the average speed of the object:  "))
    time = int(input("Please enter the time period:  "))
    equation5 = avg_speed*time
    print(f"disctance covered is equal to {equation5}m")


def calculate_distance_from_acceleration():
    # Please give the acceleration in m/s
    # This Function can be used to calculate the distance from acceleration and time
    acceleration = int(
        input("Please enter the average acceleration of the object:  "))
    time = int(input("Please enter the time period:  "))
    equation6 = (acceleration*(time*time))/2
    print(f"disctance covered is equal to {equation6}m ")


def calculate_impulse():
    # This function can be used to calculate the impulse applied on an object
    force = int(input("Please enter the force acting on the object:  "))
    time = int(input("Please eneter the time period:  "))
    equation7 = force*time
    print(f"Impulse is equal to {equation7}N ")


while True:
    print("type a bellow to view all the valid commands press q to quit: ")
    in1 = input()
    if in1 == "a":
        validcommands()

    elif in1 == "q":
        exit()

    elif in1 == "b":
        calculate_acceleration_with_force()

    elif in1 == "c":
        calculate_acceleration_with_velocity()

    elif in1 == "d":
        calculate_avg_speed()

    elif in1 == "e":
        calculate_momentum()

    elif in1 == "f":
        calculate_distance()

    elif in1 == "g":
        calculate_distance_from_acceleration()

    elif in1 == "h":
        calculate_impulse()

    else:
        pass

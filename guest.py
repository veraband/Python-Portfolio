#vera
#Arrays
#guest.py

#init
#functions
#challange 1.1
def guests():
    guests = [
    "Alice", "Bob", "Charlie", "David", "Eve",
    "Frank", "Grace", "Heidi", "Ivan", "Judy",
    "Kevin", "Liam", "Mallory", "Nia", "Oscar",
    "Peggy", "Quinn", "Riley", "Sybil", "Trent",
    "Uma", "Victor", "Walter", "Xander", "Yara",
    "Zane", "Amari", "Blake", "Casey", "Dakota"
    ]
    #challange 1.1
    who = input("What is you friend's name, Bob? ")
    guests.append(who)
    print(guests)
    #challange 1.2
    vip = input("What is the name of the VIP guest? ")
    guests.insert(0, vip)
    print(guests)
    #challange 1.3
    david = input("I'm sorry to hear you can't make it! Who would you like to go in your place? ")
    guests[4] = david
    print(guests)
    #challange 1.4
    attending = len(guests)
    print(attending)
#main
guests()

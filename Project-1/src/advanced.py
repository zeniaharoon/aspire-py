#TODO: Add your header here!

#TODO: For test1, figure out how to import your Avenger class from intermediate.py

"""
TEST 1
Now that you are familiar with classes, we are going to work with inheritance

Inheritance basically is a fancy way for our classes to relate to each other,
and in theory reduce the amount of code we need to write

We are going to implement a sub-class of the Avenger class we wrote in intermediate.py

Below, implement class, BlackPanther, which inherits from Avenger.

Make sure of these things:
- Make its own `init` function so that it gets instantiated correctly
    - This function should have all the same parameters as Avenger
- Use the `super` keyword to instantiate all the fields efficiently
    - DO NOT JUST COPY INIT FROM AVENGER

Additionally, lets have a special field just for T'Challa:
- vibranium: (boolean)    initialized to True
"""

#TODO: Add functionality here

    #TODO: Add functionality here
    """
    TEST 2

    Remember that function we made in `Avenger` that was not implemented?

    Often times we can make parents classes have unimplemented methods like this
    In python these are the closest things to **interfaces**

    Implement black panthers `special_power` method

    This function will maximize his agility and power stats to .99 at the cost of 
    depleting his health by 10

    NOTE: This is an example of an **override**
    """

    #TODO: Add functionality here
    """
    TEST 3
    
    Lets dig a little more into overriding, this happens when we 
    implement a function of our parent and change the behavior of that function.
    Something to note is that generally for it to be an override, the function signature
    has to be the exact same. Otherwise it may be an **overload**
    Python is hardly a real programming language so these concepts are muddied
    and overloading doesnt really exist...

    Lets override the attacked() function for T'Challa
    If you can recall from the movies, Black Panthers super suit
    can take kinetic impacts and repel them out to attack his enemies

    To implement this behavior into attacked(), lets override it

    attacked should now behave as follows:
    - Keep all of the code from intermediate.py where we dice roll for an agility% chance
    - Now instead of only returning a bool for dead, return a tuple where the first element
      is a bool for whether he is dead, but the second is a float which will be 
      50% of the damage that T'Challa was dealt. We can use this information to 
      deal damage back to the attacker, thus simulating the kinetic properties of his suit
    """

#TODO: Add functionality here
"""
TEST 4-5
    
Now that you have gotten the hang of creating sub-classes,
lets create a few more Avengers.

Below create an IronMan and Hulk class that follow the specification

IronMan:
- Should inherit from Avenger (follow practices from BlackPanther)
- Has an extra field
    - fuel: (int) In between 0 and 100, initialized to 100
- special_power
    - Checks if fuel greater than 70
    - If it is, should deplete fuel by 70, and return a random float between 40-60 for damage
    - If fuel less than 70, return -1
    
    
Hulk:
- Should inherit from Avenger (follow practices from BlackPanther)
- Has an extra field
    - hulked_out: (bool) default to True
- special_power
    - Checks hulked_out is True
    - If it is, should set hulked_out to False and return string "HULK SMASH"
    - If hulked_out False, set to True and return the string "I'm always angry"
"""

"""
TEST 6

Now that we have created a few classes in our ecosystem,
lets learn about class attributes that don't change and 
are persistant for every class instantiated

Sometimes we want to embed some metadata about our classes
that are independent to each individual instance. In that case
we can implement a class attribute.

For the Avenger class, implement a class attribute called
`_total_avengers`. It should increment by one every time a new avenger
is instantiated.
NOTE: Notice how we prefix this variable with an underscore, this is python's
attempt at private variables that we don't want everyone to see

In addition: Create two helper methods along with this attribute in the Avenger class
These are common methods used in Object Oriented Programming called "getters" and "setters"

get_total_avengers(): return the total number of avengers
set_total_avengers(x): take one argument and set the total number of avengers to that
reset_total_avengers(): reset the total number of avengers to 0

NOTE: The getter and setter methods here should be **class methods**
You will need to use the `@classmethod` decorator to denote that, and ensure
that the first argument is `cls` not `self`!
"""

# =================================================================================================
# DO NOT EDIT ANY CODE BELOW THIS LINE: Would be cheating...
# =================================================================================================
    """
    ===============================================
    STOP HERE! DO NOT EDIT ANY CODE BELOW THE T-REX
    ===============================================
                              _.-.
                             /  99\
                            (      `\
                            |\\ ,  ,|
                    __      | \\____/
              ,.--"`-.".   /   `---'
          _.-'          '-/      |
      _.-"   |   '-.             |_/_
,__.-'  _,.--\      \      ((    /-\
',_..--'      `\     \      \\_ /
                `-,   )      |\' 
                  |   |-.,,-" (  
                  |   |   `\   `',_
                  )    \    \,(\(\-'
              jgs \     `-,_
                   \_(\-(\`-`
                      "  "

    """
def check_input():
    while True:
        x = input("Be honest...[Yes/No]")
        if x.lower() == "yes": return True
        elif x.lower() == "no": return False
        else: print("Enter Yes or No")

def test1():
    try:
        bp = BlackPanther("Black Panther", "T'Challa", 80.5, .75, .99, level=2)
        assert issubclass(BlackPanther, Avenger)
        assert bp.vibranium_level
        return True
    except:
        return False

def test2():
    try:
        bp = BlackPanther("Black Panther", "T'Challa", 80.5, .75, .9, level=2)
        bp.special_power()
        assert bp.health == 80.5-10
        assert bp.power == .99
        assert bp.agility == .99
    except:
        return False

def test3():
    try:
        bp = BlackPanther("Black Panther", "T'Challa", 80.5, .75, 1, level=2)
        dead, recoil = bp.attacked(25)
        assert bp.health == 80.5 - 25
        assert not dead
        assert recoil == (25 / 2)
    except:
        return False

def test4():
    try:
        iron_man = IronMan("Iron Man", "Tony Stark", 50, .33, 1)
        assert issubclass(iron_man, Avenger)
        assert iron_man.fuel == 100
        damage = iron_man.special_power()
        assert iron_man.fuel == 30
        assert damage >= 40 and damage <= 60
        damage = iron_man.special_power()
        assert damage == -1
    except:
        return False

def test5():
    try:
        hulk = Hulk("Hulk", "Bruce Banner", 250, .33, 1)
        assert issubclass(hulk, Avenger)
        assert hulk.hulked_out
        quote = hulk.special_power()
        assert quote == "HULK SMASH"
        assert not hulk.hulked_out
        quote = hulk.special_power()
        assert quote == "I'm always angry"
        assert hulk.hulked_out
    except:
        return False

def test6():
    try:
        hulk = Hulk("Hulk", "Bruce Banner", 250, .33, 1)
        hulk.reset_total_avengers()
        assert hulk.get_total_avengers() == 3
        bp = BlackPanther("Black Panther", "T'Challa", 80.5, .75, 1, level=2)
        hulk2 = Hulk("Hulk", "Bruce Banner", 250, .33, 1)
        iron_man = IronMan("Iron Man", "Tony Stark", 50, .33, 1)
        assert iron_man.get_total_avengers() == 3
        assert bp.get_total_avengers() == 3
        assert hulk2.get_total_avengers() == 3
        hulk.set_total_avengers(6)
        assert iron_man.get_total_avengers() == 6
    except:
        return False

import rsa
import time
if __name__=="__main__":
    print("Running tests...")
    assert test1(), "❌❌❌ Test 1 Failed..."
    print("🍎🍎🍎 Test 1 Passed!")
    time.sleep(0.5)
    assert test2(), "❌❌❌ Test 2 Failed..."
    print("🍎🍎🍎 Test 2 Passed!")
    time.sleep(0.5)
    assert test3(), "❌❌❌ Test 3 Failed..."
    print("🍎🍎🍎 Test 3 Passed!")
    time.sleep(0.5)
    assert test4(), "❌❌❌ Test 4 Failed..."
    print("🍎🍎🍎 Test 4 Passed!")
    time.sleep(0.5)
    assert test5(), "❌❌❌ Test 5 Failed..."
    print("🍎🍎🍎 Test 5 Passed!")
    time.sleep(0.5)

    print("Congrats!!! You have unlocked the secret code")
    print("Loading Secret...")
    time.sleep(2)
    with open('secret_sauce/private.pem', mode='rb') as privatefile:
        privkeydata = privatefile.read()
    with open('secret_sauce/public.pem', mode='rb') as publicfile:
        pubkeydata = publicfile.read()
    privateKey = rsa.PrivateKey.load_pkcs1(privkeydata)
    publicKey = rsa.PublicKey.load_pkcs1_openssl_pem(pubkeydata)
    with open("secret_sauce/secret_message3.txt", "rb") as msg:
        secret = msg.read()
    decMessage = rsa.decrypt(secret, privateKey).decode()
    print("SECRET MESSAGE: ", decMessage)
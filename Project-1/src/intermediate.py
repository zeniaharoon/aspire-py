#TODO: Add your header here!

'''
Author: Zenia Haroon

Date: 7/9/23

Description: Learning OOP and classes in python. Created an Avengers class
'''

#TODO: For test2, something goes here...

import random

def uh_oh(integer, float, string, boolean, list, dictionary):
    """
    This test you are going to learn about errors and exception handling

    Consider the following:

    Often times in code, our program will crash because we didnt make it robust
    We saw in basic.py that it was fairly easy to ensure simple things like
    enforcing a parameter to be an integer. But what about other cases where
    that doesnt work?

    For another case, maybe we know and expect our code to fail in a certain location.
    Given that we know this information, we maybe want to do some specific actions before 
    our program quits, or even let it continue on!

    This is where try-except blocks come into play. If you need an example of how these work,
    feel free to browse the evaluation section at the bottom of this file (No modifications though)
    ===============================================================================================
    How to complete:

    This function will take in 6 parameters representing fundamental data types/structures:
    integer,
    float,
    string,
    boolean,
    list,
    dictionary
     
    I have implemented some code below that you are not to modify.

    Create a try-except block around that code to handle the errors that will arise.

    - When i try adding mismatched types, return the string "apple"
    - Division by zero returns "banana"
    - Attribute errors return "corn"
    - Index out of range returns "donut"
    - Key errors return "eggplant"
    """
    #TODO: Add functionality here
    '''    
    try:
        fail1 = integer + string
    except:
        return "apple"

    try:
        fail2 = float / boolean
    except:
        return "banana"

    try: 
        dictionary["I do not exist"]
    except:
        return "corn"

    try: 
        fail4 = list[3]
    except:
        return "donut"

    try: 
        fail5 = list.aye_im_walking_ere()
    except:
        return "eggplant"
    '''

    try:
        fail1 = integer + string
        fail2 = float/boolean
        fail3 = dictionary["I do not exist"]
        fail4 = list[3]
        fail5 = list.aye_im_walking_ere()
    except TypeError:
        return "apple"
    except ZeroDivisionError:
        return "banana"
    except KeyError:
        return "corn"
    except IndexError:
        return "donut"
    except AttributeError:
        return "eggplant"


  
class Avenger:
    """
    This is a class, we use this to group data together into structures that make semantic sense
    Take note on a few things:
        - The syntax for this particular class takes no arguments, unlike a function
        - The naming convention for classes is CapCase, always a capital letter to start each word
        - In computer science, we generally refer to classes as "objects"
            - In python, technically everything is an "object"

    Test 1:
    We are going to code an Avengers video game...
    Write a constructor for the Avenger class that aligns to following documentation below:

    NOTE:   For all bounded values, if the number passed in is above a boundary, set it to the max.
            if the number passed is below a boundary set it to min.
            Special exception for health, if it is below 0, automatically set to 100
            ex: if between 0-1, and number passed 30, set to 1

    Parameters:
    self:                           Reference to the object itself
    name:               (String)    The superhero name
    secret_identity:    (String)    The true identity
    health:             (Float)     (Non-negative) The amount of health this hero has to begin with
    power:              (Float)     (Between 0-1) How powerful this character is
    agility:            (Float)     (Between 0-1) How fast the character can move (dodge attacks)
    level:              (int)       (Non-negative) Level progression, should initialize to 1
                                    SPECIFY A DEFAULT VALUE = 1 FOR THIS PARAMETER ^

    Member Fields:
    name:               (String)    The superhero name
    secret_identity:    (String)    The true identity
    health:             (Float)     (Non-negative) The amount of health this hero has to begin with
    power:              (Float)     (Between 0-1) How powerful this character is
    agility:            (Float)     (Between 0-1) How fast the character can move (dodge attacks)
    level:              (int)       (Non-negative) Level progression, should initialize to 1
    exp:                (int)       (Between 0-100) Experience points, initialize to 0
    
    Returns:
    None
    """


    #TODO: Add functionality here
 
    def __init__ (self, name, secret_identity, health, power, agility, level = 1):
        self.name = str(name)
        self.secret_identity = str(secret_identity)
        self.health = float(max(0, abs(health)))
        self.power = float(max(0, min(1, power)))
        self.agility = float(max(0, min(1, agility)))
        self.level = int(max(0, level))
        self.exp = 0 

# =================================================================================================
    # Tests 2-5

    # Now that we have written the constructor for our class, lets implement some functionality
  

 # Write the following functions according to the documentation...
# =================================================================================================
    #TODO: Add functionality here
    """
    attacked()

    Should take in a parameter that will inflict damage, decreasing overall health
    However...
    Depending on the agility member field, there will be an agility% change that the attack misses
    and does no damage. HINT: use the numpy package and its random number capabilities...

    If the damage dealt is greater than the health remaining, the health should be zero
    Health should never be negative!

    Parameters:
    self
    damage

    Returns:
    dead      (boolean)   True if health below zero, else False
    """

    #TODO: Add functionality here
    def attacked (self, damage):
        rand = random.random()
        if self.agility < rand:
            if damage >= self.health:
                self.health = 0
                #print(self.health)
                return True
            else:
                self.health -= damage
                #print(self.health)
                return False
        return False
    
    """
    restore_health()

    Should take one parameter that will restore health to max value

    You will need to add another member field to the Avenger class
    to keep track of the max health originally set such that you cannot go over it

    ex: iron_man initialized with 100 health and then takes 20 damage. If 
    restore_health(50) is called, iron_man should be at 100 health not 130

    Parameters:
    self,
    restoration

    Returns:
    None
    """

    #TODO: Add functionality here

    def restore_health(self, restoration):
        if self.health <= 100:
            self.health = self.health + restoration
            if self.health > 100:
                self.health = 100
        else:
            self.health = 100    

    """
    reset()

    Takes no parameters, simply resets health back to max health

    Parameters:
    Nothing

    Returns:
    None
    """

    #TODO: Add functionality here

    def reset(self):
        self.health = 100

    """
    special_power()

    This will be what known as an "abstract method"

    For the avenger class, we will not actually write any running code in the body of this method
    it will be used later for inheritence

    When this method is called directly, it should "raise" a "NotImplementedError"

    Parameters:
    None

    Returns:
    None
    """ 
    def special_power(self):
        raise NotImplementedError

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

import rsa
import time

def test0():
    class l:
        def aye_im_walkin_ere(): pass

    d = {"I do not exist": False}
    try: 
        assert uh_oh(5, 3.3, "hello", True, l, d) == "apple"
        print("Success")
        assert uh_oh(5, 3.3, 3, False, l, d) == "banana"
        print("Success")
        assert uh_oh(5, 3.3, 3, True, l, {}) == "corn"
        print("Success")
        assert uh_oh(5, 3.3, 3, True, [], d) == "donut"
        print("Success")
        assert uh_oh(5, 3.3, 3, True, [1,2,3,4,5], d) == "eggplant"
        print("Success")
    except:
        return False
    else:
        return True

def test1():
    try:
        iron_man    = Avenger("Iron man", "Tony Stark", 100, 30, 20)
        assert hasattr(iron_man,"name")
        assert hasattr(iron_man,"secret_identity")
        assert hasattr(iron_man,"health")
        assert hasattr(iron_man,"power")
        assert hasattr(iron_man,"agility")
        assert hasattr(iron_man,"level")
        assert hasattr(iron_man,"exp")
        assert iron_man.level == 1

        thor        = Avenger("Thor", "Thor Odinson", -100, 30, -20, level=3)
        assert thor.health == 100
        assert thor.power == 1
        assert thor.agility == 0
        assert thor.level == 3
        assert thor.exp == 0
    except:
        return False
    else:
        return True

def test2():
    try:
        iron_man    = Avenger("Iron man", "Tony Stark", 100, 0.3, 0)
        thor        = Avenger("Thor", "Thor Odinson", -100, 30, 1)
        dead = iron_man.attacked(40)
        assert dead is False
        assert iron_man.health == 60
        dead = iron_man.attacked(70)
        assert dead is True
        assert iron_man.health == 0

        dead = thor.attacked(20)
        assert dead is False
        assert thor.health == 100
    except:
        return False
    else:
        return True
    
def test3():
    try:
        iron_man    = Avenger("Iron man", "Tony Stark", 100, 0.3, 0.)
        iron_man.restore_health(50)
        assert iron_man.health == 100
        iron_man.attacked(90)
        iron_man.restore_health(30)
        assert iron_man.health == 40
    except:
        return False
    else:
        return True

def test4():
    try:
        iron_man    = Avenger("Iron man", "Tony Stark", 100, 0.3, 0.)
        iron_man.restore_health(50)
        assert iron_man.health == 100
        iron_man.attacked(90)
        iron_man.restore_health(30)
        assert iron_man.health == 40
        iron_man.reset()
        assert iron_man.health == 100
    except:
        return False
    else:
        return True

def test5():
    try:
        iron_man    = Avenger("Iron man", "Tony Stark", 100, 0.3, 0.)
        iron_man.special_power()
    except NotImplementedError:
        return True
    else:
        return False



if __name__=="__main__":
    print("Running tests...")
    assert test0(), "❌❌❌ Test 0 Failed..."
    print("😤😤😤 Test 0 Passed!")
    time.sleep(0.5)
    assert test1(), "❌❌❌ Test 1 Failed..."
    print("😤😤😤 Test 1 Passed!")
    time.sleep(0.5)
    assert test2(), "❌❌❌ Test 2 Failed..."
    print("😤😤😤 Test 2 Passed!")
    time.sleep(0.5)
    assert test3(), "❌❌❌ Test 3 Failed..."
    print("😤😤😤 Test 3 Passed!")
    time.sleep(0.5)
    assert test4(), "❌❌❌ Test 4 Failed..."
    print("😤😤😤 Test 4 Passed!")
    time.sleep(0.5)
    assert test5(), "❌❌❌ Test 5 Failed..."
    print("😤😤😤 Test 5 Passed!")

    print("Congrats!!! You have unlocked the secret code")
    print("Loading Secret...")
    time.sleep(2)
    with open('secret_sauce/private.pem', mode='rb') as privatefile:
        privkeydata = privatefile.read()
    with open('secret_sauce/public.pem', mode='rb') as publicfile:
        pubkeydata = publicfile.read()
    privateKey = rsa.PrivateKey.load_pkcs1(privkeydata)
    publicKey = rsa.PublicKey.load_pkcs1_openssl_pem(pubkeydata)
    with open("secret_sauce/secret_message2.txt", "rb") as msg:
        secret = msg.read()
    decMessage = rsa.decrypt(secret, privateKey).decode()
    print("SECRET MESSAGE: ", decMessage)

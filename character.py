import random

class Character:
    def __init__(self, username=None, userage=0, usergender=None):
        self.name = username
        self.age = userage
        self.gender = usergender
        self.prep_level = 0
        self.disguise = False
        self.employee_knowledge = False
        self.usb = False
        self.map = False
        self.fake_id = False
        self.money = random.randint(1500, 2500)
        self.fitness = 0
        self.key = False
        self.found_id = False
        self.lock_pic = False
        self.risk_level = 0


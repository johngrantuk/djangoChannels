import time
from channels import Group

def SendUpdate():
    x = 0
    while True:
        Group('compass').send({'text': "Yeah working..." + str(x)})
        time.sleep(2)
        x = x + 1
        

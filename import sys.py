import sys
import pandas as pd

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello,{}'.format(who_to_greet)
    return greeting

print(greet('Houba_'))

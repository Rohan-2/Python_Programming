# Performance calculator
from time import time
def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1} s")
    return wrapper


@performance
def long_time():
	for i in range(1000000):
		i*5
                
long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if (args[0]["valid"]):
            fn(*args, **kwargs)
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
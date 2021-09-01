from decorators import startstop

@startstop
# def startstop(func):
#     def wrapper():
#         print('Starting...')
#         func()
#         print('Finished')
#         
#     return wrapper
def roll():
    print('Rolling')


roll()

# (myenv) C:\Users\Zng-LENOVO\Desktop\Class And Function>python decor.py     
# Starting...
# Rolling
# Finished
def startstop(func):
    def wrapper():
        print('Starting...')
        func()
        print('Finished')
        
    return wrapper

```python
                                    #### Sketching #####
class CNI_WORKING():
    goal = 'CNI WORKING'
    
    def __init__(self, project_web_header, PO):
        self.header = project_web_header
        self.po = PO        
    def __str__(self):
        return f'who is the PO over this project = {self.po}{self.header}'
    
    def working_going(self):
        return True
    
    def polymorphism(self):
        return 'A'
    
    
'''
######################### Inheritance ######################### 
'''

class web_site(CNI_WORKING):
    goal = 'web_site'
    
    
    
    def __init__(self, project_web_header, PO, delivery_time):
        super().__init__(project_web_header, PO)
        self.delivery = delivery_time
    '''
    def__init__
        super()._init__
        
        THEY CAN EXCHANGE EACH OTHER
    
    def __init__(self, your_header):
        self.headers = your_header
    '''
    def __str__(self):
        return f'the header and the PO = {self.header}{self.po}{self.delivery}'
    
    def characteristic_web_site(self):
        return 'to be scraping'
    
    
    def testing(self):
        any_element_two = self.header
        print('TESTING',any_element_two)
        #return f'any_element_two = {self.header}'
    
    def get_started():
        return
    
    def polymorphism(self):
        return 'B'
    
'''
##### Coordinates #####
'''    

class coordinates(CNI_WORKING):
    goal = 'Scraping_data'
    def __init__(self, project_web_header, PO):
        self.header = project_web_header
        self.po = PO
        
    def __str__(self):
        return f'any_element_one = {self.headers}'
    def testing(self):
        any_element_two = self.headers
        print('TESTING',any_element_two)
        #return f'any_element_two = {self.headers}'
        
    def characteristic_coordinates(self):
        return 'Scraping coordinates'
    
    def get():
        return
    
    def polymorphism(self):
        return 'C'

    
class multiple_inheritance(web_site,coordinates):
    def __init__(self, project_web_header, PO, delivery_time):
        self.header = project_web_header
        self.po = PO
        self.delivery = delivery_time
        return
    
    def polymorphism(self):
        return 'D'
    
    
    
    
    
def main():
    project_web_header = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    PO = 'Daniel'
    
    delivery_time = "2/11/2021"
    
    
    x = web_site(project_web_header, PO,delivery_time)
    print(x)
    
    x.testing()
    print(x.po)
    
    
    z = multiple_inheritance('HEADER', 'DANIEL','fada')
    print(z)
    print(z.characteristic_coordinates())
    
    print(z.characteristic_web_site())
    print(''' ''')
    
    
    
    '''
    ##### Polymorphism #####
    '''
    Polymorphism_a = CNI_WORKING('element_a', 'element_aa')
    print(Polymorphism_a.polymorphism())
    
    print(''' ''')
    
    Polymorphism_b = web_site('element_b', 'element_bb','element_bbb')
    print(Polymorphism_b.polymorphism())
    
    #Polymorphism_c = 
    #Polymorphism_c = 
    

if __name__ == '__main__':
    main()
    
```

    the header and the PO = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}Daniel2/11/2021
    TESTING {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    Daniel
    the header and the PO = HEADERDANIELfada
    Scraping coordinates
    to be scraping
     
    A
     
    B
    


```python

```


```python

```


```python

```

```
                                   Single Inherintace
-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

class web_site():
    goal = 'Scraping_data'
    def __init__(self, your_header):
        self.headers = your_header
    def __str__(self):
        return f'any_element_one = {self.headers}'
    def testing(self):
        any_element_two = self.headers
        print('TESTING',any_element_two)
        #return f'any_element_two = {self.headers}'
    
    
    
    def get_started():
        return
    
def main():
    your_header = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    
    SCRAPER = web_site(your_header)
    print('Testing the class:',SCRAPER)
    SCRAPER.testing()
    
    
if __name__ == '__main__':
    main()
    
the header and the PO = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}Daniel2/11/2021
TESTING {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
Daniel
    
-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><
                                      Definition of classes
class CNI:
    def __init__(self,a,b,c):
        self.ELEMENT_A = a
        self.ELEMENT_B = b
        self.ELEMENT_C = c

class zhang(CNI):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c) # = Dog.__init__(self,a,b,c)
        self.ELEMENT_D = d
        
sammy = Samoyed('Sammy',2,10,20)
print(sammy.ELEMENT_A)
print(sammy.ELEMENT_B)
print(sammy.ELEMENT_D)


Sammy
2
20

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

```


```python
### Multiple Inherintace


class CNI_WORKING():
    goal = 'CNI WORKING'
    
    def __init__(self, project_web_header, PO):
        self.header = project_web_header
        self.po = PO        
    def __str__(self):
        return f'CNI WORKING __init__ = {self.po}{self.header}'
    
    def working_going(self):
        return True
    
    
'''
######################### Inheritance ######################### 
'''

class web_site_to_scraping(CNI_WORKING):
    goal = 'web site to scraping'
    
    
    def __init__(self, project_web_header, PO, delivery_time):
        super().__init__(project_web_header, PO)                #----> super CNI_WORKING class
        self.delivery = delivery_time
    '''
    THEY CAN EXCHANGE EACH OTHER
----------------------------------------
    def__init__
        super()._init__
----------------------------------------       
    def __init__(self, your_header):
        self.headers = your_header
    '''
    def __str__(self):
        return f'web_site_to_scraping __init__ = {self.header}{self.po}{self.delivery}'
    
    
    def characteristic_web_site_to_scraping(self):
        any_element_two = self.header
        print('characteristic_web_site_to_scraping:',any_element_two)
        return 'to be scraping'
    
    def Lasanha(self):
        return 'AVC'
    
    def get_started_A():
        return
    
    

class scraping_coordinates(CNI_WORKING):
    goal = 'scraping coordinates'
    def __init__(self, project_web_header, PO):
        self.header = project_web_header
        self.po = PO
        
    def __str__(self):
        return f'scraping_coordinates __init__ = {self.header}{self.po}'
    
    
    def scraping_coordinates_to_scraping(self):
        any_element_two = self.header
        print('scraping_coordinates_to_scraping:',any_element_two)
        return 'Scraping coordinates'
    
    def Mousse(self):
        return 'diabeticos'
        
    
    def get_B():
        return

'''
######################### Multiple Inheritance ######################### 
'''

class multiple_inheritance(web_site_to_scraping, scraping_coordinates):
    def __init__(self, project_web_header, PO, delivery_time):
        self.header = project_web_header
        self.po = PO
        self.delivery = delivery_time
        return

'''
########################################################################
'''    

    
    
def main():
    project_web_header = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    PO = 'Daniel'
    delivery_time = "2/11/2021"
    
    
    
    primary = web_site_to_scraping(project_web_header, PO, delivery_time)
    print(''' ''')
    
    print(primary)
    print(''' ''')
    
    print(primary.characteristic_web_site_to_scraping())
    print(''' ''')
    
    

    secondary = scraping_coordinates(project_web_header, PO)
    print(''' ''')
    
    print(secondary)
    print(''' ''')
    
    print(secondary.scraping_coordinates_to_scraping())
    print(''' ''')    
    
    multiple = multiple_inheritance('dados_A', 'dados_B', 'dados_C')
    print(multiple.Lasanha())
    
    print(multiple.Mousse())


if __name__ == '__main__':
    main()
```

     
    web_site_to_scraping __init__ = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}Daniel2/11/2021
     
    characteristic_web_site_to_scraping: {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    to be scraping
     
     
    scraping_coordinates __init__ = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}Daniel
     
    scraping_coordinates_to_scraping: {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    Scraping coordinates
     
    AVC
    diabeticos
    


```python
class Dog():
    def __init__(self,a,b,c):
        self.ELEMENT_A = a
        self.ELEMENT_B = b
        self.ELEMENT_C = c

class Samoyed(Dog):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c) # = Dog.__init__(self,a,b,c)
        self.ELEMENT_D = d

sammy = Samoyed('Sammy',2,10,20)
print(sammy.ELEMENT_A)
print(sammy.ELEMENT_B)
print(sammy.ELEMENT_D)
```

    Sammy
    2
    20
    


```python

```

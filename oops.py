#oops concept:
# 1.creating class:
class class_name():
    pass
object_name=class_name()
print(object_name);

# 2.creating class with function:
#self is not a keyword but used as first parameter:
class class_name():
    def function_name(self):
        print("hello")
object_name=class_name()
#now we access the function in class by object & function name
object_name.function_name()

# 3(a).using (-init-) initial function(method):
class class_name():
    def __init__(self,name): #instance method
        self.name=name
    def function_name(self): #local method
        print("hello", self.name)
object_name=class_name("mani")
object_name.function_name()

#3(b)or use another form of above program is:
class class_name():
    def __init__(self,name):
        self.name=name
        name='john'
        print(name)
    def function_name(self):
        print('hello',self.name)
object_name=class_name('mobi')
object_name.function_name()

#3(c)one another form of above
class class_name():
    def __init__(self,name):
        self.name=name
        name='jack'
        print(name)
    def function_name(self):
        print('hello',self.name)
class_name('magi').function_name()

#4 class variable & instance variable:
class aquest():
    jail='centraljail'
    def __init__(self,aquest_name,age):
        self.aquest_name=aquest_name
        self.age=age
    def dispaly(self):
        print('aquest name: ',self.aquest_name)
        print('aquest age: ',self.age)
        print('jail: ',aquest.jail)
#calling functions
aquest1=aquest(str(input('enter the name; ')),int(input('enter the age: ')))
aquest1.dispaly()
aquest2=aquest(str(input('enter the name; ')),int(input('enter the age: ')))
aquest2.dispaly()

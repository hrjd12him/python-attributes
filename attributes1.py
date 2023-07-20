'''here we have a class name student'''
class student:
    pass
'''the class is empty
and its objects are s1,s2,s3'''
s1=student()
s2=student()
s3=student()

'''they have an attributes name,cast, qualification and so on'''
s1.name = "himanshu jain"
s1.cast = 'SC'
s1.qualification = '12th'

s2.age = 23

s3.name = "harsh jain"
s3.age = 25
'''we are going tp discus about __dict__, hasattr(), getattr(), delattr()'''
print(s1.name)
print(s2.age)
print(s3.name)
print(s1.__dict__)
print(s3.__dict__)
print(getattr(s1,"name"))
print(getattr(s2,"age"))
print(hasattr(s1,"name"))
print(hasattr(s2,"name"))
s2 = getattr(s2,"name","harshit jain")
print(hasattr(s2,"name"))
print(delattr(s1,"name"))

'''This will throw an error because roll_no does not exist in s1 '''
print(delattr(s1 , "roll_no"))
print(s1.__dict__)
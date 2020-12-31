import maincode as x
import threading as th
#importing the main file("code" is the name of the file I have used) as a library 


x.create("sunanda",22)
#to create a key with key_name,value given and with no time-to-live property


x.create("src",70,3600) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


x.read("sunanda")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


x.read("src")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


x.create("sunanda",53)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it


x.modify("sunanda",53)
#it replaces the initial value of the respective key with new value 

 
x.delete("sunanda")
#it deletes the respective key and its value from the database(memory is also freed)
key="qwerty"
value=20
timeout=3600
#we can access these using multiple threads like
t1=th.Thread(target=(x.create or x.read or x.delete),args=(key,value,timeout)) #as per the operation
t1.start()
t1.join()
t2=th.Thread(target=(x.create or x.read or x.delete),args=(key,value,timeout)) #as per the operation
t2.start()
t2.join()
#and so on upto tn

#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB

#Strings:

raw_string = r"Hello\t,\n World\\d"
normal_string = "Hello\t,\n World\\d"
triple_quotes = """Hello 
World"""
print(raw_string)
print(normal_string)
print(triple_quotes)

#unicode:
#from google collab

#concatenation

my_string :str = "hello "
my_string_2 : str = "World"
my_string_4 : str = my_string + "" + my_string_2
print(my_string + my_string_2)
my_string_3= "Hello World"
my_string_4 = "Hel lo Wor ld"
my_string_5= "hel-lo wor-ld"
my_string_6 = "hello world"
print(my_string_3[-1])
print(len(my_string_3))
print(my_string_3[6:10:2])
print(my_string_3.upper())
print(my_string_3.lower())
print(my_string_4.split())
print(my_string_5.split("l"))
print(my_string_6.join(["hello world"]))

#sequece pr itration ho skte he yani loops kr skte hen
#string bhi list ki tarah he

#indexing 0 se start hote he (3 cheezen hote hen start , end & steps ye end me hamesha ek number subtract krta he)
#length 1 se start hote he



#change the input string to camel case word
#input can include any special characters liek #,$,_ etc
#eg: input "Python_test*item" should output "pythonTestItem"
import re
def snake_to_camel(word):
        #replace special characters with space in input string
        s= re.sub('[^a-zA-Z]+'," ",word)
        #split the words in string to array and change first letter to upper case
        arr = ''.join(x.capitalize() for x in s.split())
        #change first letter of output string to lower case
        camel_word =arr[0].lower()+arr[1:]
        return camel_word

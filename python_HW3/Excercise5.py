#Excercise5/Chapter6

#input string
str='X-DSPAM-Confidence:0.8475'

#slicing and find method
start = str.find(':')
end = len(str)

#extracting the portion of the string after ':' character 
number = str[start+1:end]

#converting extracted string in to floating point number
floatpoint_number = float(number)

#printing number
print(number)
print(floatpoint_number)

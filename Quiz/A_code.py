
# A1. finish the following function
def censor_string(txt, lst, char):
    txt_list = txt.split()
    for i in lst:
        if i in txt_list:
            index = txt_list.index(i)
            txt_list[index] = char*len(i)
    output = ' '.join(txt_list)
    print(output)
    return output


# test case
censor_string("Today is a Wednesday!", ["Today", "a"], "-")
censor_string("The cow jumped over the moon.", ["cow", "over"], "*")
censor_string("Why did the chicken cross the road?", ["DID", "chicken", "road"], "*")


# A2. read the contents from file message.txt and mask the the words 'Jaine' and 'Python'
file = open('message.txt','r')
content = file.read().split('\n')
file.close()
for i in range(len(content)):
    content[i] = censor_string(content[i],['Jaine','Python'],'*')
output = '\n'.join(content)
print(output)
new_file = open('encrypted_message.txt','w')
new_file.write(output)
new_file.close()

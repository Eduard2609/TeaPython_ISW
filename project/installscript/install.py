#generate a bin file with a given item from a list that includes the item
def generate_bat_file(item):
    #open the file to write
    f = open('project/bat/install.bat', 'w')
    #convert list to string
    item = ''.join(item)
    #write the item to the file
    f.write(item)
    f.write('-y'+ ' \r')
    #copy the text from command.txt to the file
    with open('project/bat/command.txt', 'r') as file:
        data = file.read()
        f.write(data+ ' \r')

    f.write(item)

    f.write('-y')

    #close the file
    f.close()

#a executable file that installs chocolatey and the item

    
#call generate_bin_file with the item 'test'
generate_bat_file('test')



#convert this long string to a list


#generate a bin file with a given item from a list that includes the item
def generate_bin_file(item):
    #open the file to write
    f = open('install.bin', 'w')
    #convert list to string
    item = ''.join(item)
    #write the item to the file
    f.write(item)
    #close the file
    f.close()

#call generate_bin_file with the item 'test'
generate_bin_file('test')

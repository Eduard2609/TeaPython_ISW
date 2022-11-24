#generate a bin file with a given item from a list that includes the item
def generate_bat_file(item):
    #open the file to write
    f = open('project/bat/install.bat', 'w')
    #convert list to string
    item = ''.join(item)
    #write the item to the file
    f.write('' + ' \r')
    f.write('$env:ChocolateyInstall="$InstallDir"' + ' \r')
    f.write('Set-ExecutionPolicy Bypass -Scope Process -Force;' + ' \r')
    f.write('iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))' + ' \r')
    f.write(item + ' \r')

    #close the file
    f.close()

#a executable file that installs chocolatey and the item

    
#call generate_bin_file with the item 'test'
generate_bat_file('test')



#convert this long string to a list


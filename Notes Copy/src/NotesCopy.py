import os
import time

print "Copying your notes..." + "\n"
print "Close this if you still want to make changes\n"
time.sleep(2)

for countdown in range(3, 0, -1):
    print "... %s" % countdown
    time.sleep(1)
    

notes_location = "/Users/dev-aozhimin/Documents/CodeDocument"
save_location = '/Users/dev-aozhimin/Documents/YouCaiSupplier.txt'           #you may change the #1Copied Notes.txt 
    

try:
    os.remove('/Users/dev-aozhimin/Documents/YouCaiSupplier.txt')            #put the same name here
    print "\nDeleting the old note...\n"
    time.sleep(1)
except:
    print "\nCopying the file...\n"
    time.sleep(1)
    



for root, dirs, files in os.walk(notes_location):

    for file in files:
        item = os.path.join(root, file)

        take_file = open(item, 'r')
        copy_file = open(save_location, 'a')
        for (lineNum, line) in enumerate(take_file):
            if lineNum > 6:
                copy_file.write(line)

        # copy_file.write("\n\n" + ("=" * 70) + "\n\n")
        take_file.close()
        copy_file.close()

print "Copy Complete"
time.sleep(1.5)
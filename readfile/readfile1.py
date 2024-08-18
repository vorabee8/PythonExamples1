# Open the file in read mode
file = open('infile.txt', 'r')

# Read the entire content of the file
content = file.read()

# Print the content
print(content)

ctr=0
print("test forloop")
# Print the lines
for line in content:
   print(line, end='')
   ctr=ctr+1

print("total=",ctr)

#ifexample

#switchexample

# Close the file
file.close()

# Let's try this again

# Open the file in read mode
file = open('infile.txt', 'r')

# Read all lines from the file
lines = file.readlines()

ctr=0

# Print the lines
for line in lines:
   print(line, end='')
   ctr=ctr+1

print("total =",ctr)

# Close the file
file.close()

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt") as names:
    names = names.readlines()

with open("./Input/Letters/starting_letter.txt","r") as letter:
    lines = letter.readlines()



for name in names:
    for line in lines:
        if "[name]" in line:
            with open(f"./Output/ReadyToSend/send-to-{name.strip()}.txt","w") as output:
                output.write(line.replace("[name]",name.strip()))
        else:
            with open(f"./Output/ReadyToSend/send-to-{name.strip()}.txt","a") as output:
                output.write(line)
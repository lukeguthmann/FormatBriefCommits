
#  seperator between components of output code 
__SEPERATOR__ = ("-" * 40)

#  displays program title on screen
def script_title():
    print(__SEPERATOR__)
    print("FORMATS COMMIT -M MESSAGES \n"
          "formats and counts characters of 'commit -m' messages")
    print(__SEPERATOR__)

# displays instructions to user
def commit_message_line():
    print("Enter a subject line with 50 characters or less.\n"
          "Insert // at end time to see character count.")
    print(__SEPERATOR__)
    
    # takes user input as for commit message
    subject_line = str(input("[Commit Message]: "))

    
    print(__SEPERATOR__)
    
    while True:
        # if user enters // at end of their input, it will activate message displaying character count
        if subject_line.endswith("//"):

            # strips the // off the end so it is not in character count
            subject_line = subject_line.strip("//")

            # output current commit character count and reinforces recommended is 50 characters
            print(f"[Character Count]:  {len(subject_line)} of recommended 50") 

            # outputs current commit message for user to see
            print(f"[Current Commmit Message]: {subject_line}")

            # allows user to continue adding to commit message, or, finishes commit by pressing ENTER key
            subject_line_2 = input("[Continue Typing] OR [Hit ENTER to Finish]")

            # if the above var subject_line_2 is empty, it activates this bool conditional and breaks loop
            if bool(subject_line_2) == False:
                break

            # if the user continues to enter in characters when at subject_line_2
            else:
                
                # this gets the current subject line, adds a space, and adds what the user just typed above
                subject_line = subject_line + " " + subject_line_2 # truncating the two
                print(__SEPERATOR__)

                #continues on the with while loop
                continue

        # if commit message is greater than recommended 50
        elif len(subject_line) > 50:
            
            # strips off the // if user entered one
            subject_line = subject_line.strip("//")

            # displays current commit character count
            print(f"[Character Count]:  {len(subject_line)} of recommended 50")

            # created the warning message for commit count > 50
            character_subject_warning = (
            f'- - - - -\n'
            f'> > > [WARNING]: your subject line is {len(subject_line)} characters of recommended 50.\n'
            f'- - - - - ')

            # printing out the subject warning above
            print(character_subject_warning)

            # output the current message for user to see to make the bottom choices easier to see
            print(f"[Current Commmit Message]: {subject_line}")
            answer = input("[1] - hit ENTER to generate commit code .\n"
                           "[2] - input 'end' to finish and get git commit code or restart.")

            # if user inputs 'end' string, it breaks out the while loop and continues on with the code
            if answer == 'end':
                break

            # if user pressed the ENTER key, the subject lines has // added to it as to activate the first if conditon
            else:
                subject_line = subject_line + "//"
                print(__SEPERATOR__)

        # similar to above if character count is > 50, but in this instance is if inital character count was < 50
        else:

            # displays commit character count
            print(f"[Character Count]: {len(subject_line)} of recommended 50")

            # displays current commit message so user can make an easier choice below
            print(f"[Current Commit Message]: {subject_line} ")

            # user choices for how to proceed with commit message
            answer = input("[1] - hit ENTER to continue commit message.\n"
                           "[2] - type 'end' to git commit code.")

            # break out of this while loop
            if answer == 'end':
                break

            # continues the while loop by add at end of subject line and activates first if statement
            else:
                subject_line = subject_line + "//"
                print(__SEPERATOR__)


    # splitting the subject line into a list. This stops spaces from being accepted into the list.
    subject_line = subject_line.split()

    # rejoinging it back into a string so no spaces in there
    subject_line = " ".join(subject_line)

    while True:
        # I am making sure that the subject line does not end with a PERIOD or a SPACE. if it does, removes them both.
        if subject_line.endswith(".") or subject_line.endswith(' '):

            # slicing the commit message as to not accept a period or a space at the end.
            subject_line = subject_line[0:-1]

        else:
            break
    print(__SEPERATOR__)
    print()

    print(__SEPERATOR__)
    
    # returning the subject line but capitlised first word
    print(f"[Final Character Count]: {len(subject_line)} of recommended 50")
    print(__SEPERATOR__)
    print(__SEPERATOR__)
    
    # makes sure that the commit message is capitalised at first word and rest are lower case
    print(f'[COPY CODE] git commit -m "{subject_line.capitalize()}"')
    print(__SEPERATOR__)

    # asking if the user wants to start again. This way they can copy and paste it and see the count
    restart = input("input 'y' to restart OR hit ENTER to end.")
    if restart == 'y':
        commit_message_line()
        
    # if user enter 'n', program closes
    else:
        print("\n\n")
        exit()

if __name__ == '__main__':
    script_title()
    commit_message_line()

"""The calendar is a CodeAcademy project to create a calendar that can be edited by the user.  It is a command line programme only (at this stage)."""

from time import strftime, sleep

USER = "John"
calendar = {}
INSTRUCTION = "To use this calendar you need to use the following keys:"
KEYS = "Use A to Add, U to Update, V to View, D to Delete, and X to quit."


def welcome():
    print("Welcome %s. This is your calendar application" % USER.title())
    print("\nThe calendar is opening ...")
    sleep(1)
    print(strftime("%A %B %d, %Y"))
    print(strftime("%H:%M:%S"))
    sleep(1)
    print("\nWhat would you like to do?")


def cal_del(k):
    print("\nDeleting %s as requested" % k)
    del calendar[k]
    sleep(1)
    print
    "It's gone"
    print
    calendar


def quit(x):
    start = False


def try_again():
    answer = input("Press Y to try again or anything else to quit: ")
    if answer.upper() == "Y":
        retry = "Y"
    else:
        retry = "N"
    return retry


def date_or_event():
    loop = True
    value = []
    while loop:
        e_or_d = input("\nDo you want to search by event, date, or cancel. Enter E, D, or C: ")
        e_or_d = e_or_d.upper()
        if e_or_d == "E":
            answer = input("\nType the event name: ")
            value = [e_or_d, answer]
            loop = False
        elif e_or_d == "D":
            answer = input("\nType the date please as MM/DD/YYYY: ")
            # insert date check function here later
            value = [e_or_d, answer]
            loop = False
        elif e_or_d == "C":
            value = [e_or_d, ""]
            loop = False
        else:
            print("\nLet's try this again")
            continue
    return value


def start_calendar():
    welcome()
    print("\n%s" % INSTRUCTION)
    start = True
    while start:
        # print("\n%s" % INSTRUCTION)
        user_choice = input("\n%s: " % KEYS)
        user_choice = user_choice.upper()
        if user_choice.upper() == "V":  # this block checks if there is anything to view or not
            if len(calendar.keys()) < 1:
                print("\nSorry, there are no events to view.")
                continue
            else:
                print(calendar)
                continue
        elif user_choice.upper() == "U":  # this elif block allows the update of an existing event
            date = input("What date (MM/DD/YYYY)?")
            update = input("Enter the update: ")
            calendar[date] = update
            print("Update complete.")
            continue
            # print calendar #test of the update process
        elif user_choice.upper() == "A":  # this block allows adding a new event if this year or in the future
            event = input("Enter event details: ")
            date = input("Enter your date (MM/DD/YYYY): ")
            if len(date)!=10:  # check if the date is improper and allow trying again
                print("\nYour date must use the format MM/DD/YYYY (e.g. Jan = 01).\n")
                if try_again() == "Y":
                    continue
                else:
                    start = False
            elif int(date[6:]) < int(strftime("%Y")):  # check if the date is this year or future
                print("\nThis calendar only accepts dates for %s and later." % strftime("%Y"))
                if try_again() == "Y":
                    continue
                else:
                    start = False
            else:  # add the calendar event if the dates are valid
                calendar[date] = event
                print("\nEvent successfully added.")
        elif user_choice.upper() == "X":
            start = False
        elif user_choice.upper() == "D":
            if len(calendar.keys()) < 1:
                print("The calendar has no entries to delete")
                continue
            else:
                value = date_or_event()
                if value[0] == "D":
                    for k in calendar.keys():
                        if str(value[1]) == str(k):
                            cal_del(k)
                        else:
                            print("\nDate not found.")
                elif value[0] == "E":
                    for k in calendar.keys():
                        if str(value[1].lower()) == str(calendar[k].lower()):
                            cal_del(k)
                        else:
                            print("\nEvent not found.")
                else:
                    print("Delete cancelled")
        else:
            print("\nLet's try this again")
            continue


# print date_or_event()    
start_calendar()

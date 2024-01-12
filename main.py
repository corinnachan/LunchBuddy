from privacy import sender
from privacy import password
import random
import smtplib

class LunchBuddy: 

    buddy1 = []
    buddy2 = []
    pairs = {}

    
    def names_from_sheet(buddy1):
        pass

    buddy1 = ["A", "B", "C", "D"]
    buddy2 = ["A", "B", "C", "D"]

    def create_lists(buddy1):
        buddy2 = random.sample(buddy1, len(buddy1))

#Run a check so nobody gets themselves as the lunch buddy

    def no_same_name_check(buddy1,buddy2):
        for i in range(len(buddy1)-1):
            if buddy1[i] == buddy2[i]:
                placeholder = buddy2[i]
                buddy2[i] = buddy2[i+1]
                buddy2[i+1] = placeholder
            else: 
                temp_var = buddy2[0]
                buddy2[0] = buddy2[len(buddy2)-1]
                buddy2[len(buddy2)-1] = temp_var

    def assign_pairs(buddy1):
        pass

    def email_content(buddy1, buddy2):

    def send_emails(buddy1):
        pass
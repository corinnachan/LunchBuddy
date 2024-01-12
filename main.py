from googleapiclient.discovery import build
import base64
import email.message
import random
import smtplib

class LunchBuddy: 

    buddy1 = []
    buddy2 = []
    matched_pairs = {}

    
    def names_from_sheet(buddy1):
        pass

    buddy1 = ["A", "B", "C", "D"]
    buddy2 = ["A", "B", "C", "D"]

    def create_lists(buddy1):
        buddy2 = random.sample(buddy1, len(buddy1))
        buddys_email

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

    def assign_pairs(buddy1, buddy2):
        matched_pairs = dict(zip(buddy1, buddy2))

    def email_text(buddy1, buddy2):
        
        print("""Hi {b1}, your Lunch Buddy this week is {b2}. 
              Be sure to email them to set up a lunch this week!""".format(b1=buddy1.title(), b2=buddy2.title()))    

    def send_emails(buddy1):
        pass
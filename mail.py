# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText


# class ActionSubmit(Action):
#     def name(self) -> Text:
#         return "action_submit"
#     def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         self.SendEmail(
#             tracker.get_slot("email"),
#             tracker.get_slot("subject"),
#             tracker.get_slot("message")
#         )
        
#         dispatcher.utter_message("Thanks for providing the details. We have sent you a mail at {}".format(tracker.get_slot("email")))
#         return []

   
    
#     def SendEmail(self,toaddr,subject,message):
#         fromaddr = "sri102929@gmail.com"
#         # instance of MIMEMultipart
#         msg = MIMEMultipart()

#         # storing the senders email address
#         msg['From'] = fromaddr

#         # storing the receivers email address
#         msg['To'] = toaddr

#         # storing the subject
#         msg['Subject'] = subject

#         # string to store the body of the mail
#         body = message

#         # attach the body with the msg instance
#         msg.attach(MIMEText(body, 'plain'))

#         # open the file to be sent
#         # filename = "/home/ashish/Downloads/webinar_rasa2_0.png"
#         # attachment = open(filename, "rb")
#         #
#         # # instance of MIMEBase and named as p
#         # p = MIMEBase('application', 'octet-stream')
#         #
#         # # To change the payload into encoded form
#         # p.set_payload((attachment).read())
#         #
#         # # encode into base64
#         # encoders.encode_base64(p)
#         #
#         # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#         #
#         # # attach the instance 'p' to instance 'msg'
#         # msg.attach(p)

#         # creates SMTP session
#         s = smtplib.SMTP('smtp.gmail.com', 587)
#         s.set_debuglevel(1)

#         # start TLS for security
#         s.starttls()


#         # Authentication
#         try:
#             s.login(fromaddr, "srilekha@1")

#             # Converts the Multipart msg into a string
#             text = msg.as_string()

#             # sending the mail
#             s.sendmail(fromaddr, toaddr, text)
#         except Exception as e:
#             print(f"An Error occured while sending email: {str(e)}")
#         finally:
#             # terminating the session
#             s.quit()

     
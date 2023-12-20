from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import feedparser
from rasa_sdk.events import SlotSet


class ActionDownloadMonthlyPayslip(Action):
    def name(self) -> Text:
        return "action_download_monthly_payslip"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # URL to the monthly payslip download page
        Allsec_url = "https://smartpay.allsectech.com/Accenturelogin/"

        # Instructions for the user
        instructions =  "You can get all the payroll related details at Allsec Smart Pay. \n \n" \
                        "Here is a detailed guide to help you navigate better.\n \n" \
                        "1. Go to the following link: {}\n" \
                        "2. Log in using your credentials.\n" \
                        "3. Navigate to the 'Compensation' section.\n" \
                        "4. Click on PaySlip. \n" \
                        "5. Select the desired month and year.\n" \
                        "6. Click the 'Download' button to get your payslip PDF.".format(Allsec_url)

        # Send the instructions to the user
        dispatcher.utter_message(text=instructions)
        return []


class ActionWFHReimbursement(Action):
    def name(self) -> Text:
        return "action_wfh_reimbursment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # URL to the monthly payslip download page
        Allsec_url = "https://smartpay.allsectech.com/Accenturelogin/"

        # Instructions for the user
        instructions =  "You can get all the payroll related details at Allsec Smart Pay. \n \n" \
                        "Here is a detailed guide to help you navigate.\n \n" \
                        "1. Go to the following link: {}\n" \
                        "2. Log in using your credentials.\n" \
                        "3. Navigate to the 'Reimbursements' section.\n" \
                        "4. Click on WFH Assistance Reimbursments. \n" \
                        "5. Fill the required details and upload the receipt of your purchase.\n" \
                        "6. Click on 'Submit' button to claim for WFH Reimbursments.".format(Allsec_url)

        # Send the instructions to the user
        dispatcher.utter_message(text=instructions)
        return []


class ActionBankaccountchange(Action):
    def name(self) -> Text:
        return "action_bank_account_change"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # URL to the monthly payslip download page
        Allsec_url = "https://smartpay.allsectech.com/Accenturelogin/"

        # Instructions for the user
        instructions =  "You can get all the payroll related details at Allsec Smart Pay. \n \n" \
                        "Here is a detailed guide to help you navigate.\n \n" \
                        "1. Go to the following link: {}\n" \
                        "2. Log in using your credentials.\n" \
                        "3. Navigate to the 'Utilities & Forms' section.\n" \
                        "4. Click on  Bank Account Change. \n" \
                        "5. Select the bank name from the drop down and give your bank account to which you want to change the bank account to.\n" \
                        "6. Click on 'Submit' button and the process is done. \n \n" \
                        "You will get further notifications to your accenture mail id".format(Allsec_url)

        # Send the instructions to the user
        dispatcher.utter_message(text=instructions)
        return []


class ActionFetchLearningMaterials(Action):
    def name(self) -> Text:
        return "action_fetch_learning_materials"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        topic = tracker.get_slot("topic")
        rss_url = get_rss_url(topic)
        if rss_url:
            response = requests.get(rss_url)
            if response.status_code == 200:
                rss_content = response.text
                parsed_feed = feedparser.parse(rss_content)
                max_links_to_display = 5  # Set the maximum number of links to display
                for entry in parsed_feed.entries[:max_links_to_display]:
                    title = entry.title
                    link = entry.link
                    dispatcher.utter_message(f"Title: {title}\nLink: {link}")
            else:
                dispatcher.utter_message("Failed to fetch the RSS feed.")
        else:
            dispatcher.utter_message("Sorry, I don't have a feed URL for that topic.")
        return []

def get_rss_url(topic):
    if topic.lower() == "linux":
        return "https://www.linuxjournal.com/rss.xml"
    elif topic.lower() == "azure":
        return "https://azure.microsoft.com/en-us/blog/feed/"
    elif topic.lower() == "aws":
        return "https://aws.amazon.com/blogs/machine-learning/feed/"
    elif topic.lower() == "python":
        return "http://python-apuntes.blogspot.com/feeds/posts/default"
    elif topic.lower() == "data science":
        return "https://www.kdnuggets.com/feed/"
    else:
        return None  # Return None or a default feed URL for unknown topics

class ActionMyte(Action):
    def name(self) -> Text:
      return "action_myte"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        myte_url="https://myte.accenture.com/"

        instructions = "1. If you login through company laptop: \n"\
                       "2. To access MyTE, please click the URL: [MyTE Link](https://myte.accenture.com/) \n"\
                       "3. If you login through external device: \n" \
                       "4. Click the URL : [MyTE Link](https://myte.accenture.com/) \n" \
                       "5. Login with your Accenture credentials. \n " \
                       "6. You can now access MyTE."

        dispatcher.utter_message(text=instructions)
        return[]

class ActionGetMyTEExpensesInstructions(Action):
    def name(self) -> Text:
        return "action_get_myte_expenses_instructions"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        myte_url="https://myte.accenture.com/"
        # Provide simple instructions for MyTE Expenses

        instructions = "To process expenses in MyTE, follow these steps: [MyTE Link](https://myte.accenture.com/).\n \n" \
                       "1. Log in to MyTE with your Accenture credentials.\n" \
                       "2. Click on the 'Expenses' or 'Expense Management' section.\n" \
                       "3. Choose the option to create a new expense report.\n" \
                       "4. Fill in the required details, such as expenses, receipts, and descriptions.\n" \
                       "5. Review and submit your expense report.\n" \
                       "6. Wait for approval from your manager or finance team.\n" \
                       "7. Once approved, your expenses will be reimbursed."
        
        # Send the response to the user
        dispatcher.utter_message(text=instructions)
        return []


class ActionID(Action):
    def name(self) -> Text:
        return "action_id"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        support_url =  "https://support.accenture.com"
        instructions =  "To apply for an ID, visit the Support Portal: {}. Here are the steps: \n \n" \
                        "1. Click on 'Request Workplace Service/Support'.\n" \
                        "2. Fill in the mandatory fields such as country, contact, and building.\n" \
                        "3. Choose 'ID' under the category.\n" \
                        "4. Select all 3 cards under the sub-category: SEZ, Display, and Wallet.\n" \
                        "5. Fill in the floor number, seat number, and a short description as 'Request new card'.\n" \
                        "6. Fill in the description field.\n" \
                        "7. Click 'Add Attachments' and upload your photo with a white background.\n" \
                        "8. Click 'Submit'.\n \n \n \n" \
                        "You will receive an email confirming that a new case has been opened on the date and time with the respective FCR ID and a short description. You can mention your FCR number to the helpdesk to inquire about your IDs." .format(support_url)
        dispatcher.utter_message(text=instructions)
        return []

 
class ActionBookingRoom(Action):
    def name(self) -> Text:
        return "action_booking_room"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        reservation_url = "https://reservations.accenture.com/reserve-space/Default.aspx"
        instructions ="You can use the Reservation Portal at {} to make your booking.\n \n" \
                      "Here are the steps to follow for booking a room:\n \n" \
                      "1. Visit the portal and navigate to 'Check-in or Management Space Reservations'.\n" \
                      "2. Click on 'Reserve Workspace' and select 'Create a Reservation'.\n" \
                      "3. Choose the type of reservation, e.g., 'Ind Reserve Meeting Room'.\n" \
                      "4. Select the date, time, location, and number of people.\n" \
                      "5. Choose the room from the available list and proceed.\n" \
                      "6. Enter the enterprise IDs of the members occupying the room.\n" \
                      "7. Click 'Create Reservation'.\n" \
                      "8. You'll receive a confirmation email, and if the booking is in 'Request' status, wait for the Local Workplace team's confirmation.\n" \
                      "9. Once confirmed, you can check in by clicking 'Check In'." .format(reservation_url)
        dispatcher.utter_message(text=instructions)
        return []

class ActionRelocateLocation(Action):
    def name(self):
        return "action_relocate_location"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        relocation_url = "https://ast.accenture.com/atlas/Home/wfrmHomePage.aspx"

        instructions = "To relocate your work location, please follow these steps:\n \n" \
                       "1. Click on the link {} to raise reloaction request.\n" \
                       "2. Once you're on the page, click on 'Transfer' and fill in the mandatory fields.\n" \
                       "3. Click the 'Submit' button." .format(relocation_url)
        dispatcher.utter_message(text=instructions)
        return []

 
class ActionBookSeat(Action):
    def name(self):
        return "action_book_seat"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        seat_booking_url = "https://acpindia-mobile.accenture.com/home"

        instructions = "To book a seat, please follow these steps:\n \n" \
                       "1. Click on the link {} to book your seat in the workspace.\n" \
                       "2. On the page, select the facility floor and choose an available seat.\n" \
                       "3. Once selected, click on 'Reserve,' and your seat will be booked.\n" \
                       "4. You'll receive a confirmation email to your Outlook account about your seat booking." .format(seat_booking_url)
        dispatcher.utter_message(text=instructions)
        return []


class ActionApplyForTechLeap(Action):
    def name(self) -> Text:
        return "action_apply_for_techleap"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Replace [Application Link] with the actual application link
        application_link = "https://atci.techleap.accenture.com/home"

        response ="To apply for TechLeap, please follow these steps:\n \n" \
                  "1. Launch the browser and clear the cache and cookies from browser settings.We recommend using the Chrome browser.\n " \
                  "2. You can receive the School 1 Registration Application through Outlook with an attached PDF and instructions.Date and time are specified for each slot, along with the number of slots available.You can also use this website: [Application Link].\n" \
                  "3. View the available slots and make a wise decision to select an exam slot. Click the button to select a slot.This will open the exam slot review page, showing the selected exam slot details.\n" \
                  "4. Review the slot details and confirm by clicking the “Book this slot for me” button OR select a different slot by clicking the “I want a different slot” button.On clicking the “Book this slot for me” button, a processing page will show for 20-30 seconds.Afterward, the “Click here to proceed” button will be visible on the page.\n " \
                  "5. Click the “Click here to proceed” button. This will show the exam slot booked details.\n " \
                  "Please read the information displayed on the page. \n " \
                  "To know about the process of your application, visit our application page: " + application_link

        dispatcher.utter_message(text=response)
        return []


class ActionAssessmentMailers(Action):
    def name(self) -> Text:
        return "action_assessment_mailers"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "1. To receive assessment mailers, make sure you have subscribed to our mailing list. \n " \
                   "2. You will receive updates and instructions via email. \n " \
                   "3. You will receive the mailers for Assessment Registration 4-5 weeks after your school kick-off call. \n " \
                   "4. You will get multiple opportunities to register for assessment every fortnight. \n "

        dispatcher.utter_message(text=response)
        return []

 

class ActionSchoolSelection(Action):
    def name(self) -> Text:
        return "action_school_selection"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        application_link = "https://atci.techleap.accenture.com/home"
        response = "1. Here is the link to how you can choose the school in techleap {}.\n \n" \
                   "2. The learning programs in the entire Technology spectrum of the TechLeap phase are modelled in a 2-dimensional construct.Understand the choice made by the ASE’s. If the choice is inline with the mid-term or long-term project needs then encourage the ASE to continue on the choice.\n" \
                   "3. The ASE's are expected to choose a school that is inline with the business needs.\n" \
                   "4. Supervisor/Project Mentor or DU Lead would recommend a relevant school to the ASE.".format(application_link)
        dispatcher.utter_message(text=response)
        return []

class ActionAtciAse(Action):
     def name(self) -> Text:
        return "action_atci_ase"
     def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text,Any]]:
        link="https://ts.accenture.com/sites/Marketing_Communications_CoE/SitePages/ATCI/ASE%20Professional%20Advancement%20Program.aspx"

        Year1="https://accenture.percipio.com/customlibrary/3d964feb-aef9-47d1-be98-6860612bea38/7eb526e8-88bc-4f23-98d3-8b8808a41e33"

        Year2="https://accenture.percipio.com/customlibrary/3d964feb-aef9-47d1-be98-6860612bea38/2287c077-b0b1-465b-a778-fee26cf2beb3"

        response =  "The ATCI-ASE Professional Advancement Program is a structured learning path which is spread across 0-24 months with interventions focusing on Business Communication skills, Personal Productivity & Well-Being. This learning path runs parallel to the Tech Expressway Program. \n \n" \
                    "1. Access and read through the 'ATCI Tech Expressway' ASE Professional Development Curriculum at {} \n" \
                    "2. Click on the link to access Year1 of the course: {} \n" \
                    "3. Click on the link to access Year2 of the course: {} \n \n " \
                    "For any queries or support required,please write to 'ATCI.ProfessionalAdv@accenture.com'." .format(link,Year1,Year2)
  
        dispatcher.utter_message(text=response)
        return []

# mylearning

class Actionmylearning(Action):
     def name(self) -> Text:
        return "action_mylearning"
     def run(self,dispatcher:CollectingDispatcher, tracker: Tracker,domain:Dict[Text,Any]) -> List[Dict[Text,Any]]:
          mylearning = "https://mylearning.accenture.com/mylearningui/learner/home"

          response ="1. The myLearning portal is designed for your learning needs.It let's you take up mandatory trainings at your level and view your ongoing and upcoming trainings.\n \n" \
                    "2. Click on the link to go to portal {} \n \n  " \
                    "For any help on the myLearning portal, reach out to the team via the 'Contact Us' option on the portal home page.".format(mylearning)

          dispatcher.utter_message(text=response)
          return []

# action_ethics

class ActionEthics(Action):
     def name(self) -> Text:
          return "action_ethics"
     def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text,Any]]:

          mylearning = "https://mylearning.accenture.com/mylearningui/learner/home"

          response ="1. Ethics and compliance is a mandatory course.\n \n" \
                    "2. Ethics and Compliance courses and additional learning connections help you to live accenture core values,comply with laws, practice good behaviors and follow our Code of Business Ethics.\n \n " \
                    "You can access your required training directly from {}".format(mylearning)
          dispatcher.utter_message(text=response)
          return []


class ActionChangePrimarySkill(Action):
    def name(self) -> Text:
        return "action_change_primary_skill"

    def run(self, dispatcher:CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          mycompetency_url = "https://mycompetency.accenture.com/#/home"

          response ="To change your primary skill, follow these steps:\n \n" \
                    "1. Go to the [MyCompetency]({}) website.\n" \
                    "2. Once you are on the MyCompetency website, you will be able to see your primary and secondary skills under 'My Skill Profile'.\n" \
                    "3. Find the 'Change Skill' option for your primary skill and click on it.\n" \
                    "4. You will be redirected to the next page where you can search for the skill you are interested in.\n" \
                    "5. Click on the skill for which assessments are available.\n" \
                    "6. Mark it as your primary skill by clicking on 'Mark as primary skill'.\n" \
                    "7. Now, this skill will be added as your primary skill.\n" \
                    "8. Take the assessments to improve your proficiency.\n \n" \
                    "Note: You can have only one skill as your primary skill, but you can add multiple skills as secondary skills." .format(mycompetency_url)

          dispatcher.utter_message(text=response)
          return []


class ActionAddSecondarySkill(Action):
    def name(self) -> Text:
        return "action_add_secondary_skill"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         mycompetency_url = "https://mycompetency.accenture.com/#/home"

         response ="To add secondary skills, follow these steps:\n \n" \
                   "1. Click on {} to go to the MyCompetency website.\n" \
                   "2. Once you are on the MyCompetency website, you will be able to see your primary and secondary skills under 'My Skill Profile'.\n" \
                   "3. On the MyCompetency website, under 'My Skill Profile', find the 'Add New Skill' option and click on it.\n" \
                   "4. Search for a skill for which assessments are available.\n" \
                   "5. Click on the skill and select 'Add Secondary Skill'.\n" \
                   "6. The skill will be added to your list of secondary skills.\n" \
                   "7. You can add multiple secondary skills by repeating these steps." .format(mycompetency_url)

         dispatcher.utter_message(text=response)
         return []

class AnswerQuestions(Action):
    def name(self) -> Text:
        return "action_answer_questions"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message["intent"].get("name")

        if intent == "ask_mentor_network_purpose":
            response = "The Mentor Network program is aimed at providing ASEs coaching and guidance to settle in, make a smooth transition from college to corporate, and nurture their potential and guide them to take steps to achieve their career aspirations at ATCI. [Learn more about iAspire](https://www.iaspire.accenture.com/) by using this link."
        elif intent == "ask_is_mentor_program_part_of_iaspire":
            response = "Yes, the Mentor Network program is part of the many exciting career-building experiences we are bringing to you with iAspire."
        elif intent == "ask_who_is_a_mentor":
            response = "A mentor is at the career level of a team lead who can help our entry-level talent in their formative career years, and guide the mentees to settle in with Accenture and ATCI."
        elif intent == "ask_topics_for_mentor_guidance":
            response = "A mentor offers additional support to the ASEs in addition to the supervisor who is primarily responsible for ASE's journey. Along with this, mentors will support the transition of ASEs from campus to corporate, help balance learning and project work, and provide the bigger picture and the behaviors to follow during the two-year learning journey of the Tech Expressway Academy."
        elif intent == "ask_how_to_get_matched_with_mentor":
            response = "To get matched with a mentor:\n \n1. Visit iAspire.\n2. Click on 'Take Charge' and then go to 'Build my Mentor Network'.\n3. Click on the 'Let’s go' button to go to the Mentor Network page.\n4. To register as a mentee, click on 'Get Guidance'.\n5. Select the area you need guidance on and mention your 'Mentor Guidance Objective' (your purpose of seeking mentorship).\n6. The system will automatically assign a mentor to you based on your market unit, then market and business group.".format()
        elif intent == "ask_how_to_connect_with_mentor":
            response = "Once a mentor is auto-assigned to you, a meeting will be scheduled with the mentor automatically from the back end."
        elif intent == "ask_can_opt_out_of_mentor_program":
            response = "Mentor Network is a completely volunteer program and is designed to help you settle in. You can continue with the program until the time you find value in it."
        elif intent == "ask_can_change_mentor":
            response = "No, you cannot change your mentor on your own. To select a new mentor, your current mentor will need to mark the mentorship as complete on iAspire. You can also write to iAspire@accenture.com for help."

        # Send the response with the hyperlink
        dispatcher.utter_message(text=response)
        return []
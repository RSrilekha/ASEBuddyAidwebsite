# import pandas as pd
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet

# class ActionExcelData(Action):
#     def name(self):
#         return "action_excel_data"

#     def run(self, dispatcher, tracker, domain):
#         try:
#             # Extract entities from the user's message
#             entities = tracker.latest_message.get('entities', [])

#             # Check if entities are present
#             if entities:
#                 column_name, column_value = self.extract_column_name(entities)

#                 if column_name and column_value:
#                     print(f"Extracted entities - column_name: {column_name}, column_value: {column_value}")

#                     # Load Excel data
#                     excel_file_path = r'C:\Users\vanik\ASE Status - DU12.xlsx'
#                     df = pd.read_excel(excel_file_path)

#                     print(f"Loaded Excel data:\n{df.head()}")  # Print the first few rows of the DataFrame for debugging

#                     # ... rest of your code using the loaded DataFrame 'df' and extracted entities
#                     dispatcher.utter_message(f"Setting column_name slot to: {column_name}")
#                     dispatcher.utter_message(f"Setting column_value slot to: {column_value}")

#                 else:
#                     dispatcher.utter_message("I'm sorry, I couldn't understand your question.")

#             else:
#                 dispatcher.utter_message("I'm sorry, I couldn't understand your question.")

#         except Exception as e:
#             dispatcher.utter_message(f"An error occurred: {str(e)}")

#         return []

#     def extract_column_name(self, entities):
#         # Assuming 'column_name' and 'column_value' are valid entities in your training data
#         column_name = None
#         column_value = None

#         for entity in entities:
#             if entity['entity'] == 'column_name':
#                 column_name = entity['value']
#             elif entity['entity'] == 'column_value':
#                 column_value = entity['value']

#         return column_name, column_value

#     def generate_response(self, entities, df):
#         response = ""

#         for entity in entities:
#             column_name = entity['entity']
#             column_value = entity['value']

#             relevant_data = df[df['Resource Name'] == column_value]
#             print(relevant_data)
#             if not relevant_data.empty:
#                 # Handle different types of questions
#                 if column_name.lower() == 'skill':
#                     response += f"The skill of {column_value} is: {relevant_data['Skill'].values[0]}\n"
#                 elif column_name.lower() == 'training status':
#                     response += f"The training status of {column_value} is: {relevant_data['Training status'].values[0]}\n"
#                 elif column_name.lower() == 'enterprise id':
#                     response += f"The Enterprise ID of {column_value} is: {relevant_data['Enterprise ID'].values[0]}\n"
#                 elif column_name.lower() == 'mme poc':
#                     response += f"The MME POC of {column_value} is: {relevant_data['MME POC'].values[0]}\n"
#                 elif column_name.lower() == 'additional skills trained on':
#                     response += f"The additional skills trained on by {column_value} are: {relevant_data['Additional skills trained on'].values[0]}\n"
#                 elif column_name.lower() == 'workday supervisor':
#                     response += f"The Workday Supervisor of {column_value} is: {relevant_data['Workday Supervisor'].values[0]}\n"
#                 elif column_name.lower() == 'trained by':
#                     response += f"{column_value} was trained by: {relevant_data['Trained by'].values[0]}\n"
#                 elif column_name.lower() == 'hiring status':
#                     response += f"The Hiring Status of {column_value} is: {relevant_data['Hiring Status'].values[0]}\n"
#                 elif column_name.lower() == 'techleap status':
#                     response += f"The Techleap Status of {column_value} is: {relevant_data['Techleap Status'].values[0]}\n"
#                 elif column_name.lower() == 'joining date':
#                     response += f"The Joining Date of {column_value} is: {relevant_data['Resource Joining Date'].values[0]}\n"
#                 elif column_name.lower() == 'appeared for client interview':
#                     response += f"{column_value} appeared for a client interview: {relevant_data['Appeared for client interview'].values[0]}\n"
#                 # Add more conditions for other columns as needed...
#                 else:
#                     response += f"Sorry, I don't have information about {column_name} for {column_value}.\n"
#             else:
#                 response += f"Sorry, no data found for {column_name} {column_value}.\n"

#         return response.strip()

# import pandas as pd
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet
# class ActionExcelData01(Action):
#     def name(self):
#         return "action_excel_data01"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         print("Tracker:", tracker.current_state())
#         try:
#             # Extract entities from the user's message
#             entities = tracker.latest_message.get('entities', [])
            
#             # Check if entities are present
#             if entities:
#                 # Extract column_name and resource_name from entities
#                 column_name, resource_name = self.extract_entities(entities)

#                 if column_name and resource_name:
#                     # Load Excel data
#                     excel_file_path = r'C:\Users\vanik\ASE Status - DU12.xlsx'
#                     df = pd.read_excel(excel_file_path)

#                     # Query the DataFrame for the specified resource_name
#                     relevant_data = df[df['Resource Name'].str.lower() == resource_name.lower()]

#                     if not relevant_data.empty:
#                         # Extract information based on the specified column_name
#                         response = self.generate_response(column_name, resource_name, relevant_data)
#                         dispatcher.utter_message(response)
#                     else:
#                         dispatcher.utter_message(f"Sorry, no data found for {resource_name}.")
#                 else:
#                     dispatcher.utter_message("I'm sorry, I couldn't understand your question.")

#             else:
#                 dispatcher.utter_message("I'm sorry, I couldn't understand your question.")

#         except Exception as e:
#             dispatcher.utter_message(f"An error occurred: {str(e)}")

#         return []

#     def extract_entities(self, entities):
#         column_name = None
#         resource_name = None

#         for entity in entities:
#             if entity['entity'] == 'column_name':
#                 column_name = entity['value']
#             elif entity['entity'] == 'resource_name':
#                 resource_name = entity['value']

#         return column_name, resource_name

#     def generate_response(self, column_name, resource_name, df):
#     # Convert column_name and resource_name to lowercase for case-insensitive matching
#      column_name_lower = column_name.lower()
#      resource_name_lower = resource_name.lower()

#     # Check if the column exists in the DataFrame
#      if column_name_lower in df.columns:
#         # Extract information for the specified column
#         information = df.loc[df['Resource Name'].str.lower() == resource_name_lower, column_name_lower].values

#         if len(information) > 0:
#             return f"The {column_name} of {resource_name} is: {information[0]}"
#         else:
#             return f"Sorry, no data found for {resource_name}."
#      else:
#         return f"Sorry, I don't have information about {column_name} for {resource_name}."


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionGetSupervisor(Action):
    def name(self) -> Text:
        return "action_get_supervisor"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Assuming df is your DataFrame, and it has columns 'Resource Name' and 'Supervisor'
            df = pd.read_excel(r'C:\Users\vanik\ASE Status - DU12.xlsx')  # Replace with your actual file name or path

            # Extract supervisor information from the DataFrame
            supervisor_dict = {}
            for index, row in df.iterrows():
                resource_name = row["Resource Name"]
                supervisor = row["Workday Supervisor"]
                if not pd.isnull(resource_name) and not pd.isnull(supervisor):
                    supervisor_dict[resource_name] = supervisor

            # Get the resource name from the tracker
            resource_name = tracker.get_slot("resource_name")

            # Debug prints
            print(f"Tracker Resource Name: {resource_name}")
            print(f"Supervisor Dict: {supervisor_dict}")

            # Check if the requested resource name exists in the supervisor_dict
            if resource_name in supervisor_dict:
                supervisor = supervisor_dict[resource_name]
                dispatcher.utter_message(f"The supervisor of {resource_name} is {supervisor}")
            else:
                dispatcher.utter_message(f"Supervisor information not found for {resource_name}")

        except Exception as e:
            print(f"Error: {e}")
            dispatcher.utter_message(f"Error reading Excel file: {e}")

        return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionGetSkills(Action):
    def name(self) -> Text:
        return "action_get_skills"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Assuming df is your DataFrame, and it has columns 'Resource Name' and 'Basic Skill'
            df = pd.read_excel(r'C:\Users\vanik\ASE Status - DU12.xlsx')  # Replace with your actual file name or path

            # Extract skills information from the DataFrame
            skills_dict = {}
            for index, row in df.iterrows():
                resource_name = row["Resource Name"]
                skill = row["Skill"]
                if not pd.isnull(resource_name) and not pd.isnull(skill):
                    skills_dict[resource_name] = skill

            # Debug prints
            print(f"Skills Dict: {skills_dict}")

            # Check if any resource name is provided in the user's input
            if tracker.latest_message.get('entities'):
                # Get the resource name from the user's input
                resource_name_requested = tracker.latest_message['entities'][0]['value']

                # Debug prints
                print(f"Requested Resource Name: {resource_name_requested}")

                # Check if the requested resource name exists in the skills_dict
                if resource_name_requested in skills_dict:
                    skill = skills_dict[resource_name_requested]
                    dispatcher.utter_message(f"{resource_name_requested} has the skill: {skill}")
                else:
                    dispatcher.utter_message(f"Skill information not found for {resource_name_requested}")
            else:
                # If no specific resource name is provided, list skills for all resources
                for resource_name, skill in skills_dict.items():
                    dispatcher.utter_message(f"{resource_name} has the skill: {skill}")

        except Exception as e:
            print(f"Error: {e}")
            dispatcher.utter_message(f"Error reading Excel file: {e}")

        return []
    
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionGetEnterpriseID(Action):
    def name(self) -> Text:
        return "action_get_enterprise_id"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Assuming df is your DataFrame, and it has columns 'Resource Name' and 'Enterprise ID'
            df = pd.read_excel(r'C:\Users\vanik\ASE Status - DU12.xlsx')  # Replace with your actual file name or path

            # Extract Enterprise ID information from the DataFrame
            enterprise_id_dict = {}
            for index, row in df.iterrows():
                resource_name = row["Resource Name"]
                enterprise_id = row["Enterprise ID"]
                if not pd.isnull(resource_name) and not pd.isnull(enterprise_id):
                    enterprise_id_dict[resource_name] = enterprise_id

            # Get the resource name from the tracker
            resource_name = tracker.get_slot("resource_name")

            # Debug prints
            print(f"Tracker Resource Name: {resource_name}")
            print(f"Enterprise ID Dict: {enterprise_id_dict}")

            # Check if the requested resource name exists in the enterprise_id_dict
            if resource_name in enterprise_id_dict:
                enterprise_id = enterprise_id_dict[resource_name]
                dispatcher.utter_message(f"The Enterprise ID of {resource_name} is {enterprise_id}")
            else:
                dispatcher.utter_message(f"Enterprise ID information not found for {resource_name}")

        except Exception as e:
            print(f"Error: {e}")
            dispatcher.utter_message(f"Error reading Excel file: {e}")

        return []

# Similarly, you can create classes for each column like 'action_get_mme_poc', 'action_get_skill', etc.

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionGetAspiration(Action):
    def name(self) -> Text:
        return "action_get_aspiration"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Assuming df is your DataFrame, and it has columns 'Resource Name' and 'Aspiration'
            df = pd.read_excel(r'C:\Users\vanik\ASE Status - DU12.xlsx')  # Replace with your actual file name or path

            # Extract Aspiration information from the DataFrame
            aspiration_dict = {}
            for index, row in df.iterrows():
                resource_name = row["Resource Name"]
                aspiration = row["Aspirations"]
                if not pd.isnull(resource_name) and not pd.isnull(aspiration):
                    aspiration_dict[resource_name] = aspiration

            # Get the resource name from the tracker
            resource_name = tracker.get_slot("resource_name")

            # Debug prints
            print(f"Tracker Resource Name: {resource_name}")
            print(f"Aspiration Dict: {aspiration_dict}")

            # Check if the requested resource name exists in the aspiration_dict
            if resource_name in aspiration_dict:
                aspiration = aspiration_dict[resource_name]
                dispatcher.utter_message(f"The Aspiration of {resource_name} is {aspiration}")
            else:
                dispatcher.utter_message(f"Aspiration information not found for {resource_name}")

        except Exception as e:
            print(f"Error: {e}")
            dispatcher.utter_message(f"Error reading Excel file: {e}")

        return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionGetTrainingStatus(Action):
    def name(self) -> Text:
        return "action_get_training_status"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Assuming df is your DataFrame, and it has columns 'Resource Name' and 'Training Status'
            df = pd.read_excel(r'C:\Users\vanik\ASE Status - DU12.xlsx')  # Replace with your actual file name or path

            # Extract Training Status information from the DataFrame
            training_status_dict = {}
            for index, row in df.iterrows():
                resource_name = row["Resource Name"]
                training_status = row["Training status"]
                if not pd.isnull(resource_name) and not pd.isnull(training_status):
                    training_status_dict[resource_name] = training_status

            # Get the resource name from the tracker
            resource_name = tracker.get_slot("resource_name")

            # Debug prints
            print(f"Tracker Resource Name: {resource_name}")
            print(f"Training Status Dict: {training_status_dict}")

            # Check if the requested resource name exists in the training_status_dict
            if resource_name in training_status_dict:
                training_status = training_status_dict[resource_name]
                dispatcher.utter_message(f"The Training Status of {resource_name} is {training_status}")
            else:
                dispatcher.utter_message(f"Training Status information not found for {resource_name}")

        except Exception as e:
            print(f"Error: {e}")
            dispatcher.utter_message(f"Error reading Excel file: {e}")

        return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionGetAdditionalSkills(Action):
    def name(self) -> Text:
        return "action_get_additional_skills"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Assuming df is your DataFrame, and it has columns 'Resource Name' and 'Additional Skills'
            df = pd.read_excel(r'C:\Users\vanik\ASE Status - DU12.xlsx')  # Replace with your actual file name or path

            # Extract Additional Skills information from the DataFrame
            additional_skills_dict = {}
            for index, row in df.iterrows():
                resource_name = row["Resource Name"]
                additional_skills = row["Additional skills trained on"]
                if not pd.isnull(resource_name) and not pd.isnull(additional_skills):
                    additional_skills_dict[resource_name] = additional_skills

            # Get the resource name from the tracker
            resource_name = tracker.get_slot("resource_name")

            # Debug prints
            print(f"Tracker Resource Name: {resource_name}")
            print(f"Additional Skills Dict: {additional_skills_dict}")

            # Check if the requested resource name exists in the additional_skills_dict
            if resource_name in additional_skills_dict:
                additional_skills = additional_skills_dict[resource_name]
                dispatcher.utter_message(f"The Additional Skills of {resource_name} are {additional_skills}")
            else:
                dispatcher.utter_message(f"Additional Skills information not found for {resource_name}")

        except Exception as e:
            print(f"Error: {e}")
            dispatcher.utter_message(f"Error reading Excel file: {e}")

        return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionGetTrainedBy(Action):
    def name(self) -> Text:
        return "action_get_trained_by"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Assuming df is your DataFrame, and it has columns 'Resource Name' and 'Trained By'
            df = pd.read_excel(r'C:\Users\vanik\ASE Status - DU12.xlsx')  # Replace with your actual file name or path

            # Extract Trained By information from the DataFrame
            trained_by_dict = {}
            for index, row in df.iterrows():
                resource_name = row["Resource Name"]
                trained_by = row["Trained by"]
                if not pd.isnull(resource_name) and not pd.isnull(trained_by):
                    trained_by_dict[resource_name] = trained_by

            # Get the resource name from the tracker
            resource_name = tracker.get_slot("resource_name")

            # Debug prints
            print(f"Tracker Resource Name: {resource_name}")
            print(f"Trained By Dict: {trained_by_dict}")

            # Check if the requested resource name exists in the trained_by_dict
            if resource_name in trained_by_dict:
                trained_by = trained_by_dict[resource_name]
                dispatcher.utter_message(f"{resource_name} was trained by {trained_by}")
            else:
                dispatcher.utter_message(f"Training information not found for {resource_name}")

        except Exception as e:
            print(f"Error: {e}")
            dispatcher.utter_message(f"Error reading Excel file: {e}")

        return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionGetHiringStatus(Action):
    def name(self) -> Text:
        return "action_get_hiring_status"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Assuming df is your DataFrame, and it has columns 'Resource Name' and 'Hiring Status'
            df = pd.read_excel(r'C:\Users\vanik\ASE Status - DU12.xlsx')  # Replace with your actual file name or path

            # Extract Hiring Status information from the DataFrame
            hiring_status_dict = {}
            for index, row in df.iterrows():
                resource_name = row["Resource Name"]
                hiring_status = row["Hiring Status"]
                if not pd.isnull(resource_name) and not pd.isnull(hiring_status):
                    hiring_status_dict[resource_name] = hiring_status

            # Get the resource name from the tracker
            resource_name = tracker.get_slot("resource_name")

            # Debug prints
            print(f"Tracker Resource Name: {resource_name}")
            print(f"Hiring Status Dict: {hiring_status_dict}")

            # Check if the requested resource name exists in the hiring_status_dict
            if resource_name in hiring_status_dict:
                hiring_status = hiring_status_dict[resource_name]
                dispatcher.utter_message(f"The Hiring Status of {resource_name} is {hiring_status}")
            else:
                dispatcher.utter_message(f"Hiring Status information not found for {resource_name}")

        except Exception as e:
            print(f"Error: {e}")
            dispatcher.utter_message(f"Error reading Excel file: {e}")

        return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionGetResourceJoiningDate(Action):
    def name(self) -> Text:
        return "action_get_resource_joining_date"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Assuming df is your DataFrame, and it has columns 'Resource Name' and 'Resource Joining Date'
            df = pd.read_excel(r'C:\Users\vanik\ASE Status - DU12.xlsx')  # Replace with your actual file name or path

            # Extract Resource Joining Date information from the DataFrame
            joining_date_dict = {}
            for index, row in df.iterrows():
                resource_name = row["Resource Name"]
                joining_date = row["Resource Joining Date"]
                if not pd.isnull(resource_name) and not pd.isnull(joining_date):
                    joining_date_dict[resource_name] = joining_date

            # Get the resource name from the tracker
            resource_name = tracker.get_slot("resource_name")

            # Debug prints
            print(f"Tracker Resource Name: {resource_name}")
            print(f"Resource Joining Date Dict: {joining_date_dict}")

            # Check if the requested resource name exists in the joining_date_dict
            if resource_name in joining_date_dict:
                joining_date = joining_date_dict[resource_name]
                dispatcher.utter_message(f"{resource_name} joined on {joining_date}")
            else:
                dispatcher.utter_message(f"Joining Date information not found for {resource_name}")

        except Exception as e:
            print(f"Error: {e}")
            dispatcher.utter_message(f"Error reading Excel file: {e}")

        return []
    
    
from typing import Text, List, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionGetTechleapStatus(Action):
    def name(self) -> Text:
        return "action_get_techleap_status"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Assuming df is your DataFrame, and it has columns 'Resource Name' and 'Techleap Status'
            df = pd.read_excel(r'C:\Users\vanik\ASE Status - DU12.xlsx')  # Replace with your actual file name or path

            # Extract Techleap Status information from the DataFrame
            techleap_status_dict = {}
            for index, row in df.iterrows():
                resource_name = row["Resource Name"]
                techleap_status = row["Techleap Status"]
                if not pd.isnull(resource_name) and not pd.isnull(techleap_status):
                    techleap_status_dict[resource_name] = techleap_status

            # Get the resource name from the tracker
            resource_name = tracker.get_slot("resource_name")

            # Debug prints
            print(f"Tracker Resource Name: {resource_name}")
            print(f"Techleap Status Dict: {techleap_status_dict}")

            # Check if the specified resource exists in the dictionary
            if resource_name in techleap_status_dict:
                status = techleap_status_dict[resource_name]
                message = f"The Techleap status for {resource_name} is {status}."
            else:
                message = f"Sorry, I couldn't find information for {resource_name} in the Techleap status data."

            # Send the message to the user
            dispatcher.utter_message(text=message)

        except Exception as e:
            # Handle exceptions appropriately
            print(f"Error: {e}")
            dispatcher.utter_message(text="An error occurred while retrieving the Techleap status.")

        return []

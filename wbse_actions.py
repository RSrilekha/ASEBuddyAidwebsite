from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class GetwbseCodeBillableAction(Action):
    def name(self) -> Text:
        return "action_get_wbse_code_billable"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("location")
        billable = tracker.get_slot("billable")

        print(f"Location: {location}, Billable: {billable}")
         
        print(tracker.current_slot_values())



        # Mapping of wbse codes for different locations and billable status
        wbse_codes = {
            "Hyderabad": {"billable": "BGYJU005"},
            "Bangalore": {"billable": "BGYJU008"},
            "Chennai": {"billable": "BGYJU00B"},
        }

        # Get the corresponding wbse code based on location and billable status
        if billable:
            wbse_code = wbse_codes.get(location, {}).get("billable")
        else:
            wbse_code = None

        print(f"wbse Code: {wbse_code}")

        if wbse_code:
            dispatcher.utter_message(f"The wbse code for {location} ({'Billable'}) is: {wbse_code}")
        else:
            dispatcher.utter_message(f"Sorry, unable to retrieve the wbse code for the given details")

        return []


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class GetwbseCodeNonBillableAction(Action):
    def name(self) -> Text:
        return "action_get_wbse_code_non_billable"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("location")
        non_billable = tracker.get_slot("non_billable")

        print(f"Location: {location}, Non_Billable: {non_billable}")
         
        print(tracker.current_slot_values())



        # Mapping of wbse codes for different locations and billable status
        wbse_codes = {
            "Hyderabad": {"non_billable": "BGYJU00O"},
            "Bangalore": {"non_billable": "BGYJU007"},
            "Chennai": {"non_billable": "BGYJU009"},
        }

        # Get the corresponding wbse code based on location and billable status
        if non_billable:
            wbse_code = wbse_codes.get(location, {}).get("non_billable")
        else:
            wbse_code = None

        print(f"wbse Code: {wbse_code}")

        if wbse_code:
            dispatcher.utter_message(f"The wbse code for {location} ({'Non_Billable'}) is: {wbse_code}")
        else:
            dispatcher.utter_message(f"Sorry, unable to retrieve the wbse code for the given details")

        return []
        
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class GetwbseCodeAction(Action):
    def name(self) -> Text:
        return "action_get_wbse_code"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("location")
        atci_on_job_shadow_lt_6_months = tracker.get_slot("ATCI_On_Job_Shadow_LT_6_months")

        print(f"Location: {location}, ATCI On-Job Shadow < 6 months: {atci_on_job_shadow_lt_6_months}")
        print(tracker.current_slot_values())

        wbse_code = self.get_wbse_code(location, "ATCI_On_Job_Shadow_LT_6_months", "AAV8X002")

        if wbse_code:
            dispatcher.utter_message(f"The wbse code for {location} (ATCI On-Job Shadow < 6 months) is: {wbse_code}")
        else:
            dispatcher.utter_message(f"Sorry, unable to retrieve the wbse code for the given details")

        return []

    def get_wbse_code(self, location: Text, duration_slot: Text, default_code: Text) -> Text:
        # Mapping of wbse codes for different locations and durations
        wbse_codes = {
            "Hyderabad": {duration_slot: "AAV8X002"},
            "Bangalore": {duration_slot: "AAV8X002"},
            "Chennai": {duration_slot: "AAV8X002"},
            "Mumbai": {duration_slot: "AAV8X002"},
            "Pune": {duration_slot: "AAV8X002"},
            "Gurugram": {duration_slot: "AAV8X002"},
            "Kolkata": {duration_slot: "AAV8X002"},
        }

        # Get the corresponding wbse code based on location and duration
        return wbse_codes.get(location, {}).get(duration_slot, default_code)
    
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class GetwbseCodeAtciAction(Action):
    def name(self) -> Text:
        return "action_get_wbse_code_atci"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("location")
        atci_on_job_shadow_gt_6_months = tracker.get_slot("ATCI_On_Job_Shadow_GT_6_months")

        print(f"Location: {location}, ATCI On-Job Shadow greater than 6 months: {atci_on_job_shadow_gt_6_months}")
        print(tracker.current_slot_values())

        wbse_code = self.get_wbse_code(location, "ATCI_On_Job_Shadow_GT_6_months", "AAV8X00P")

        if wbse_code:
            dispatcher.utter_message(f"The wbse code for {location} (ATCI On-Job Shadow greater than 6 months) is: {wbse_code}")
        else:
            dispatcher.utter_message(f"Sorry, unable to retrieve the wbse code for the given details")

        return []

    def get_wbse_code(self, location: Text, duration_slot: Text, default_code: Text) -> Text:
        # Mapping of wbse codes for different locations and durations
        wbse_codes = {
            "Hyderabad": {duration_slot: "AAV8X00P"},
            "Bangalore": {duration_slot: "AAV8X00P"},
            "Chennai": {duration_slot: "AAV8X00P"},
            "Mumbai": {duration_slot: "AAV8X00P"},
            "Pune": {duration_slot: "AAV8X00P"},
            "Gurugram": {duration_slot: "AAV8X00P"},
            "Kolkata": {duration_slot: "AAV8X00P"},
        }

        # Get the corresponding wbse code based on location and duration
        return wbse_codes.get(location, {}).get(duration_slot, default_code)


class GetwbseCodeAvanadeWithin6MonthsAction(Action):
    def name(self) -> Text:
        return "action_get_wbse_code_avanade_within_6_months"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("location")
        avanade_within_6_months = tracker.get_slot("Avanade_within_6_months")

        print(f"Location: {location}, Avanade within 6 months: {avanade_within_6_months}")
        print(tracker.current_slot_values())

        wbse_code = self.get_wbse_code(location, "Avanade_within_6_months", "AENB200G")

        if wbse_code:
            dispatcher.utter_message(f"The wbse code for {location} (Avanade within 6 months) is: {wbse_code}")
        else:
            dispatcher.utter_message(f"Sorry, unable to retrieve the wbse code for the given details")

        return []

    def get_wbse_code(self, location: Text, duration_slot: Text, default_code: Text) -> Text:
        # Mapping of wbse codes for different locations and durations
        wbse_codes = {
            "Hyderabad": {duration_slot: "AENB200G"},
            "Bangalore": {duration_slot: "AENB200G"},
            "Chennai": {duration_slot: "AENB200G"},
            "Mumbai": {duration_slot: "AENB200G"},
            "Pune": {duration_slot: "AENB200G"},
            "Gurugram": {duration_slot: "AENB200G"},
            "Kolkata": {duration_slot: "AENB200G"},
        }

        # Get the corresponding wbse code based on location and duration
        return wbse_codes.get(location, {}).get(duration_slot, default_code)


class GetwbseCodeAvanadeMoreThan6MonthsAction(Action):
    def name(self) -> Text:
        return "action_get_wbse_code_avanade_more_than_6_months"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("location")
        avanade_more_than_6_months = tracker.get_slot("Avanade_more_than_6_months")

        print(f"Location: {location}, Avanade more than 6 months: {avanade_more_than_6_months}")
        print(tracker.current_slot_values())

        wbse_code = self.get_wbse_code(location, "Avanade_more_than_6_months", "AENB201K")

        if wbse_code:
            dispatcher.utter_message(f"The wbse code for {location} (Avanade more than 6 months) is: {wbse_code}")
        else:
            dispatcher.utter_message(f"Sorry, unable to retrieve the wbse code for the given details")

        return []

    def get_wbse_code(self, location: Text, duration_slot: Text, default_code: Text) -> Text:
        # Mapping of wbse codes for different locations and durations
        wbse_codes = {
            "Hyderabad": {duration_slot: "AENB201K"},
            "Bangalore": {duration_slot: "AENB201K"},
            "Chennai": {duration_slot: "AENB201K"},
            "Mumbai": {duration_slot: "AENB201K"},
            "Pune": {duration_slot: "AENB201K"},
            "Gurugram": {duration_slot: "AENB201K"},
            "Kolkata": {duration_slot: "AENB201K"},
        }

        # Get the corresponding wbse code based on location and duration
        return wbse_codes.get(location, {}).get(duration_slot, default_code)



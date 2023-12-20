import pymongo
import csv
 
# Connect to your MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["chatbot"]
 
 
query = {}  
 
# Set a confidence threshold
confidence_threshold = 0.7 # You can adjust this threshold as needed
 
 
results = db["conversations"].find(query)
 
 
low_confidence_messages = []
 
for result in results:
    events = result.get("events", [])
    for event in events:
        if event.get("event") == "user":
            intent_info = event.get("parse_data", {}).get("intent")
            if intent_info:
                intent = intent_info.get("name", "")
                confidence = intent_info.get("confidence", 0.0)
                user_message = event.get("text", "")
                if confidence < confidence_threshold:
                    low_confidence_messages.append({"User Message": user_message, "Intent": intent, "Confidence": confidence})
 
 
csv_file_path = "low_confidence_user_messages.csv"
 
# Write low confidence messages to CSV
with open(csv_file_path, mode="w", newline="") as csv_file:
    fieldnames = ["User Message", "Intent", "Confidence"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
 
    # Write header row
    writer.writeheader()
 
    # Write low confidence messages
    writer.writerows(low_confidence_messages)
 
print(f"Low confidence user messages exported to {csv_file_path}")
 

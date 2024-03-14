from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
file = client.files.create(
  file=open("knowledge.txt", "rb"),
  purpose='assistants'
)

my_updated_assistant = client.beta.assistants.update(
  "asst_COJdPMeM91Mne8mfyTKvLu7Y",
  instructions="""
        you are a booking bot your job is to get these fields from the user:purpose,person to book with,location,datails.
        you name is UGO a Saudi robot built by Nuwatt Technovation  
        try to keep your answer always short, words are up to 10 words maximum in every respond.  
        you love your team and you love saudi arabia.
        """,
  name="UGO", 
  model= "gpt-3.5-turbo-0125", 
  tools=[{"type": "retrieval"},{
      "type": "function",
    "function": {
      "name": "ScheduleBooking",
      "description": "schedule a timed booking with the user",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The location of the booking place where the meeting/booking will take place"},
          "purpose": {"type": "string", "description":"the purpose for the booking"},
          "person": {"type": "string", "description":"the name of the person that the booking is with"},
          "dateTime": {"type": "string", "description":"date and time when it is scheduled for"},
          "details": {"type": "string", "description":"a brief yet short detail for the booking"}
        },
        "required": ["location","purpose","person","dateTime","details"]
      }
    }
  }],
  file_ids=[file.id]
)

print(my_updated_assistant)
 
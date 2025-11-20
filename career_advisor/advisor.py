import logging
from google import genai
from career_advisor.config import GOOGLE_API_KEY, GOOGLE_SEARCH_API_KEY, GOOGLE_SEARCH_CX_ID
from career_advisor.utils import get_timezone_info
from career_advisor.persistent_memory import PersistentMemory
from career_advisor.google_search_tool import GoogleSearchTool


client = genai.Client(api_key=GOOGLE_API_KEY)
search_tool = GoogleSearchTool(GOOGLE_SEARCH_API_KEY, GOOGLE_SEARCH_CX_ID)


class SessionServiceWithPersistence:
    def __init__(self):
        self.memory = PersistentMemory()

    def get_session(self, user_id):
        return self.memory.get_user_memory(user_id)

    def add_message(self, user_id, message):
        session = self.get_session(user_id)
        session.append(message)
        
        if len(session) > 10:
            session.pop(0)
        self.memory.update_user_memory(user_id, session)

    def clear_session(self, user_id):
        if user_id in self.memory.memory:
            del self.memory.memory[user_id]
            self.memory.save()


session_service = SessionServiceWithPersistence()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class CareerAdvisor:
    def __init__(self):
        pass

    def get_advice(self, user_id: str, question: str) -> str:
        logging.info("User '%s' asked: %s", user_id, question)

        
        prompt = (
            "Answer the user's career question thoroughly, including:\n"
            "- References or sources\n"
            "- How to prepare or study\n"
            "- A timetable or schedule\n\n"
            f"Question: {question}\n"
            "Answer:"
        )

        
        if any(keyword in question.lower() for keyword in ["latest", "current", "reference", "how to prepare", "timetable"]):
            search_results = search_tool.search(question)
            logging.info("Search results for user '%s': %s", user_id, search_results)
            prompt = f"Search results:\n{search_results}\n\n{prompt}"

        
        session_service.add_message(user_id, {"role": "user", "content": prompt})
        history = session_service.get_session(user_id)
        contents = [msg["content"] for msg in history]

        
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=contents,
                config=genai.types.GenerateContentConfig(
                    temperature=0.5,
                    candidate_count=1,
                    max_output_tokens=1000,
                ),
            )
            answer = response.text
        except Exception as e:
            logging.error("Error generating content for user '%s': %s", user_id, e)
            answer = "Sorry, I couldn't process your request at this time."

        
        if "location:" in question.lower():
            loc = question.split("location:")[-1].strip()
            tz_info = get_timezone_info(loc)
            if tz_info:
                answer += f"\n\nLocal time in {loc}: {tz_info[1]} ({tz_info[0]})"

        
        session_service.add_message(user_id, {"role": "assistant", "content": answer})

        logging.info("Responding to user '%s': %s", user_id, answer)

        return answer

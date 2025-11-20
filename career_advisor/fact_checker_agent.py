from career_advisor.google_search_tool import GoogleSearchTool
from career_advisor.config import GOOGLE_SEARCH_API_KEY, GOOGLE_SEARCH_CX_ID

class FactCheckerAgent:
    def __init__(self):
        self.search_tool = GoogleSearchTool(GOOGLE_SEARCH_API_KEY, GOOGLE_SEARCH_CX_ID)

    def check_facts(self, question: str) -> str:
        
        keywords = ["fact check", "verify", "true", "accuracy"]
        if any(word in question.lower() for word in keywords):
            search_results = self.search_tool.search(question)
            return f"Fact check info:\n{search_results}\n\n{question}"
        return question

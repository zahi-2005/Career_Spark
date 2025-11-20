from career_advisor.advisor import CareerAdvisor
from .fact_checker_agent import FactCheckerAgent


class MultiAgentSystem:
    def __init__(self):
        self.fact_checker = FactCheckerAgent()
        self.career_advisor = CareerAdvisor()

    def get_combined_advice(self, user_id: str, question: str) -> str:
        
        enhanced_question = self.fact_checker.check_facts(question)

        
        response = self.career_advisor.get_advice(user_id, enhanced_question)

        return response

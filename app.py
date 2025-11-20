import logging
from career_advisor.multi_agent_controller import MultiAgentSystem


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    multi_agent = MultiAgentSystem()
    user_id = "default_user"  
    
    print("Welcome to the Multi-Agent Career Advisor!")
    print("Type your career questions below, or type 'exit' to quit.")

    while True:
        user_input = input("\nAsk your career question:\n> ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        logging.info("User input: %s", user_input)
        try:
            
            response = multi_agent.get_combined_advice(user_id, user_input)
            logging.info("Agent response: %s", response)
            print("\nCareer Advisor Response:\n", response)
        except Exception as e:
            logging.error("Error during advice generation: %s", e)
            print(f"Oops, something went wrong: {e}")

if __name__ == "__main__":
    main()


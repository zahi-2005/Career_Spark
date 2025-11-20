class InMemorySessionService:
    def __init__(self):
        self.sessions = {}

    def get_session(self, user_id):
        if user_id not in self.sessions:
            self.sessions[user_id] = []
        return self.sessions[user_id]

    def add_message(self, user_id, message):
        session = self.get_session(user_id)
        session.append(message)
        
        if len(session) > 10:
            session.pop(0)

    def clear_session(self, user_id):
        if user_id in self.sessions:
            del self.sessions[user_id]

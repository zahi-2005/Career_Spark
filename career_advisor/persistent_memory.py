import json
import os

class PersistentMemory:
    def __init__(self, filename='memory.json'):
        self.filename = filename
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.memory = json.load(f)
        else:
            self.memory = {}

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.memory, f)

    def get_user_memory(self, user_id):
        return self.memory.get(user_id, [])

    def update_user_memory(self, user_id, data):
        self.memory[user_id] = data
        self.save()

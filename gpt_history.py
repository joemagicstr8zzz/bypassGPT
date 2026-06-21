class ConversationHistory:
    def __init__(self, max_length=5):
        self.history = []
        self.max_length = max_length

    def add(self, user_input, gpt_response):
        # Keep history within bounds (each turn consists of 2 roles)
        if len(self.history) >= self.max_length * 2:
            self.history.pop(0)  # Remove oldest user message
            self.history.pop(0)  # Remove oldest assistant response
            
        self.history.append({"role": "user", "content": user_input})
        self.history.append({"role": "assistant", "content": gpt_response})

    def get_history(self):
        return self.history

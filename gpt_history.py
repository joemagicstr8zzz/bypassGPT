class ConversationHistory:
    def __init__(self, max_length=5):
        self.history = []
        self.max_length = max_length

    def add(self, user_input, gpt_response):
        if len(self.history) >= self.max_length * 2:
            self.history.pop(0)  # Remove the oldest user input
            self.history.pop(0)  # Remove the oldest GPT response
        self.history.append(user_input)
        self.history.append(gpt_response)

    def get_formatted_history(self):
        return "\n".join(self.history)
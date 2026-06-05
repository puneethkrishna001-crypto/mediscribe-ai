class ConversationMemory:
    def __init__(self, max_history=5):
        self.max_history = max_history
        self.history = []

    def add(self, role, message):
        self.history.append(
            {
                "role": role,
                "content": message
            }
        )

        if len(self.history) > self.max_history * 2:
            self.history = self.history[-self.max_history * 2:]

    def get_context(self):
        context = []

        for item in self.history:
            context.append(
                f"{item['role']}: {item['content']}"
            )

        return "\n".join(context)
from collections import defaultdict

class ConversationManager:

    def __init__(self):

        # Guarda conversaciones por usuario
        self.conversations = defaultdict(list)

        # Número máximo de mensajes que recordará
        self.max_messages = 20

    def get_messages(self, user_id: str):

        return self.conversations[user_id]

    def add_user_message(self, user_id: str, message: str):

        self.conversations[user_id].append(
            {
                "role": "user",
                "content": message
            }
        )

        self._trim(user_id)

    def add_assistant_message(self, user_id: str, message: str):

        self.conversations[user_id].append(
            {
                "role": "assistant",
                "content": message
            }
        )

        self._trim(user_id)

    def clear(self, user_id: str):

        self.conversations[user_id] = []

    def _trim(self, user_id: str):

        if len(self.conversations[user_id]) > self.max_messages:

            self.conversations[user_id] = self.conversations[user_id][-self.max_messages:]
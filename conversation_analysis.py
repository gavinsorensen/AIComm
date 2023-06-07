class InteractionTracker:
    def __init__(self):
        # initialize empty dictionary to track user interactions
        self.interactions = {}
    
    def track_interaction(self, user_id, message):
        # if user_id already exists in interactions dictionary, add message to the list of messages
        if user_id in self.interactions:
            self.interactions[user_id].append(message)
        # if user_id is not in interactions dictionary, create new key and add message to the list of messages
        else:
            self.interactions[user_id] = [message]
    
    def flag_conversations(self, max_length, max_repetitive):
        # initialize empty list to store flagged conversations
        flagged_conversations = []
        
        # iterate over all user_ids in interactions dictionary
        for user_id in self.interactions:
            messages = self.interactions[user_id]
            length = len(messages)
            num_repetitive = len(set(messages))
            
            # if conversation length exceeds max_length or number of repetitive messages exceeds max_repetitive, add conversation to flagged_conversations list
            if length > max_length or num_repetitive <= max_repetitive:
                flagged_conversations.append(user_id)
        
        # return list of flagged conversations
        return flagged_conversations

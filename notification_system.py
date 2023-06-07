import datetime

class CustomerInquiry:
    def __init__(self, inquiry_id, customer_name, issue_description, timestamp):
        self.inquiry_id = inquiry_id
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.timestamp = timestamp

class CustomerInquiryTracker:
    def __init__(self, unresolved_time_threshold):
        self.unresolved_time_threshold = unresolved_time_threshold
        self.customer_inquiries = []
    
    def add_inquiry(self, customer_name, issue_description):
        inquiry_id = len(self.customer_inquiries) + 1
        timestamp = datetime.datetime.now()
        inquiry = CustomerInquiry(inquiry_id, customer_name, issue_description, timestamp)
        self.customer_inquiries.append(inquiry)
    
    def check_unresolved(self):
        current_time = datetime.datetime.now()
        unresolved = []
        
        for inquiry in self.customer_inquiries:
            time_difference = current_time - inquiry.timestamp
            if time_difference.seconds > self.unresolved_time_threshold:
                unresolved.append(inquiry)
        
        return unresolved

class NotificationSystem:
    def __init__(self):
        self.operatives = []
    
    def add_operative(self, operative):
        self.operatives.append(operative)
    
    def notify_operatives(self, unresolved):
        for operative in self.operatives:
            message = "The following inquiries have not been resolved: \n"
            for inquiry in unresolved:
                message += f"Inquiry ID: {inquiry.inquiry_id}, Customer Name: {inquiry.customer_name}, Issue Description: {inquiry.issue_description}\n"
            message += "Please follow up with these customers as soon as possible."
            operative.receive_notification(message)

class Operative:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def receive_notification(self, message):
        # Code to send notification email to the operative
        pass

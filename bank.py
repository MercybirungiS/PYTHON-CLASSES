class Bank():
    def __init__(self,acc_Name,acc_No,acc_type):
        self.acc_Name=acc_Name
        self.acc_No=acc_No
        self.acc_type=acc_type
    def name(self):
        return f"Your account name is {self.acc_Name}.Thank you for trusting us !"
    def account_Number(self):
        return f"Your account number is {self.acc_No}. Thank you for trusting us!"
    def account_type(self):
        return f"Your account type is {self.acc_type}.Thank you for trusting us !"

        
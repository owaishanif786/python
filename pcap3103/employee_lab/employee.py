class Employee:
    def __init__(self, name, title, email_address, phone_number=''):
        self.name = name
        self.title = title
        self.email_address = email_address
        self.phone_number = phone_number
    
    def email_signature(self, include_phone=False):
        signature = f'{self.name}\n{self.title}\n{self.email_address}\n'
        if(include_phone == True):
            signature += f'{self.phone_number}\n'
        
        print(signature)

if __name__ == '__main__':
    emp = Employee('lil', 'lilWolf', 'lil@example.com', '030012345')
    emp.email_signature()
    emp.email_signature(True)
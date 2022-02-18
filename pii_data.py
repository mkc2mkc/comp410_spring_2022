import re


# PII = Personally Identifiable Information
# Create a new Pii class based on str
class Pii(str):
    # For help with regex see
    # https://regex101.com
    # https://www.w3schools.com/python/python_regex.asp
    def has_us_phone(self):
        # Match a US phone number ddd-ddd-dddd ie 123-456-7890
        match = re.search(r'\d{3}-\d{3}-\d{4}', self)
        if match:
            return True
        return False

    def has_email(self):
        return None

    def has_ipv4(self):
        # Match an IPv4 address: num.num.num.num where num range = 0 - 255

        # [0-9]:        match numbers 0 - 9
        # [1-9][0-9]:   match numbers 10 - 99
        # 1[0-9][0-9]:  match numbers 100 - 199
        # 2[0-4][0-9]:  match numbers 200 - 249
        # 25[0-5]:      match numbers 250 - 255

        match = re.search(r'^\b([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b'
                          r'.\b([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b'
                          r'.\b([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b'
                          r'.\b([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b$', self)

        # 255.255.255.255 is already preserved for broadcasting and would be valid
        if self.__eq__('255.255.255.255') | self.__eq__('0.0.0.0'):
            return False
        elif match:
            return True
        return False

    def has_ipv6(self):
        match = re.search(r'\b^[0-9a-fA-F]{0,4}\b:\b[0-9a-fA-F]{0,4}\b:'
                          r'\b[0-9a-fA-F]{0,4}\b:\b[0-9a-fA-F]{0,4}\b:'
                          r'\b[0-9a-fA-F]{0,4}\b:\b[0-9a-fA-F]{0,4}\b:'
                          r'\b[0-9a-fA-F]{0,4}\b:\b[0-9a-fA-F]{0,4}\b', self)
        if self.__eq__('0:0:0:0:0:0:0:0'):
            return False
        elif match:
            return True
        return False

    def has_name(self):
        return None

    def has_street_address(self):
        return None

    def has_credit_card(self):
        # match a standard credit card number
        match = re.search(r'\d{4}-\d{4}-\d{4}-\d{4}', self)
        if match:
            return True
        return False

    def has_at_handle(self):
        return None

    def has_pii(self):
        return self.has_us_phone() or self.has_email() or self.has_ipv4() or self.has_ipv6() or self.has_name() or \
               self.has_street_address() or self.has_credit_card() or self.has_at_handle()


def read_data(filename: str):
    data = []
    with open(filename) as f:
        # Read one line from the file stripping off the \n
        for line in f:
            data.append(line.rstrip())
    return data


if __name__ == '__main__':
    data = read_data('sample_data.txt')
    print(data)
    print('---')

    pii_data = Pii('My phone number is 123-123-1234')
    print(pii_data)

    if pii_data.has_pii():
        print('There is PII data preset')
    else:
        print('No PII data detected')

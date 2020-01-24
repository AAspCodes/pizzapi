from .address import Address
import json

class Customer:
    """The Customer who orders a pizza."""

    def __init__(self, stuff):
        print(stuff)
        self.first_name = stuff[0].strip()
        self.last_name = stuff[1].strip()
        self.email = stuff[2].strip()
        self.phone = str(stuff[3]).strip()
        self.str_address = stuff[4]
        print(self.str_address)
        self.address = Address(self.str_address)

    def save(self, filename="customers/customer1.json"):
        """
        saves the current customer to a .json file for loading later
        """
        if not filename.startswith("customers"):
            filename = "customers/" + filename
        json_dict = {"first_name": self.first_name,
             "last_name": self.last_name,
             "email": self.email,
             "phone": self.phone,
             "address": self.str_address}

        with open(filename, "w") as f:
            json.dump(json_dict, f)

    @staticmethod
    def load(filename):
        """
        load and return a new customer object from a json file
        """
        with open(filename, "r") as f:
            data = json.load(f)

            customer = Customer(data["first_name"], 
                                data["last_name"],
                                data["email"],
                                data["phone"],
                                data["address"])
        return customer

    def __repr__(self):
        return "Name: {} {}\nEmail: {}\nPhone: {}\nAddress: {}".format(
            self.first_name,
            self.last_name,
            self.email,
            self.phone,
            self.address,
        )

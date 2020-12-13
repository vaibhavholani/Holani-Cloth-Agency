from __future__ import annotations
import pyrebase
from typing import Optional
from Indivijuval import Supplier

"""
config = {
    "apiKey": "AIzaSyD0vwrC3MH6u4UlRLD3GkHuSXDU8cmi_pU",
    "authDomain": "shanker-sarees-project.firebaseapp.com",
    "databaseURL": "https://shanker-sarees-project.firebaseio.com/",
    "storageBucket": "shanker-sarees-project.appspot.com"
}
"""


class DataUpload:

    """
    The class responsible for Uploading of Data into the Database.

    database : the link to the online database

    :param authentication: hold the config information to access the database
    """

    def __init__(self, authentication: dict = {
        "apiKey": "AIzaSyD0vwrC3MH6u4UlRLD3GkHuSXDU8cmi_pU",
        "authDomain": "shanker-sarees-project.firebaseapp.com",
        "databaseURL": "https://shanker-sarees-project.firebaseio.com/",
        "storageBucket": "shanker-sarees-project.appspot.com"
    }) -> None:

        fire_base = pyrebase.initialize_app(authentication)
        self.database = fire_base.database()

    def upload(self, supplier: Supplier) -> Optional[None, Exception]:

        data = {"name": supplier.name,
                "short_name": supplier.short_name,
                "address": supplier.address
                }
        self.database.child("Supplier").child(2).set(data)




data_up = DataUpload()
data_up.upload(Supplier.create_supplier("abcd", "abcd", "abcd"))

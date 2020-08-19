from Entities import RegisterEntry, MemoEntry
import datetime

sample_register1 = RegisterEntry.call(123, 444, "samunder", "saitax", str(datetime.date))
sample_register2 = RegisterEntry.call(125, 446, "a", "b", str(datetime.date))

supplier_names = ["a", "b", "c", "d", "saitax"]

party_name = ["a", "b", "c", "d", "samunder"]


data_store = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]



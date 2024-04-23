import pandas as pd
pd.set_option("display.max_rows", None)

cust= pd.read_excel("/Users/rajeevabudal/Downloads/2318029-Custumer_Data.xlsx")

order = pd.read_excel("/Users/rajeevabudal/Downloads/2318030-Orders_Data.xlsx")

# print(cust.head())
# print(order.head())

cust_order = pd.merge(cust, cust, left_on = "ID", right_on = "Name", how = "left")[["Name", "Address", "OID", "Date"]]

print(cust_order.head(5));

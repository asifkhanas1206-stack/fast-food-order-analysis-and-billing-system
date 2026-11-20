import pandas as pd
def make_bill(order, prices):
    total = 0
    for item in order:
        name = item[0]
        qty = item[1]
        if name in prices:
            cost = prices[name] * qty
            total += cost
            print(f"{name} x {qty} = {cost}")
        else:
            print(f"{name} not found!")
    return total

def get_discount(total):
    if total >= 3000: 
        return 10  
    if total >= 1500:
        return 5    
    return 0

def size_tag(x):
    if x >= 1500:
        return "Big"
    if x >= 500: 
        return "Medium"
    return "Small"
menu = pd.read_csv("menu.csv")
fri_data = pd.read_csv("orders_friday.csv")
sat_data = pd.read_csv("orders_saturday.csv")
print("---  SAMPLE RECORDS ---")
print(menu.head()) 
print("\n---  DATA INSPECTION ---")
print("Head:\n", fri_data.head())
print("\nTail:\n", fri_data.tail())
print("\nShape tuple:", fri_data.shape)
print("\nColumns list:", fri_data.columns.tolist())
print("\nDescribe summary:\n", fri_data.describe())
print("\nConcise Info:")
fri_data.info()

main_df = pd.concat([fri_data, sat_data], ignore_index=True)

print("\n---  MISSING VALUES BEFORE CLEANING ---")
print(main_df.isnull().sum()) 

main_df = main_df.dropna(subset=["customer", "item_id"])
main_df["payment"] = main_df["payment"].fillna("Cash")
main_df["qty"] = main_df["qty"].fillna(1)

main_df["delivery_min"] = main_df["delivery_min"].interpolate()
print("\nMissing values after cleaning:")
print(main_df.isnull().sum())
main_df["qty"] = main_df["qty"].astype(int)

print("\nDuplicates found:", main_df.duplicated().sum())
main_df = main_df.drop_duplicates()

main_df = pd.merge(main_df, menu, on="item_id", how="inner")

main_df["line_total"] = main_df["price"] * main_df["qty"]           
main_df["size"] = main_df["line_total"].apply(size_tag)          
main_df.loc[main_df["category"] == "Wraps", "category"] = "Wraps & Sandwiches" 
main_df = main_df.rename(columns={"delivery_min": "delivery_time"}) 
main_df = main_df.drop(columns=["calories"])                        

small_df = main_df[["order_id", "customer", "item_name", "qty", "line_total"]] 
big_lines = main_df[main_df["line_total"] > 1500]                             
card_payments = main_df[(main_df["payment"] == "Card") & (main_df["qty"] >= 2)] 
print("\nSelected order details:")
print(small_df.head())

print("\nOrders above Rs. 1500:")
print(big_lines.head())

print("\nCard payments with quantity 2 or more:")
print(card_payments.head())

sorted_desc = main_df.sort_values(by="line_total", ascending=False)
sorted_asc = main_df.sort_values(by="line_total", ascending=True)
print("\nHighest order lines:")
print(sorted_desc.head())

print("\nLowest order lines:")
print(sorted_asc.head())

print("\n--- GROUPBY & AGGREGATION ---")
sales_by_cat = main_df.groupby("category")["line_total"].sum().sort_values(ascending=False)
print("Sales by Category:\n", sales_by_cat)

top_items = main_df.groupby("item_name")["qty"].sum().sort_values(ascending=False)
print("\nTop ordered items:")
print(top_items.head())
payment_modes = main_df.groupby("payment")["line_total"].agg(["sum","mean","min","max" ,"count"])
print("\nPayment Modes Summary:\n", payment_modes)

order_totals = main_df.groupby("order_id")["line_total"].sum().to_frame(name="order_total")
cust_info = main_df[["order_id", "customer", "day"]].drop_duplicates("order_id").set_index("order_id")

final_orders = order_totals.join(cust_info).reset_index()
final_orders["disc_pct"] = final_orders["order_total"].apply(get_discount)
final_orders["discount"] = final_orders["order_total"] * final_orders["disc_pct"] / 100
final_orders["final_bill"] = final_orders["order_total"] - final_orders["discount"]



ordered_ids = main_df["item_id"].tolist()
not_ordered_count = 0

for item_id in menu["item_id"]:
    if item_id not in ordered_ids:
        not_ordered_count += 1
top_sales = main_df.groupby("item_name")["line_total"].sum()
top_sales = top_sales.sort_values(ascending=False)
print("\n--- INSIGHTS ---")

print("1. Top grossing item:")
print(top_sales.head(1))
print(f"2. Average final invoice generation is Rs.{round(final_orders['final_bill'].mean(), 2)}.")
print(f"3. Maximum order payment recorded is Rs.{final_orders['final_bill'].max()}.")
print(f"4. Total number of transactions cleared: {final_orders.shape[0]}.")
print(f"5. Count of menu items that didn't get any orders: {not_ordered_count}.")

main_df.to_csv("final_cleaned_orders.csv", index=False)
final_orders.to_csv("order_totals.csv", index=False)
print("\nCSV Files saved successfully!")

menu_prices = dict(menu[['item_name', 'price']].values)

user_choice = input("\nDo you want to run interactive mode for custom order? (y/n): ")
if user_choice.lower() == 'y':
    print("\n--- MENU CARD ---")
    for idx, row in menu.iterrows():
        print(f"{row['item_id']} - {row['item_name']} - Rs {row['price']}")
        
    user_cart = []
    while True:
        inp_id = input("Enter item id (0 to exit): ")
        if not inp_id.isdigit():
            print("Put a valid number.")
            continue
        inp_id = int(inp_id) 
        if inp_id == 0: 
            break
        
        if inp_id not in menu["item_id"].values:
            print("ID not found!")
            continue
            
        quantity = input("Quantity: ")
        if not quantity.isdigit() or int(quantity) <= 0:
            print("Invalid count number!")
            continue
            
        item_title = menu[menu["item_id"] == inp_id]["item_name"].values[0]
        user_cart.append([item_title, int(quantity)])
        
    print("\n--- BILL DATA ---")
    sub_total = make_bill(user_cart, menu_prices)
    disc_rate = get_discount(sub_total)
    print("Gross Total:", sub_total)
    print(f"Discount: {disc_rate}%")
    print("Net Payable: Rs", sub_total - (sub_total * disc_rate / 100))
else:
    print("Program execution completed.")

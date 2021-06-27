import os

class Product:
  ID = 1001
  def __init__(self, name, count, price):
    self.id = Product.ID
    self.name = name
    self.count = count 
    self.price = price 

    Product.ID += 1

  def __repr__(self):
    return f"ID: {self.id} | Name: {self.name} ,  Remaining: {self.count} ,  Price: {self.price}"


class DB:
  def __init__(self):
    self.products = []
    self.start_server()

  def main_menu(self):
    print("\nMain menu")
    print("------------------")
    # print("\nSelect an option:\n")
    print("\t1. Add item")
    print("\t2. Show items")
    print("\t3. Delete item (by id)")
    print("\t4. Search for items(by name)")
    print("\t5. Clear screen")
    print("\t6. Save products to file")
    print("\t7. Load products from file")
    print("\t99. Exit")

    command = input("\nEnter number of option:")
    while command not in ["1", "2", "3", "4", "5","6", "7", "99"]:
      command = input("Enter a valid option:")
    return command

  def clear_screen(self):
    os.system("cls")
  
  def append_product(self, product):
    self.products.append(product)

  def add_product(self):
    print("\nAdd new product")
    print("----------------")
    name = input("\tName: ")
    count = int(input("\tCount: "))
    price = float(input("\tPrice: "))
    similar_product = [x for x in self.products if x.name == name]
    if similar_product:
      similar_product[0].count += count
      return "\n Product Already exists, count added."
    else:
      p = Product(name, count, price)
      self.append_product(p)
      return "\nCreated Successfully"

  def delete_product(self):
    print("\nDelete product")
    print("----------------")
    product_id = int(input("\tID: "))
    deleted_item = False
    for p in self.products:
      if p.id == product_id:
        deleted_item = self.products.pop(self.products.index(p))
        break
    if deleted_item:
      return f"\{deleted_item.id} Deleted."
    else:
      return f"\nItem not found !"
      
  def show_all_products(self):
    self.print_products(self.products, "All products: ")

  def print_products(self, products, message):
    if products:
      print(f"\n{message}")
      print("-------------")
      for p in products:
        print(p)
    if not products:
      print("\nNo products found !")

  def search_product(self):
    print(f"\nSearching for items:")
    print("-------------\n")
    name = input("\tEnter Name: ")
    prods = list(filter(lambda x: x.name.lower().find(name.lower()) >-1 , self.products))
    self.print_products(prods, "Search result: ")

  def load_from_file(self):
    print("\nLoad data from file")
    print("-------------")
    filename = input("\tfilename:")
    if not os.path.exists(filename):
      return "File not found !"
    with open(filename, "r") as file:
      for row in file.read().splitlines():
        if not row.split(): continue
        row = row.split(",")
        p = Product(row[0], row[1], row[2])
        self.append_product(p)
    return "\nProducts loaded successfully."

  def save_to_file(self):
    print("\nSaving data to file")
    print("-------------")
    filename = "products.csv"
    with open(filename, "w+") as file:
      for p in self.products:
        text = f"{p.name},{p.count},{p.price}\n"
        file.write(text)
    return "\nSaved successfully.\nFile: products.csv"

  def start_server(self, message=""):
    if message:
      print(message)
    command = self.main_menu()
    result = None
    if command == "99":
      exit()

    elif command == "1":
      result = self.add_product()

    elif command == "2":
      result = self.show_all_products()

    elif command == "3":
      result = self.delete_product()

    elif command == "4":
      result = self.search_product()
    
    elif command == "5":
      result = self.clear_screen()

    elif command == "6":
      result = self.save_to_file()

    elif command == "7":
      result = self.load_from_file()

    self.start_server(result)

DB()

 

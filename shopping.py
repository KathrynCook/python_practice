class Store:
  def __init__(self, name, goods_type, goods_list, profits, is_open = True):
    self.name = name
    self.store_type = goods_type
    self.goods = goods_list
    self.profits = profits
    self.open = is_open

  def __repr__(self):
    description = "{name} is a {store_type} store which currently stocks {goods}. It is ".format(name = self.name, store_type = self.store_type, goods = self.goods)
    if self.open:
      description += "open."
    else:
      description += "closed."
    return description
  
  def buy_stock(self, items):
    self.goods.Append(items)
    print("New stuff arrived at {store}".format(store = self.name))

  def open_store(self):
    self.open = True
    print("{store} is open".format(store = self.name))

  def close_store(self):
    self.open = False
    print("{store} is closed".format(store = self.name))

class Shopper:
  def __init__(self, name, goods_list, money, location = "Home"):
    self.name = name
    self.goods = goods_list
    self.money = money
    self.location = location

  def __repr__(self):
    description = "This is {name} who has {goods} in their basket and {money} left to spend. Currently they are in {location}.".format(name = self.name, goods = self.goods, money = self.money, location = self.location)
    return description

  def visit_location(self, location):
    if location.open:
      self.location = location.name
      print("{person} is now in {location}".format(person= self.name, location = self.location))
    else:
      print("Sorry, {store} is currently closed.".format(store = location.name))

  def buy_item(self, item, location):
    if self.location != location.name:
      print("Sorry, you're in the wrong store!")
    elif location.open == False:
      print("Sorry, {store} is currently closed. Please come back later!".format(store = location.name))
    else:
      if item in location.goods:
        if self.money >= 3:
          print("Buying a {thing}".format(thing = item))
          self.money -= 3
          location.profits += 3
          location.goods.remove(item)
          self.goods.append(item)
        else:
          print("Sorry, not enough money for {thing}!".format(thing = item))
      else:
        print("Sorry, {thing} is out of stock!".format(thing = item))

  def return_item(self, item, location):
    self.goods.remove(item)
    location.goods.append(item)
    self.money += 3
    location.profits -= 3
    print("Item returned.")


store_one = Store("The Store", "grocery", ["fish", "apple", "bread", "milk"], 25)
store_two = Store("Rival Store", "sporting goods", ["ball", "bat", "net", "tent"], 30)
person_one = Shopper("Ida", [], 10, "Home")
person_two = Shopper("Egor", [], 50, "Home")

person_one.visit_location(store_one)
person_one.buy_item("milk", store_one)
print(person_one.goods, person_one.money)
print(store_one.goods, store_one.profits)
person_one.buy_item("bread", store_one)
print(person_one.goods, person_one.money)
print(store_one.goods, store_one.profits)
person_one.buy_item("apple", store_one)
print(person_one.goods, person_one.money)
print(store_one.goods, store_one.profits)
person_one.visit_location(store_two)
person_one.buy_item("ball", store_two)

print(person_one)
print(store_one)

person_two.visit_location(store_two)
person_two.buy_item("tent", store_two)
print(person_two.goods, person_two.money)
print(store_two.goods, store_two.profits)
person_two.buy_item("golf ball", store_two)
person_two.return_item("tent", store_two)
print(person_two.goods, person_two.money)
print(store_two.goods, store_two.profits)

store_two.close_store()
person_two.buy_item("net", store_two)





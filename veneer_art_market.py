class Art:
  def __init__ (self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  def __repr__(self):
    return "{a}. \"{t}\". {y}, {m}. {on}, {ol}.".format(a = self.artist, t = self.title, y = self.year, m = self.medium, on = self.owner.name, ol = self.owner.location)

class Marketplace:
  def __init__(self):
    self.listings = []
  def __repr__(self):
    return "Welcome to the Veneer Marketplace. Please have a look at out current listings!"
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  def remove_listing(self, old_listing):
    self.listings.remove(old_listing)
  def show_listings(self):
    print('Current listings: ')
    for listing in self.listings:
      print(listing)

class Client:
  def __init__ (self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  def sell_artwork(self, artwork, price):
    if artwork.owner.name == self.name:
      sell_piece = Listing(artwork, price, self.name)
      veneer.add_listing(sell_piece)
  def buy_artwork(self, artwork):
    if artwork.owner.name != self.name:
      for listing in veneer.listings:
        if listing.art.title == artwork.title:
          art_listing = listing 
          artwork.owner = self
          veneer.remove_listing(art_listing)

class Listing:
   def __init__ (self, art, price, seller):
     self.art = art
     self.price = price
     self.seller = seller
   def __repr__(self):
     return '{at}, ${p}.'.format(at = self.art.title, p = self.price)

veneer = Marketplace()

edytta = Client('Edytta Halpirt', 'Private Collection', False)

moma = Client('The MOMA', 'New York', True)

girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', 'oil on canvas', 1910, edytta)
  
edytta.sell_artwork(girl_with_mandolin, '6M (USD)')
veneer.show_listings()
print()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
print()
veneer.show_listings()

# Here are some more things you could try: 
# Add a wallet instance variable to clients, update the buying and selling of artworks to also exchange dollar amounts.
# Create a wishlist for your clients, things that are listed but they’re not sure if they should purchase just yet.
# Create expiration dates for listings! Have out of date listings automatically removed from the marketplace.
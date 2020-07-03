# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#item_total = 0
def displayInventory(inventory):
 print("Inventory:\n")
 item_total = 0
 for k, v in inventory.items():
  print(k +':  '+str(v))
  item_total=item_total + 1 
  sum = int(v)
 print("\nTotal number of items: " + str(item_total))
 
displayInventory(stuff)

stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def displayinventory(inventory):
 print('Inventory :')
 item=0
 for k, v in inventory.items():
  print('Total no of items :'+str(item))
  
displayinventory(stuff)  

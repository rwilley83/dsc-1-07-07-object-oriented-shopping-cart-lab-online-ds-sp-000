class ShoppingCart:
    def __init__(self, _employee_discount=None):
    	self._total = 0
    	self._items = []
    	self._employee_discount = _employee_discount

    def get_total(self):
    		return self._total

    def set_total(self, amount):
    		self._total += amount

    def get_items(self):
    		return self._items

    def set_items(self, item):
    		self._items.append({'name': item['name'], 'price': item['price'], 'quantity': item['quantity']})

    def get_employee_discount(self):
    		return self._employee_discount

    def set_employee_discount(percentage):
    		self._employee_discount += percentage

    total = property(get_total, set_total)
    items = property(get_items, set_items)
    employee_discount = property(get_employee_discount, set_employee_discount)

    def add_item(self, name, price, quantity=1):
    	item_total = price * quantity
    	self.total = + item_total
    	self.items = {'name': name, 'price': price, 'quantity': quantity}
    	return self.total

    def mean_item_price(self):
    	item_prices = []
    	total_items = 0
    	for item in self.items:
    		item_prices.append(item['price'] * item['quantity'])
    		total_items += item['quantity']
    	return round(sum(item_prices) / total_items, 2)

    def median_item_price(self):
    	item_prices = []
    	for item in self.items:
    		for i in list(range(0, item['quantity'])):
    			item_prices.append(item['price'])
    	sorted_item_prices = sorted(item_prices)
    	center = len(sorted_item_prices) / 2
    	if center % 2 == 1:
    		return sorted_item_prices[int(center)]
    	else:
    		return (sorted_item_prices[int(center)] + sorted_item_prices[int(center) + 1]) / 2

    def apply_discount(self):
    	if self.employee_discount:
    		return self.total * (1 - self.employee_discount/100)
    	else:
    		return "Sorry, there is no discount to apply to your cart :("

    def item_names(self):
    	item_name_list = []
    	for item in self._items:
    		for i in list(range(0, item['quantity'])):
    			item_name_list.append(item['name'])
    	return item_name_list

    def void_last_item(self):
    	if len(self.items) == 0:
    		return "There are no items in your cart!"
    	else:
    		self.total = -self._items[-1]['price'] #* self._items[-1]['quantity']
    		if self.items[-1]['quantity'] > 0:
    			self._items[-1]['quantity'] += -1
    		else:
    			self._items.pop()





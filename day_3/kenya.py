from person import Person

class Kenyan(Person):

	def probe(self, corrupt):
		self.corrupt = corrupt
	def is_corrupt(self):
		if self.corrupt:
			return "Yes"
		return "No"
		

from requests import Session

class FruityVice:
	def __init__(self) -> None:
		self.api = "https://www.fruityvice.com/api"
		self.session = Session()
		self.session.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def get_all_fruits(self) -> dict:
		return self.session.get(f"{self.api}/fruit/all").json()
	
	def get_fruit_by_id(self, fruit_id: int) -> dict:
		return self.session.get(
			f"{self.api}/fruit/{fruit_id}").json()
	
	def get_fruit_by_name(self, fruit_name: str) -> dict:
		return self.session.get(
			f"{self.api}/fruit/{fruit_name}").json()
	
	def get_fruit_by_nutrition_value(
			self,
			fruit_name: str,
			minimum: int,
			maximum: int) -> dict:
		return self.session.get(
			f"{self.api}/fruit/{fruit_name}?min={minimum}&max={maximum}").json()

	def get_fruits_by_family(self, family: str) -> dict:
		return self.session.get(
			f"{self.api}/fruit/family/{family}").json()
	
	def get_fruits_by_genus(self, genus: str) -> dict:
		return self.session.get(
			f"{self.api}/fruit/genus/{genus}").json()

	def get_fruits_by_order(self, order: str) -> dict:
		return self.session.get(
			f"{self.api}/fruit/order/{order}").json()

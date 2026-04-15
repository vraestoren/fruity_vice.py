from requests import Session

class FruityVice:
	def __init__(self) -> None:
		self.api = "https://www.fruityvice.com/api"
		self.session = Session()
		self.session.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}

	def _get(self, endpoint: str, params: dict = None) -> dict:
		return self.session.get(f"{self.api}{endpoint}", params=params or {}).json()

	def get_all_fruits(self) -> dict:
		return self._get(f"{self.api}/fruit/all")
	
	def get_fruit_by_id(self, fruit_id: int) -> dict:
		return self._get(f"/fruit/{fruit_id}")
	
	def get_fruit_by_name(self, fruit_name: str) -> dict:
		return self._get(f"/fruit/{fruit_name}")
	
	def get_fruit_by_nutrition_value(
			self,
			fruit_name: str,
			minimum: int,
			maximum: int) -> dict:
		params = {
			"min": minimum,
			"max": maximum
		}
		return self._get(f"/fruit/{fruit_name}", params)

	def get_fruits_by_family(self, family: str) -> dict:
		return self._get(f"/fruit/family/{family}")
	
	def get_fruits_by_genus(self, genus: str) -> dict:
		return self._get(f"/fruit/genus/{genus}")

	def get_fruits_by_order(self, order: str) -> dict:
		return self._get(f"/fruit/order/{order}")

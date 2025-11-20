import requests

class GoogleSearchTool:
    def __init__(self, api_key, cx_id):
        self.api_key = api_key
        self.cx_id = cx_id

    def search(self, query):
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": self.api_key,
            "cx": self.cx_id,
            "q": query,
        }
        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            results = response.json().get("items", [])
            snippets = [item.get("snippet", "") for item in results[:3]]
            return "\n".join(snippets)
        except requests.exceptions.RequestException as e:
            
            return f"Search failed: {e}"

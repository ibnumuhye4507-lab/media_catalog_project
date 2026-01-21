class CatalogManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CatalogManager, cls).__new__(cls)
            cls._instance.items = []
        return cls._instance

    def set_items(self, items):
        self.items = items

    def get_all(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)

    # አዲሱ የመፈለጊያ ፋንክሽን
    def search_by_title(self, title):
        return [item for item in self.items if title.lower() in item.title.lower()]
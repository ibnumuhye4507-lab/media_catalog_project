class CatalogManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CatalogManager, cls).__new__(cls)
            cls._instance.items = []
        return cls._instance
    def delete_item_by_title(self, title):
        initial_count = len(self.items)
        # ርዕሱ አንድ አይነት የሆኑትን አስወግዶ ሌሎቹን ብቻ ያስቀራል
        self.items = [item for item in self.items if item.title.lower() != title.lower()]
        return len(self.items) < initial_count # አንድ ነገር ከጠፋ True ይመልሳል
    def set_items(self, items):
        self.items = items

    def get_all(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)

    # አዲሱ የመፈለጊያ ፋንክሽን
    def search_by_title(self, title):
        return [item for item in self.items if title.lower() in item.title.lower()]
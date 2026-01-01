import xml.etree.ElementTree as ET
import os
# ከmodels ፎልደር ውስጥ ክላሶቹን እናስገባለን
from src.models.media import Book, Movie 
from src.models.factory import MediaFactory

class CatalogRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_all(self):
        """ከ XML ፋይል መረጃን ያነባል"""
        if not os.path.exists(self.file_path):
            return []
        
        try:
            tree = ET.parse(self.file_path)
            root = tree.getroot()
            items = []

            for elem in root:
                # የ XML መረጃውን ወደ ዲክሽነሪ (dictionary) እንቀይራለን
                data = {child.tag: child.text for child in elem}
                # በFactory Pattern አማካኝነት ኦብጀክቱን እንፈጥራለን
                item = MediaFactory.create_media(elem.tag, **data)
                if item:
                    items.append(item)
            return items
        except Exception as e:
            print(f"መረጃ ሲጫን ስህተት ተፈጥሯል: {e}")
            return []

    def save_all(self, media_items):
        """መረጃን ወደ XML ፋይል ሴቭ ያደርጋል"""
        root = ET.Element("catalog")
        
        for item in media_items:
            # መጽሐፍ ወይም ፊልም መሆኑን እንለያለን
            if isinstance(item, Book):
                tag = "book"
            elif isinstance(item, Movie):
                tag = "movie"
            else:
                continue

            media_elem = ET.SubElement(root, tag)
            ET.SubElement(media_elem, "title").text = str(item.title)
            ET.SubElement(media_elem, "year").text = str(item.year)
            
            # እንደየአይነቱ የተለየውን መረጃ እንጨምራለን
            if isinstance(item, Book):
                ET.SubElement(media_elem, "author").text = str(item.author)
            elif isinstance(item, Movie):
                ET.SubElement(media_elem, "director").text = str(item.director)
        
        # ፋይሉን በUTF-8 ፎርማት እንጽፋለን
        tree = ET.ElementTree(root)
        tree.write(self.file_path, encoding="UTF-8", xml_declaration=True)
import sys
import os
from lxml import etree

# ፓይዘን የፈጠርናቸውን ፎልደሮች እንዲያገኝ
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.repositories.catalog_repository import CatalogRepository
from src.services.catalog_manager import CatalogManager
from src.models.factory import MediaFactory

def show_menu():
    print("\n" + "="*30)
    print("  የሚዲያ ካታሎግ ማስተዳደሪያ")
    print("="*30)
    print("1. ሁሉንም ሚዲያዎች እይ")
    print("2. አዲስ መጽሐፍ ጨምር")
    print("3. አዲስ ፊልም ጨምር")
    print("4. HTML ሪፖርት አውጣ") # አዲስ የተጨመረ
    print("5. ሴቭ አድርግና ውጣ")
    print("="*30)

def main():
    repo = CatalogRepository("data/catalog.xml")
    manager = CatalogManager()
    
    manager.set_items(repo.load_all())
    
    while True:
        show_menu()
        choice = input("ምርጫዎን ያስገቡ (1-5): ")
        
        if choice == '1':
            items = manager.get_all()
            if not items:
                print("\nካታሎጉ ባዶ ነው።")
            else:
                for i, item in enumerate(items, 1):
                    type_name = item.__class__.__name__
                    print(f"{i}. [{type_name}] ርዕስ: {item.title}, ዓ.ም: {item.year}")

        elif choice == '2':
            title = input("የመጽሐፉ ርዕስ: ")
            year = input("የታተመበት ዓ.ም: ")
            author = input("ደራሲ: ")
            new_book = MediaFactory.create_media("book", title=title, year=year, author=author)
            manager.add_item(new_book)
            print("መጽሐፉ ተጨምሯል!")

        elif choice == '3':
            title = input("የፊልሙ ርዕስ: ")
            year = input("የወጣበት ዓ.ም: ")
            director = input("አዘጋጅ (Director): ")
            new_movie = MediaFactory.create_media("movie", title=title, year=year, director=director)
            manager.add_item(new_movie)
            print("ፊልሙ ተጨምሯል!")

        elif choice == '4': # ሪፖርት የማውጫው ክፍል እዚህ ነው መሆን ያለበት
            try:
                dom = etree.parse("data/catalog.xml")
                xslt = etree.parse("data/full_catalog.xsl")
                transform = etree.XSLT(xslt)
                new_dom = transform(dom)
                with open("report.html", "wb") as f:
                    f.write(etree.tostring(new_dom, pretty_print=True))
                print("\n ok ሪፖርቱ 'report.html' በሚል ስም ተዘጋጅቷል! በብራውዘርህ ክፈተው።")
            except Exception as e:
                print(f"\n no ስህተት ተፈጥሯል: {e}")
                print("ምናልባት data/full_catalog.xsl ፋይል አልተፈጠረም ይሆናል።")

        elif choice == '5':
            repo.save_all(manager.get_all())
            print("መረጃው ተቀምጧል (Saved)። ደህና ሁኑ!")
            break
        else:
            print("የተሳሳተ ምርጫ! እባክህ እንደገና ሞክር።")

if __name__ == "__main__":
    main()
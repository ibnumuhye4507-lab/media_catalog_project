import sys
import os
import webbrowser
from lxml import etree

# Directory setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(BASE_DIR))

XML_PATH = os.path.join(BASE_DIR, "..", "data", "catalog.xml")
XSL_PATH = os.path.join(BASE_DIR, "..", "data", "full_catalog.xsl")
REPORT_PATH = os.path.join(BASE_DIR, "..", "report.html")

from src.repositories.catalog_repository import CatalogRepository
from src.services.catalog_manager import CatalogManager
from src.models.factory import MediaFactory

def show_menu():
    print("\n" + "="*35)
    print("      MEDIA CATALOG MANAGER")
    print("="*35)
    print("1. View All Media Items")
    print("2. Add New Book")
    print("3. Add New Movie")
    print("4. Generate HTML Report")
    print("5. Search Media by Title")
    print("6. Save and Exit")
    print("="*35)

def main():
    repo = CatalogRepository(XML_PATH)
    manager = CatalogManager()
    
    # Load existing data from XML
    try:
        manager.set_items(repo.load_all())
    except Exception as e:
        print(f"Error loading data: {e}")
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            items = manager.get_all()
            if not items:
                print("\nThe catalog is empty.")
            else:
                for i, item in enumerate(items, 1):
                    type_name = item.__class__.__name__
                    print(f"{i}. [{type_name}] {item.title} ({item.year})")

        elif choice == '2':
            title = input("Book Title: ")
            year = input("Publication Year: ")
            author = input("Author: ")
            new_book = MediaFactory.create_media("book", title=title, year=year, author=author)
            manager.add_item(new_book)
            print("Book added successfully!")

        elif choice == '3':
            title = input("Movie Title: ")
            year = input("Release Year: ")
            director = input("Director: ")
            new_movie = MediaFactory.create_media("movie", title=title, year=year, director=director)
            manager.add_item(new_movie)
            print("Movie added successfully!")

        elif choice == '4':
            try:
                if not os.path.exists(XML_PATH) or not os.path.exists(XSL_PATH):
                    print(f"Error: XML or XSL file not found!")
                    continue
                
                dom = etree.parse(XML_PATH)
                xslt = etree.parse(XSL_PATH)
                transform = etree.XSLT(xslt)
                new_dom = transform(dom)
                
                with open(REPORT_PATH, "wb") as f:
                    f.write(etree.tostring(new_dom, pretty_print=True))
                
                print(f"Report generated: {REPORT_PATH}")
                webbrowser.open('file://' + os.path.realpath(REPORT_PATH))
            except Exception as e:
                print(f"Report error: {e}")

        elif choice == '5':
            query = input("Enter title to search: ")
            results = manager.search_by_title(query)
            if results:
                print(f"\n--- Found {len(results)} item(s) ---")
                for i, item in enumerate(results, 1):
                    print(f"{i}. [{item.__class__.__name__}] {item.title} ({item.year})")
            else:
                print(f"No results found for '{query}'")

        elif choice == '6':
            repo.save_all(manager.get_all())
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
# TODO: complete this class
from math import ceil, floor

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.pages = ceil(len(self.collection) / self.items_per_page)
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        return self.pages
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index >= self.pages or page_index < 0:
            return -1
        elif page_index < self.pages-1:
            return self.items_per_page
        else:
            return len(self.collection)-self.items_per_page*(self.pages-1)
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index in range(len(self.collection)):
            return floor(item_index/self.items_per_page)
        else:
            return -1

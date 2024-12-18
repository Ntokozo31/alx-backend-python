#!/usr/bin/env python3


class BaseCaching:
    """BaseCaching defines a caching system"""
    def __init__(self):
        self.cache_data = {}


class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching"""
    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to key in self_cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

    def print_cache(self):
        """Print the current cache data"""
        print("Current Cache data:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")

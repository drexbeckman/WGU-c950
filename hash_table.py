#Hash table handling collisions by chaining
class Hash_table:
    #hash_table constructor
    def __init__(self, capacity = 10):
        #create hashtable
        self.table = []
        #create buckets containing lists for each element of the hash table
        for i in range(capacity):
            self.table.append([])

    #add an element into the hash table O(n)
    def add_item(self, key, item):
        #use hash function to determine bucket item will go into
        bucket = hash(key) % len(self.table)
        list = self.table[bucket]

        #update an element of the table
        for kv in list:
            if kv[0] == key:
                kv[1] = item
                return True

        #insert the item into the bucket's list
        key_value = [key, item]
        list.append(key_value)
        return True

    #remove an element from the hash table O(1)
    def remove_item(self, item_key):
        #find the element's location in the hash table
        bucket = item_key % 10
        list = self.table[bucket]

        #remove the item if it exists in the correct bucket
        if item_key in list:
            list.remove(item_key)
        #alert user if the item does not exist in the table
        else:
            print(f"Could not find {item_key} in hash table")

    #search for an element in the hash table O(n)
    def search_item(self, item_key):
        #find the item's location in the hash table
        bucket = hash(item_key) % len(self.table)
        list = self.table[bucket]

        #find item in list if it exists
        for kv in list:
            if kv[0] == item_key:
                return kv[1]
        return None
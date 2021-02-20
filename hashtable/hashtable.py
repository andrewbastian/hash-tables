class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'NODE:({repr(self.value)})'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.head = 0
        self.buckets = [None] * self.capacity

# DAY 2:
    def __str__(self):
        if self.head is None:
            return '[EMPTY LIST]'

        cur = self.head
        string = ''

        while cur is not None:
            string += f'({cur.value})'

            if cur.next is not None:
                string += '-->'

            cur = cur.next

        return string

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
# DAY 1
        return len(self.buckets)
        

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.head / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.


        """
    # algorithm fnv-1a is
        # Your code here
        hash = 14695981039346656037
        # hash := FNV_offset_basis do
        hashed = key.encode()
        for byte_of_data in hashed:
        # for each byte_of_data to be hashed
            hash = hash * 1099511628211
            # hash := hash × FNV_prime
            hash = hash ^ byte_of_data
            # hash := hash XOR byte_of_data

        return hash
        # return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        pass

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # DAY 1
                # Which slot (index) in the table is the value going?
        """        idx = self.hash_index(key)
        res = HashTableEntry(key, value)
        # Store the value at that slot
        self.buckets[idx] = res"""
        # DAY 2
        
        idx = self.hash_index(key)
        res = HashTableEntry(key, value)
        cur = self.buckets[idx]

        # if the bucket has no index:
        if self.buckets[idx] is None:
            # add the new entry to the unoccupied index
            self.buckets[idx] = HashTableEntry(key, value)
            # expand LinkedList by 1 node
            self.head += 1
            # if the HashTable is getting too small,
            if self.get_load_factor() > 0.7:
                # expand the Table by a factor of `2` 
                self.resize(self.capacity * 2)
        else:
            while cur:
                # check the buckets index key against the entry key for equality,
                if cur.key is key:
                    # check the buckets index value against the entry value,
                    cur.value = value
                    # if both are true do not make an entry
                    return
                # create new var equal to the buckets index
                prev = cur
                # move that index to the next node
                cur = cur.next
            # set our entry to the node after the one we are currently on
            prev.next = res
            # expand LinkedList by 1 Node
            self.head += 1
            # if HashTable is getting too small
            if self.get_load_factor() > 0.7:
                # expand HashTable by a factor of `2`
                self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)
        self.buckets[idx] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)

        if self.buckets[idx]:
            val = self.buckets[idx].value
            return val
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # DAY 2
        new_table = HashTable(new_capacity)
        # for each slot in table:
        for head in self.buckets:
            # for each element in the linked list in that slot:
            if head:
                # for each element in the linked list in that slot:
                new_table.put(head.key, head.value)
                if head.next:
                    cur = head
                    while cur.next:
                        cur = cur.next
                        new_table.put(cur.key, cur.value)

        self.buckets = new_table.buckets
        self.capacity = new_table.capacity


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

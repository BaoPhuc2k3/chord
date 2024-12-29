import hashlib

def hash_key(key):
    """Hash a key using SHA-1 and convert it to an integer."""
    return int(hashlib.sha1(key.encode()).hexdigest(), 16) % (2**8) 

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.successor = self  
        self.finger_table = []
        self.data = {} 

    def find_successor(self, key):
        """Tìm successor của key."""
        if self.successor.node_id >= key > self.node_id:
            return self.successor
        else:
            return self.successor.find_successor(key)

    def store(self, key, value):
        """Lưu trữ dữ liệu vào hệ thống."""
        key_hash = hash_key(key)
        successor = self.find_successor(key_hash)
        successor.data[key_hash] = value

    def lookup(self, key, start_node=None):
        """Tra cứu dữ liệu trong hệ thống."""
        key_hash = hash_key(key)
        if key_hash in self.data:
            return self.data[key_hash]
        elif start_node == self:
            return None
        else:
            if start_node is None:
                start_node = self  
            return self.successor.lookup(key, start_node)




def test_chord_algorithm():
    node1 = Node(10)
    node2 = Node(50)
    node3 = Node(200)

    node1.successor = node2
    node2.successor = node3
    node3.successor = node1

    node1.store("test1", "data1")
    node2.store("test2", "data2")
    
    assert node1.lookup("test1") == "data1"
    assert node3.lookup("test2") == "data2"
    assert node2.lookup("nonexistent") is None

    print("All test cases passed!")

if __name__ == "__main__":
    test_chord_algorithm()

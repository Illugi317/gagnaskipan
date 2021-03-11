class adt_node:
    def __init__(self,key,value):
        self.key = key
        self.value = value

class MapADT:
    def __init__(self):
        self.entry_list = list()

    def insert(self, key, value):
        n_idx = self._find_index(key)
        if n_idx is not None:
            self.entry_list[n_idx].value = value
        else:
            entry = adt_node(key,value)
            self.entry_list.append(entry)
    
    def update(self, key, value):
        self.insert(key,value)

    def find(self, key):
        n_idx = self._find_index(key)
        if n_idx is not None:
            return self.entry_list[n_idx].value
        else:
            return False

    def remove(self, key):
        n_idx = self._find_index(key)
        assert n_idx is not None, "Invalid map key"
        self.entry_list.pop(n_idx)

    def _find_index(self,key):
        for x in range(len(self)):
            if self.entry_list[x].key == key:
                return x
        return None

    def __iter__(self):
        return iter(self.entry_list)

    def __len__(self):
        return len(self.entry_list)

    def __str__(self):
        ret_str = ""
        for x in self:
            ret_str += f"{x.key}{x.value}"


        

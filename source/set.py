#!python

# ======================================= CLASS INSTANCE =========================================


class SetInstance(object):

    # =================================== INITIALIZER METHOD =====================================
    def __init__(self, items=None):
        """ Initializes class data type and size counter, then adds items to list if empty. """
        self.list, self.size = list(), 0        # Initializes list object and size counter
        if items is not None:
            for item in items:
                self.list.append(item)          # Appends items to empty list
                self.size += 1                  # Increments size counter

    # ===================================== CONTAINS METHOD ========================================
    def contains(self, target_item):
        """ Returns whether or not set contains target item. """
        return target_item in self.list         # Returns Boolean indicating presence of item in list

    # ===================================== ITEM ADD METHOD ========================================
    def add(self, target_item):
        """ Returns success/failure message after adding target item to set. """
        if self.contains(target_item):
            return print("\nFAILURE: SET ALREADY CONTAINS ITEM TO ADD: \n{}\n".format(target_item))
        self.list.append(target_item)           # Adds item to list
        self.size += 1                          # Increments size counter
        print("\nSUCCESS: TARGET ITEM {} HAS BEEN ADDED TO SET.\n".format(target_item))
    
    # =================================== ITEM REMOVE METHOD =======================================
    def remove(self, target_item):
        """ Returns success/failure message after removing target item from set. """
        if not self.contains(target_item):
            return print("\nFAILURE: SET DOES NOT CONTAIN ITEM TO REMOVE: \n{}\n".format(target_item))
        self.list.remove(target_item)           # Removes item from list
        self.size -= 1                          # Decrements size counter
        print("\nSUCCESS: TARGET ITEM {} HAS BEEN REMOVED FROM SET.\n".format(target_item))

    # ==================================== SET UNION METHOD ========================================
    def union(self, target_set):
        """ Returns union of parent and target set if both sets share item(s). """
        union_set = SetInstance(self.list)
        for item in target_set:                 # Iterates through items in target set
            if not union_set.contains(item):    # Checks if item does not exist in parent set
                union_set.add(item)             # Adds item to union set if shared
        return union_set

    # ================================= SET INTERSECTION METHOD ====================================
    def intersection(self, target_set):
        """ Returns intersection of parent and target set if both sets do not share item(s). """
        intersection_set = SetInstance()
        for item in target_set:                 # Iterates through items in target set
            if self.contains(item):             # Checks if item exists in parent set
                intersection_set.add(item)      # Adds item to intersection set if not shared
        return intersection_set

    # ================================== SET DIFFERENCE METHOD =====================================
    def difference(self, target_set):
        """ Returns difference between parent and target if item(s) exist(s) in parent but not in target. """
        difference_set = SetInstance(self.list)
        for item in target_set.list:            # Iterates through items in target set
            if difference_set.contains(item):   # Checks if difference (parent) set has item
                difference_set.remove(item)     # Removes item if item exists in parent
            else:
                difference_set.add(item)        # Adds item if item does not exist in parent
        return difference_set

    # ============================== SUBSET IDENTIFICATION METHOD ==================================
    def is_subset(self, target_set):
        """ Returns whether or not target set is subset of parent set. """
        for item in target_set.list:            # Iterates through items in target set
            if not self.contains(item):         # Checks if item does not exist in parent set
                return False
        return True

def main():
    hobbit_set = SetInstance(items=["Frodo", "Merry", "Pippin", "Samwise", "Gandalf"])
    hobbit_set.add("Bilbo")                                     # Adds Bilbo to parent
    hobbit_set.remove("Gandalf")                                # Removes Gandalf from parent
    hobbit_set.union(["Frodo", "Samwise", "Gollum"])            # Returns the two Hobbits
    hobbit_set.intersection(["Merry", "Pippin", "Samwise"])     # Returns the Baggins family
    print(hobbit_set.size)

if __name__ == "__main__":
    main()
"""
NAME:       Aakash Sudhakar
PROJECT:    Call Routing Project
COURSE:     CS3 at Make School (Alan Davis)
"""

# =============================== INITIALIZERS AND IMPORT STATEMENTS =================================


import sys
sys.path.append("../source")
from hashtable import HashTable


# =========================================== MAIN SCRIPT ============================================



class Call_Router_Single_Number(object):
    """ Inputs single number and outputs cost. """
    def __init__(self, number, path):
        FILENAME_ROUTE, ht_cost = path, HashTable()
        with open(FILENAME_ROUTE) as fr:
            for line in fr:
                line = line.strip().split(",")
                ht_cost.set(line[0], float(line[1]))
        self.route_costs = ht_cost                      # Sets numbers with costs to table

        FILENAME_NUMBER, number_list = number, list()
        with open(FILENAME_NUMBER) as fr:
            for line in fr:
                line = line.strip()
                number_list.append(line)
        self.numbers = number_list

    def cost_calculator(self):
        number_list = list()
        for number in self.numbers:
            if self.route_costs.get(number) == None:
                number_list.append(None)
            else:
                number_list.append(self.route_costs.get(number))
        return number_list

class Call_Router_Multiple_Numbers(object):
    """ Inputs list of numbers and outputs costs in array. """
    def __init__(self, number, route_list):
        ht_costs = HashTable()
        for file in route_list:
            with open(file) as fr:
                for line in fr:
                    line = line.strip()
                    line = line.split(",")
                    ht_costs.set(line[0], float(line[1]))
        self.route_costs = ht_costs

        FILENAME_NUMBER, number_list = number, list()
        with open(FILENAME_NUMBER) as fr:
            for line in fr:
                line = line.strip()
                number_list.append(line)
        self.numbers = number_list

    def cost_calculator(self):
        number_list = list()
        for number in self.numbers:
            if self.route_costs.get(number) is None:
                number_list.append(None)
            else:
                number_list.append(self.route_costs.get(number))
        return number_list

if __name__ == "__main__":
    number, path = "./data/phone-numbers-3.txt", "./data/route-costs-4.txt"
    call_item = Call_Router_Single_Number(number, path)
    print(call_item.cost_calculator())














































def NestedDict():
    return defaultdict(lambda: defaultdict(float))

def _find_cost_of_number_with_dict_iter(dataset, input_number):
    """ Helper function that finds cost of number by iterating through standard dictionary. """
    area_code, local_code, personal_code = input_number[0:5], input_number[6:8], input_number[9:12]
    dataset = [j for i in dataset for j in i]
    data_dict = dict()

    for i, j in zip(dataset[0::2], dataset[1::2]):
        data_dict[i] = j

    for key, value in data_dict.items():
        if key in input_number:
            return print("\nCalling {} costs you ${}/minute!".format(input_number, value))
    return print("\nCalling {} costs you nothing!".format(input_number))

def _find_cost_of_number_with_nested_dict(dataset, input_number):
    """ Helper function that finds cost of number by checking nested dictionary (tree). """
    area_code, local_code, personal_code = input_number[0:5], input_number[6:8], input_number[9:12]
    dataset = [j for i in dataset for j in i]
    data_dict = dict()
    tree = NestedDict()

    for i, j in zip(dataset[0::2], dataset[1::2]):
        data_dict[i] = j

    if tree is not None:
        print("yay")

    # for key, value in data_dict.items():
    #     tree[key] = value
    
    print(tree)

def main():
    ROUTES_PATH = "./data/route-costs-4.txt"
    CALLS_PATH = "./data/call-costs-3.txt"
    NUMBERS_PATH = "./data/phone-numbers-3.txt"
    formatted_routes_data, formatted_calls_data = list(), list()

    with open(ROUTES_PATH) as fr:           # Imports route costs data
        routes_data = fr.readlines()
    for item in routes_data:
        formatted_routes_data.append(item.strip().split(","))

    with open(NUMBERS_PATH) as fr:          # Imports phone number data
        numbers_data = fr.readlines()

    _find_cost_of_number_with_dict_iter(formatted_routes_data, "+1415246")

# if __name__ == "__main__":
#     main()
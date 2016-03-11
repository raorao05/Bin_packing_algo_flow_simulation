'''
This is the simulation of flow of First_Fit_Decreasing.
Through this simulation, it will expose the flow of how FFD works.
It does not take into account the performance, speed of alth.
'''

import random

class Bin():
    def __init__(self, max_capa):
        self.bin_list = []
        self.capacity = 0
        # Max_capa of each bin
        self.max_capa = max_capa
    
    def bin_append(self, item):
        self.bin_list.append(item)
        self.capacity += item
    
    def __str__(self):
        return 'Bin (current_capacity=%d, items=%s, max_capacity=%s)' % (self.capacity, str(self.bin_list), self.max_capa)

def item_assignment(demand):
    '''
    Demand is the list of the requested capacities that need to be fitted in to bins. Each requested capacity is not bigger than 10
    In this simulation, there are 4 bin with different maximum capacity.
    We will see how the demand will fit these 4 bins in FFD.
    '''
    # Sorting the demand list
    demands = sorted(demand, reverse = True)
    bins = []
    
    # Assign the random max capacity of each bin.
    # The max_capa is not bigger than 20
    for i in range(4):
        ran = random.randint(1,20)
        bins.append(Bin(ran))
    for index, bin in enumerate(bins):
        print "Index: %s, bin: %s" %(index, bin)
    print "\nThe list of demands: %s \n" % demands
    
    # Starts fitting demands to bins
    for item in demands[:]:
        print ("%s Starting a new fitting %s" %(('*'*30), ('*'*30)))
        print ("\nThe requested capacity is going to be checked: %s" %item)
        for index, bin in enumerate(bins):
            print "\n******** BEFORE FITTING"
            print "Bin: %s, Value:%s\n" %(index, bin)
            if bin.capacity + item <= bin.max_capa:
                bin.bin_append(item)
                demands.remove(item)
                print "\n******** AFTER FITTING"
                print "Bin: %s, Value:%s" %(index, bin)
                print "\nThe demaining requested capacities: %s \n" %demands
                break
        
        else:
            # raise NotImplementedError
            print "\n!!!!!OOP!!!!! There is NO bin eligible for the request \n"
            pass

    return bins

def testing(demand_list, max_capa=None):
    print "%s Starting %s \n " %(('*'*30), ('*'*30))
    bins = item_assignment(demand_list)
    print '\n%s RESULT SUMMARY %s' %(('*'*30), ('*'*30))
    print 'The simulation using', len(bins), 'bins:'
    for bin in bins:
        print bin
        
if __name__ == '__main__':

    random_demand_list = [random.randint(i, 10) for i in range(1, 10)]
    testing(random_demand_list)

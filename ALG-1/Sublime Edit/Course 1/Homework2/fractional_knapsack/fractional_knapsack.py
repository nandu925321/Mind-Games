# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here - takes O(2n)
    # figured this would be better than any sorting algorithm that would take log(n) time
    # if n = 10000 2n is 20000 but if sorted it would be 40 k 
    value_per_weight = [values[i]/weights[i] for i in range(len(weights))]

    for i in range(n):
    	if(capacity == 0):
    		return value
    	
    	inde = value_per_weight.index(max(value_per_weight))
    	value_weight = value_per_weight[inde]
    	weight_v_weight = weights[inde]
    	max_v = values[inde]
    	a = min(weight_v_weight,capacity)
    	value = value + value_weight * a

    	capacity = capacity - a
    	# not removing the elements as code might be prone to bugs while array resizing and indexing
    	weights[inde] = 0
    	values[inde] = 0
    	value_per_weight[inde] = 0





    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

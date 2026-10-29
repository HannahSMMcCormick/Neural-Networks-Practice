
inputs = [1.2,5.1,2.1]
weights = [[3.1,2.1,8.7],[2.3,1.5,8.9],[2.5,6.8,9.4]]
bias = [2,6,3]

output = 0 


curr_layre_out = []

for neuron,bias in zip(weights,bias):
    neuron_out = 0
    
    for n , weight in zip(inputs,neuron):
        
        neuron_out += n * weight
    neuron_out += bias
    curr_layre_out.append(neuron_out)
    
print(curr_layre_out)
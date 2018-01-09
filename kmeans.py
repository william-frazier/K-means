#CS451
#HW5: K-Means Algorithm
#William Frazier and Alex Berry
 
import random
import csv
import numpy as np
import matplotlib.pyplot as plt

def read_file(filename):
    """
   reads the data set and converts it into a list
   with elements as 16 element numpy vectors, one
   for each country
   """
   
    x = []
    country = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, quotechar='|')
        next(reader)
        for row in reader:
            country.append(row[0])
            entry = [float(i) for i in row[1:]]
            x.append(np.array(entry))
    return (x, country)
 
def squared_distance(entryA, entryB):
    """
    Computes the squared distance between two vectors.
    """
    difference = entryA - entryB
    return sum(difference * difference)
   
def closest_centroid(point, centroids):
    """
    Returns the index of the centroid closest to point xi.
    """
    closest_k = 0
    for i in range(len(centroids)):
        distance = squared_distance(point, centroids[i])
        if i == 0:
            closest = distance
        if distance < closest:
            closest = distance
            closest_k = i
    return closest_k
   
def centroid_assignment(x, mu):
    """
    Assigns each data point to its closest centroid.
    Returns c, the list of cluster indices. Each index
    in c corresponds to the point at the same index of x.
    """
    c = []
    for i in range(len(x)):
        k_of_point = closest_centroid(x[i], mu)
        c.append(k_of_point)
    return c
   
def update_mu(x, c, k):
    """
    Updates the k centroids by computing the average of
    the data points assigned to each centroid. Returns mu,
    the list of current centroids.
    """
    mu = []
    for i in range(k):
        total = 0
        count = 0
        #loop through all centroid clusters
        for point in range(len(c)):
            #check every point in c
            if c[point] == i:
                #if point is assigned to this cluster
                total += x[point]
                #add its data to the average
                count += 1
        mu.append(total / count)
    return mu
       
def cost_func(x, c, mu):
    """
    Computes the cost function J given x, c, and mu.
    """
    cost = 0
    for i in range(len(x)):    
        cost += squared_distance(x[i], mu[c[i]])
    return cost/len(x)
   
def k_means(K, x, iterations):
    """
    Runs k-means algorithm given K, x, and # of iterations. The
    max # of iterations should be 500. Repeats centroid assignment
    and updating mu until convergence or iteration limit. Returns 
    the cost value at convergence.
    """
    mu = []
    for element in random.sample(x,K):
        #initialize mu as K random dat points
        mu.append(element)
    old_c = None
    #initialize old_c as null to preclude equality with new_c
    for j in range(iterations):
        new_c = centroid_assignment(x, mu)
        mu = update_mu(x, new_c, K)
        if new_c == old_c:
            #checking for convergence
            cost = cost_func(x, new_c, mu)
            return (cost, new_c)
        old_c = new_c    
   
def country_clusters(K, c, countries):
    """
    Given K, c, and the list of countries, returns a list
    of lists with each sublist representing one of the K
    clusters. The elements of the sublists are countries in
    a particular cluster.
    """
    country_list = []
    for i in range(K+1):
        country_list.append([])
        #create a list with K+1 empty sublists
    for j in range(len(c)):
        country_list[c[j]].append(countries[j])
        #for each cluster, append appropriate countries
    return country_list

def graph_cost_vs_k():
    """
    Graphs the cost value as a function of k.
    """
    plt.plot(K_list, cost_list)
    plt.ylabel('Cost')
    plt.xlabel('K value')
    plt.show()
    
def write_text_output():
    """
    Writes output of kmean_run.py into a text file called
    'country_cluester.txt'.
    """
    with open('country_clusters.txt','w') as output_file:
        for cluster in output_list:
            output_file.write(cluster+'\n')
 
max_K = 10
(x, country) = read_file('country.csv')
cost_list = []
K_list = []
for K in range(max_K):
    (cost, c)= k_means(K+1, x, 100)
    cost_list.append(cost)
    K_list.append(K)

clustered_countries = country_clusters(K, c, country)
output_list =[]
for i in range(len(clustered_countries)):
    cluster_format = "Cluster " + str(i+1) + " is: " + str(clustered_countries[i])
    output_list.append(cluster_format)
    #print(cluster_format) #uncomment to print each cluster as kmeans runs
    
graph_cost_vs_k()
#write_text_output() #uncomment to write output to a text file
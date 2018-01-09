#CS451
#k_means_run.py
#Alex Berry and Will Frazier
 
import csv_reader as cr
import kmeans
import matplotlib.pyplot as plt

def graph_cost_vs_k():
    plt.plot(K_list, cost_list)
    plt.ylabel('Cost')
    plt.xlabel('K value')
    plt.show()
    
def write_text_output():
    with open('country_clusters.txt','w') as output_file:
        for cluster in output_list:
            output_file.write(cluster+'\n')
 
max_K = 10
#iteration = int(input('number of iterations = '))
(x, country) = cr.read_file('country.csv')
cost_list = []
K_list = []
for K in range(max_K):
    (cost, c)= kmeans.k_means(K+1, x, 100)
    cost_list.append(cost)
    K_list.append(K)

clustered_countries = kmeans.country_clusters(K, c, country)
output_list =[]
for i in range(len(clustered_countries)):
    cluster_format = "Cluster " + str(i+1) + " is: " + str(clustered_countries[i])
    output_list.append(cluster_format)
    print(cluster_format)
    
graph_cost_vs_k()
write_text_output()
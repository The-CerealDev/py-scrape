import pandas as pd


link_list = 'linksv2_cleaned.txt'
csv_file = 'pre_final_blackrock.csv'

'''
Heres how i want it to work:
    its going to check all the links in the txt file that contains only blackrock links
    then its going to compare and remove the rows in the dataframe that are not blackrock
    then it pushes the new one into a new csv file
'''


with open(link_list, 'r') as rfile:
    blackrock_links = [link.strip() for link in rfile.readlines()]

current_var = pd.read_csv(csv_file)  
# this is going to create the dataframe from the csv file #
links = list(current_var["Link"].str.strip())

# this finds all the links in the csv file #

non_blackrock_index = {''}

for ind,link in enumerate(links):
    
    if link not in blackrock_links:
        non_blackrock_index.add((ind,link))
        
    
for ind in non_blackrock_index:
    print(ind)

'''

THIS IS COMPLETELY USELESS AS THERE WAS ALREADY BLACKROCK VALIDATION IN PYSCYRAPE

'''


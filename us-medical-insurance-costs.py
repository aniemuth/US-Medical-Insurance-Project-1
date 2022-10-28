#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[13]:


import csv


# In[14]:


## Points of Intrest:
    #Regions with most smokers
    #Avg age of people with at least one child
    #Oldest smoker vs oldest nonsmoker
    #Avg cost insurance by region


# In[15]:


regions = []
ages = []
num_children = []
smoker_status = []
ins_charges = []
bmi = []
sex = []


# In[16]:


def load_list_data(lst, csv_file, column_name):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column_name])
        return lst


# In[17]:


load_list_data(regions, "insurance.csv", "region")
load_list_data(ages, "insurance.csv", "age")
load_list_data(num_children, "insurance.csv", "children")
load_list_data(smoker_status, "insurance.csv", "smoker")
load_list_data(ins_charges, "insurance.csv", "charges")
load_list_data(bmi, "insurance.csv", "bmi")
load_list_data(sex, "insurance.csv", "sex")


# In[18]:


#finding list of unique regions
unique_regions = []
def unique_regions_lst():
    for region in regions:
        if region not in unique_regions:
            unique_regions.append(region)
    return unique_regions
unique_regions_lst()
print(unique_regions)


# In[19]:


#getting number of smokers and nonsmokers
def count_smokers():
    count_smoker =0
    count_non = 0
    for smokers in smoker_status:
        if smokers == "yes": count_smoker += 1
        elif smokers == "no": count_non += 1
    return count_smoker, count_non
smoke, non = count_smokers()
print("The number of smokers is " + str(non))
print("The number of nonsmokers is " + str(smoke))


# In[20]:


#finding number of smokers in each region
smoker_regions = zip(smoker_status, regions)
#print(list(smoker_regions))
def regions_with_most_smokers():
    smk_count_sw = 0
    smk_count_se = 0
    smk_count_nw = 0
    smk_count_ne = 0
    for row in smoker_regions:
            if row[0] == "yes" and row[1] == "southwest":
                smk_count_sw += 1
            if row[0] == "yes" and row[1] == "southeast":
                smk_count_se += 1
            if row[0] == "yes" and row[1] == "northwest":
                smk_count_nw += 1
            if row[0] == "yes" and row[1] == "northeast":
                smk_count_ne += 1
    return smk_count_sw, smk_count_se, smk_count_nw, smk_count_ne
total_smokers_regions = regions_with_most_smokers()              
print("The total number of smokers in the southwest is " + str(total_smokers_regions[0]))
print("The total number of smokers in the southeast is " + str(total_smokers_regions[1]))
print("The total number of smokers in the northwest is " + str(total_smokers_regions[2]))
print("The total number of smokers in the northeast is " + str(total_smokers_regions[3]))


# In[21]:


#finding average age of people with at least 1 child
parental_age = zip(ages, num_children)
#print(list(parental_age))
parent_age = []
def parental_age_lst():
    for row in parental_age:
        if row[1] != "0": parent_age.append(row[0])
    return parent_age
parental_age_lst()
modified_parent_age = [int(i) for i in parent_age]
from statistics import mean
avg_parent_age = mean(modified_parent_age)
avg_parent_age_rounded = round(39.78010471204188, 0)
print(avg_parent_age_rounded)


# In[34]:


#finding oldest smoker
age_smoke_status = zip(ages, smoker_status)
#print(list(age_smoke_status))
smoker_ages = []
def ages_who_smoke():
    for row in age_smoke_status:
        if row[1] == "yes": smoker_ages.append(row[0])
ages_who_smoke()
modified_smoker_ages = [int(i) for i in smoker_ages]
def oldest_smoker():
    oldest_smoker_age = 0
    for age in modified_smoker_ages:
        if age >  oldest_smoker_age: oldest_smoker_age = age
    return oldest_smoker_age
smoker_age = oldest_smoker()
print("The oldest smoker is " + str(smoker_age))


# In[43]:


#finding oldest nonsmoker
age_smoke_status = zip(ages, smoker_status)
nonsmoker_ages = []
def ages_who_dont_smoke():
    for row in age_smoke_status:
        if row[1] == "no": nonsmoker_ages.append(row[0])
ages_who_dont_smoke()
modified_nonsmoker_ages = [int(i) for i in nonsmoker_ages]
def oldest_nonsmoker():
    oldest_nonsmoker_age = 0
    for age in modified_nonsmoker_ages:
        if age >  oldest_nonsmoker_age: oldest_nonsmoker_age = age
    return oldest_nonsmoker_age
nonsmoker_age = oldest_nonsmoker()
print("The oldest nonsmoker is " + str(nonsmoker_age))


# In[99]:


#finding charges by region
charges_by_region = zip(ins_charges, regions)
#print(list(charges_by_region))
def regional_charges_lst_to_modify():
    charges_sw = []
    charges_se = []
    charges_nw = []
    charges_ne = []
    for row in charges_by_region:
        if row[1] == "southwest": charges_sw.append(row[0])
        if row[1] == "southeast": charges_se.append(row[0])
        if row[1] == "northwest": charges_nw.append(row[0])
        if row[1] == "northeast": charges_ne.append(row[0])
    return charges_sw, charges_se, charges_nw, charges_ne
total_charges_sw, total_charges_se, total_charges_nw, total_charges_ne = regional_charges_lst_to_modify()
modified_regional_charges_sw = [float(i) for i in total_charges_sw]
modified_regional_charges_se = [float(i) for i in total_charges_se]
modified_regional_charges_nw = [float(i) for i in total_charges_nw]
modified_regional_charges_ne = [float(i) for i in total_charges_ne]
def regional_charges(charges):
    charges_total = 0
    for charge in charges: charges_total += charge
    return charges_total / len(charges)
avg_charge_sw = regional_charges(modified_regional_charges_sw)
avg_charge_se = regional_charges(modified_regional_charges_se)
avg_charge_nw = regional_charges(modified_regional_charges_nw)
avg_charge_ne = regional_charges(modified_regional_charges_ne)
print("The average charge for the southwest is $" + str(round(avg_charge_sw, 2)))
print("The average charge for the southeast is $" + str(round(avg_charge_se, 2)))
print("The average charge for the northwest is $" + str(round(avg_charge_nw, 2)))
print("The average charge for the northeast is $" + str(round(avg_charge_ne, 2)))


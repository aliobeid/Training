# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# <a href="https://colab.research.google.com/github/aliobeid/algos/blob/master/Algorithms.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
# %% [markdown]
# # Permutations of a String
# 

# %%

def perms(word):
  if len(word)<=1:
    return word
  else:
    lst = []
    for i in range(len(word)):
      f = word[i]
      r = word[0:i]+word[i+1:]
      for perm in perms(r):
        lst.append(f+perm)
    return lst 



# %%
def permutations(word):
    if len(word) <=1:
        return word
    else:
        lst = []
    for p in permutations(word[1:]):
        for i in range(len(word)):
            lst.append(p[:i]+word[0:1]+p[i:])
    return lst


# %%
get_ipython().run_cell_magic('timeit', '', 'permutations("abcd")')


# %%
get_ipython().run_cell_magic('timeit', '', 'perms("abcd")')


# %%


# %% [markdown]
# # Most frequent integer of an integer array

# %%
array= [1,9,8,6,5,3,4,4,4,5,3,5,2,3,5,4]

def most_freq_int(int_array):
    count_dict = {}
    for i in int_array:
        if i in count_dict:
            count_dict[i] +=1
        else:
            count_dict[i] = 1 
    max_counter = -1 
    most_freq = None 
    for int_val in count_dict.keys():
        if count_dict[int_val] > max_counter:
            max_counter = count_dict[int_val]
            most_freq = int_val   
    return most_freq



# %%
most_freq_int(array)


# %%
count_dict = {}
for i in array:
    if i in count_dict:
        count_dict[i] +=1
    else:
        count_dict[i] = 1
        
max_counter = -1 
most_freq = None 
for int_val in count_dict.keys():
    if count_dict[int_val] > max_counter:
        max_counter = count_dict[int_val]
        most_freq = int_val


# %%
count_dict


# %%
most_freq


# %%



#!/usr/bin/env python
# coding: utf-8

# In[1]:


1 + 1


# In[2]:


print(1 + 1)


# In[3]:


runs_scored = 4


# In[4]:


runs_scored


# In[5]:


3*runs_scored


# In[6]:


runs_scored = runs_scored + 3


# In[7]:


runs_scored


# In[8]:


stolen_bases = 21 # int


# In[9]:


pitch_mph = 94.4 # float


# In[10]:


starting_p = 'Noah Syndergaard'
starting_c = "Travis d'Arnaud"


# In[11]:


type(starting_p)


# In[12]:


type(stolen_bases)


# In[13]:


starters = f'{starting_p}, {starting_c}, etc.'
starters


# In[14]:


"it's outta here!".upper()


# In[15]:


'BJ Upton'.replace('BJ', 'Melvin')


# In[16]:


'mike trout'.capitalize()


# In[17]:


'  mike trout'.lstrip()


# In[22]:


team1_runs = 6


# In[23]:


team2_runs = 4


# In[24]:


team1_won = team1_runs > team2_runs


# In[25]:


team2_won = team1_runs < team2_runs


# In[26]:


teams_tied = team1_runs == team2_runs


# In[27]:


teams_did_not_tie = team1_runs != team2_runs


# In[28]:


type(team1_won)


# In[29]:


teams_did_not_tie


# In[30]:


shootout = (team1_runs > 8) and (team2_runs > 8)


# In[31]:


at_least_one_good_team = (team1_runs > 8) or (team2_runs > 8)


# In[32]:


pitching_duel = not ((team1_runs > 2) or (team2_runs > 2))


# In[33]:


meh = not (shootout or at_least_one_good_team or pitching_duel)


# In[39]:


if team1_won:
    message = "Nice job team 1!"
elif team2_won:
  message = "Way to go team 2!!"
else:
  message = "must have tied!"


# In[40]:


message


# In[41]:


roster_list = ['clayton kershaw', 'mookie betts', 'cody bellinger']


# In[42]:


roster_list[0]
roster_list[0:2]
roster_list[-2:]


# In[43]:


roster_dict = {'P': 'clayton kershaw',
               'RF': 'mookie betts',
               'CF': 'cody bellinger'}


# In[44]:


roster_dict['RF']
roster_dict['1B'] = 'max muncy'


# In[45]:


pos = 'RF'
roster_dict[pos]


# In[46]:


p, rf = ['clayton kershaw', 'mookie betts']


# In[47]:


p = 'clayton kershaw'
rf = 'mookie betts'


# In[48]:


roster_list = ['clayton kershaw', 'mookie betts', 'cody bellinger']


# In[49]:


roster_list_upper = ['', '', '']
i = 0
for player in roster_list:
    roster_list_upper[i] = player.title()
    i = i + 1


# In[50]:


roster_list_upper


# In[51]:


for x in roster_dict:
    print(f"position: {x}")


# In[52]:


for x in roster_dict:
   print(f"position: {x}")
   print(f"player: {roster_dict[x]}")


# In[53]:


for x, y in roster_dict.items():
    print(f"position: {x}")
    print(f"player: {y}")


# In[54]:


roster_list
roster_list_proper = [x.title() for x in roster_list]
roster_list_proper


# In[55]:


roster_list_proper_alt = [y.title() for y in roster_list]


# In[56]:


type([x.title() for x in roster_list])
[x.title() for x in roster_list][:2]


# In[57]:


roster_last_names = [full_name.split(' ')[1] for full_name in roster_list]
roster_last_names


# In[58]:


roster_c_only = [
    x.title() for x in roster_list if x.startswith('c')]
roster_c_only


# In[59]:


salary_per_player = {
    'clayton kershaw': 31000000,
    'mookie betts': 27000000,
    'cody bellinger': 11500000}


# In[60]:


salary_m_per_upper_player = {
    name.upper(): salary/1000000 for name, salary in salary_per_player.items()}


# In[61]:


sum([1, 2, 3])
sum([salary for _, salary in salary_per_player.items()])


# In[62]:


len(['clayton kershaw', 'mookie betts', 'cody bellinger'])


# In[63]:


strikes_needed = len(
    ['clayton kershaw', 'mookie betts', 'cody bellinger'])


# In[64]:


strikes_needed
4 + len(['clayton kershaw', 'mookie betts', 'cody bellinger'])


# In[67]:


def hr_sweetspot(launch_angle, exit_velocity):
    """
    multi line strings in python are between three double quotes

    it's not required, but the convention is to put what the fn does in one of
    these multi line strings (called "docstring") right away in function

    when you type hr_sweetspot? in the REPL, it shows this docstring

    this function takes launch angle, exit velocity and returns a bool
    indicating whether hit is in the sweet spot for home runs
    """
    return (25 <= launch_angle <= 35) and (exit_velocity >= 95)


# In[68]:


def noisy_hr_sweetspot(launch_angle, exit_velocity):
    """
    this function takes launch angle, exit velocity and returns a bool
    indicating whether hit is in the sweet spot for home runs

    it also prints launch_angle
    """
    print(launch_angle)
    return (25 <= launch_angle <= 35) and (exit_velocity >= 95)


# In[69]:


hr_sweetspot(30, 98)
noisy_hr_sweetspot(29, 92)


# In[70]:


def hr_sweetspot_wdefault(launch_angle=14, exit_velocity=68):
    """
    this function takes launch angle, exit velocity and returns a bool
    indicating whether hit is in the sweet spot for home runs

    if a value for launch angle or exit velocity is not entered, it'll default
    to the league averages for 2019
    """
    return (25 <= launch_angle <= 35) and (exit_velocity >= 95)


# In[71]:


hr_sweetspot_wdefault(launch_angle=30)
hr_sweetspot_wdefault(31, 112)
hr_sweetspot_wdefault(31)
hr_sweetspot_wdefault(exit_velocity=115)


# In[72]:


def do_to_list(working_list, working_fn, desc):
    """
    this function takes a list, a function that works on a list, and a
    description

    it applies the function to the list, then returns the result along with
    description as a string
    """

    value = working_fn(working_list)

    return f'{desc} {value}'


# In[73]:


def last_elem_in_list(working_list):
    """
    returns the last element of a list.
    """
    return working_list[-1]


# In[74]:


infield = ['1B', '2B', '3B', 'P', 'C', 'SS']


# In[75]:


do_to_list(infield, last_elem_in_list, "last element in your list:")
do_to_list([1, 2, 4, 8], last_elem_in_list, "last element in your list:")


# In[76]:


do_to_list(infield, len, "length of your list:")


# In[77]:


do_to_list([2, 3, 7, 1.3, 5], lambda x: 3*x[0], "first element in your list times 3 is:")


# In[78]:


import os  # note: normally you'd import this at the top of your file


# In[79]:


os.cpu_count()


# In[80]:


from os import path  # again, normally you'd import this at the top


# In[81]:


DATA_DIR = '/Downloads/ltcwbb/ltcwbb-files/code'


# In[82]:


path.join(DATA_DIR, 'players.csv')


# In[ ]:





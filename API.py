from github import Github

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# create a Github instance:
# using username and password
username = input("Enter a username inside quoteation marks: ")
password = input("Enter your password inside quotation marks: ")
g = Github(username, password)

class Language:
  def __init__(self, name, count):
    self.name = name
    self.count = count

languages = []

for repo in g.get_user().get_repos():
    # Prints names of users repos
    print("Name of repo: " + repo.name)
    # Prints the number of stars that repo has
    print("Number of stars: " + str(repo.stargazers_count))
    # Prints the language used in that repo
    print("Language used: " + str(repo.language))
    for commit in repo.get_commits():
        print commit.commit.author.date
        print commit.commit.author        
    print("\n")



y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
 
plt.show()
    
username = "null"
password = "null"

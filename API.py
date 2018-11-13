from github import Github

# First create a Github instance:

# using username and password
username = input("Enter a username inside quoteation marks: ")
password = input("Enter your password inside quotation marks: ")
g = Github(username, password)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
    print(repo.stargazers_count)
    print(repo.language)
    print("\n")
    
username = "null"
password = "null"

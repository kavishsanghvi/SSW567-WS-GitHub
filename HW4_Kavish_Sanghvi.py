"""
author: @kavishsanghvi
@purpose: to fetch and store the count of commit of the repository from GitHub using RESTful services APIs
"""

import requests
import json

def repo(u_id):
    """ fetch and count the commits of the repository from GitHub
    
    :param uid_id: GitHub username
    :type: str
    :return: list
    """
    
    repo_name_url = requests.get(f"https://api.github.com/users/{u_id}/repos") 
    repo_name = repo_name_url.json() 
    output = []
    for i in repo_name:
        repos = i.get("name")
        repo_commit_url = requests.get(f"https://api.github.com/repos/{u_id}/{repos}/commits")
        repo_commit = repo_commit_url.json()   
        com = 0
        for item in repo_commit:
            if item in repo_commit: 
                com = com + 1  
        output.append(f"Repo: {repos}, Commits: {com}")
    return output

def main():
    user_input = input("Enter your GitHub username: ")
    return repo(user_input)

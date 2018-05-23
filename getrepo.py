from github import Github

# Generate a token at https://github.com/settings/tokens
token = '621fe62c181a4a4a26ac5c312970c34bae2d3b69'

g = Github(token)

repo_name = 'kunumi/numi'
repo = g.get_repo(repo_name)
collaborators = repo.get_collaborators()
commits = repo.get_commits()

for commit in commits:
    print commit.author.name

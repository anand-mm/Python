import gitlab

# Replace "http://gepnic-devops.nic.in" with your GitLab instance URL
# Replace "glpat-s4ySKJTcj5sC7YB_Rqo-" with your private access token
gl = gitlab.Gitlab(url="http://gepnic-devops.nic.in/gitlab", private_token="glpat-s4ySKJTcj5sC7YB_Rqo-")

# Make sure to authenticate with GitLab before listing issues
gl.auth()

# List open issues
open_issues = gl.issues.list(state='opened')

projects = gl.projects.list()

project_id = 219

project = gl.projects.get(project_id)

issue = project.issues.create({'title': 'I have a bug',
                               'description': 'Something useful here.'})

branches = project.branches.list()

for branch in branches:
    print(branch)

# commits = project.commits.list()

# Print the open issues
# for issue in open_issues:
#     print(issue)

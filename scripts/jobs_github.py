from github import Github

access_token = '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'
LINE = '-' * 80

g = Github(access_token)
repo = g.get_repo("backend-br/vagas")

open_issues = repo.get_issues(state='open')
tamanho_repo = 1
for issue in open_issues:
    lista_labels = []
    for label in issue.labels:
        lista_labels.append(label.name)
        if 'Sênior' not in lista_labels and 'Pleno' not in lista_labels:
            print(f'{issue.created_at} - {issue.title} - {issue.html_url}\n{lista_labels}')
            tamanho_repo += 1
print(f'Tamanho...{open_issues.totalCount}')

import git,os,stat,shutil
cwd=os.path.join(os.getcwd(), "repo")
def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)
if os.path.exists(cwd):
    shutil.rmtree(cwd, onerror=remove_readonly)
git.Repo.clone_from("https://github.com/nokokiii/Monkey_Tower_Defence/", cwd, branch="master")
repo = git.Repo("./repo")
tree = repo.tree()
save=0
for blob in tree:
    commit = next(repo.iter_commits(paths=blob.path, max_count=1))
    save+=commit.committed_date
if os.path.exists("last.txt"):
    with open('last.txt', 'r') as f:
        lines=f.read()
        if lines!=str(save):
            print(lines,str(save))
            shutil.rmtree(os.path.join(os.getcwd(), "game"), onerror=remove_readonly)
            shutil.copytree(cwd, os.path.join(os.getcwd(), "game"))
            with open('last.txt', 'w') as f:
                f.write(str(save))
else:
    with open('last.txt', 'w') as f:
        f.write(str(save))
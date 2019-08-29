from plover_vcs.vcs.exception_decorator import wrap_exceptions
from plover_vcs.vcs.vcs_service import VcsService
from git import Repo


@wrap_exceptions()
class GitVcsService(VcsService):
    def __init__(self, repo: str):
        self.repo = Repo.init(repo)

    def add(self, file: str):
        self.repo.git.add(file)

    def commit(self, message: str):
        self.repo.commit(str)

    def pull(self):
        self.repo.git.pull()

    def switch(self, branch: str):
        self.repo.git.checkout(branch)

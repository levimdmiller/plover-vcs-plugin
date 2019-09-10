from plover_vcs.vcs.exception_decorator import wrap_exceptions
from plover_vcs.vcs.vcs_service import VcsService
from git import Repo


@wrap_exceptions()
class GitVcsService(VcsService):
    def __init__(self, repo: str):
        super().__init__(repo)
        self.repo = Repo.init(repo)

    def commit(self, file: str, message: str):
        self.repo.git.pull()
        self.repo.git.add(file)
        self.repo.commit(str)
        self.repo.git.push()

    def diff(self, file: str) -> str:
        return self.repo.git.diff(file)

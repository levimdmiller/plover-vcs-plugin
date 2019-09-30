from plover_vcs.vcs.git_vcs_service import GitVcsService
from plover_vcs.vcs.vcs_service import VcsService

IMPLEMENTATIONS = {
    'git': GitVcsService
}


class VcsServiceFactory:
    def __init__(self, config_manager):
        self.config_manager = config_manager

    def create(self, repo: str) -> VcsService:
        return IMPLEMENTATIONS[self.config_manager.config](repo)

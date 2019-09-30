from plover_vcs.file_watcher import FileWatcher
from plover_vcs.message_generator.git_diff_message_generator import GitSingleFileDiffMessageGenerator
from plover_vcs.vcs.vcs_service_factory import VcsServiceFactory
from plover_vcs.vcs_config import CONFIG_MANAGER


def run():
    message_gen = GitSingleFileDiffMessageGenerator()
    vcs_service_factory = VcsServiceFactory(CONFIG_MANAGER)
    file_watcher = FileWatcher(vcs_service_factory, message_gen)
    for d in CONFIG_MANAGER.config.dictionaries:
        file_watcher.watch_file(d)

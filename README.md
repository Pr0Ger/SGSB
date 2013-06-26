
This is a simple tool to backup game saves.

## Commands

- `sgsb.py backup` — Backup saves for games selected in task.ini
- `sgsb.py list` — Show list of games
- `sgsb.py restore` — Restore saves for games selected in task.ini
	- `--all` — Ignore task.ini and backup/restore all available games

## task.ini example

	[Braid]
	backup = True
	restore = True

## Writing new plugin

Files with plugins classes should be placed in the `plugins` directory.

```python
class FooPlugin(BasePlugin):
	Name = "Game name"
	dependencies = ["Games for Windows Live profile"]
	support_os = ["Windows", "Darwin"]  # platform.system()

	def init(self):
		# Initialization of plugin
		pass

	# _ is instance of `BackupFile`
	def backup(self, _):
		# This function will be runned while backup procedure
		pass

	def restore(self, _):
		# This function will be runned while restore procedure
		pass

	def detect(self):
		# This function used for detecting presense of game in the system. Should return `True` or `False`
		return False
```

`BackupFile` API:

- add_files(id, path, files)
- add_folder(id, path, folder)
- restore_files(id, path, files)
- restore_folder(id, path, folder)

`id` is an identificator used to separate different parts of backup (for example saves and config files from different directories)

`path` is a path to files or folder that should be backuped

`files` is a string or list of strings that should be saved from `path` directory
`folder` is a string with name of folder that should be backuped (for example, if we want to backup `/home/pr0ger/foo` we should call `add_folder('foo_directory', '/home/pr0ger', 'foo')`)
import sublime, sublime_plugin, os, subprocess

class QuicklookCommand(sublime_plugin.WindowCommand):
	def run(self, paths=[]):
		plugin_dir = os.path.dirname(os.path.realpath(__file__))
		applescript_path = os.path.join(plugin_dir, 'quicklook.applescript')
		os.chmod(applescript_path, 0o755)
		path = self.get_path(paths)
		subprocess.Popen([applescript_path, path])

	def get_path(self, paths):
		if paths:
			return paths[0]
		elif self.window.active_view():
			return self.window.active_view().file_name()
		elif self.window.folders():
			return self.window.folders()[0]
		else:
			return '.'

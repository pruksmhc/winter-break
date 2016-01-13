import sublime, sublime_plugin

class find_definitions_and_copy(sublime_plugin.TextCommand, sublime_plugin.WindowCommand):
	def run(self, edit):
		#change the color of the entire texts. 
		content = self.view.substr(sublime.Region(0, self.view.size()))
		print("CONTENT'")
		print(content)
		find_words(self.view.window())
		newFile = self.window.new_file()
		newFile.run_command("New",{"textBuffer": contents})
	def find_words(self, window):
   	    print("Finding all intstances of the word acrossWEFtext files in the repo.")
   	    for selection in self.view.sel():
   	    	if selection.empty():
   	    		selection = self.view.word(selection)
   	    		text = self.view.substr(selection)
   	    print(text)
   	    locations = window.lookup_symbol_in_index(text)
   	    print(locations)

class New(sublime_plugin.TextCommand):
	def run(self, edit, textBuffer):
		self.view.insert(edit, 0, textBuffer)
		
	
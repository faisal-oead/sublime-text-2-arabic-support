# -*- coding: utf-8 -*-

# This work is licensed under the GNU Public License (GPL).
# To view a copy of this license, visit http://www.gnu.org/copyleft/gpl.html
# Written by praveen vijayan (praveenvijayan)
# Written  by faisal oead 

import sublime, sublime_plugin, sys
import arabic_reshaper

class bidiCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = sublime.Region(0, self.view.size())
		bidiRegion(region, self.view, edit)

class bidiselectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selectionSet = self.view.sel()
		for selectionRegion in selectionSet:
			bidiRegion(selectionRegion, self.view, edit)

def bidiRegion(region, view, edit):
	txt = view.substr(region)
	reshaped_text = arabic_reshaper.reshape(txt)
	view.replace(edit, region, reshaped_text)
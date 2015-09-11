import pypandoc
from .mkcException import mkcException

(from_formats,to_formats) = pypandoc.get_pandoc_formats()

class StrFormat(object):
	"""Class defining a string, PLUS mention of its lang (ie LaTeX, Markdown, etc.)"""
	def __init__(self, string, lang=None):
		if lang is not None  and  lang not in from_formats:
			raise mkcException( "The lang "+ lang+" cannot be converted by Pandoc.")
		self.string=string
		self.lang=lang
		
	def convertTo(self, lang=None):
		if lang is not None  and lang not in to_formats:
			raise mkcException( "The string '"+self.string+"' cannot be converted to "+lang+" by Pandoc.")
		
		if lang is not None and self.lang != lang:
			return pypandoc.convert( self.string, format=self.lang, to=lang)
		else:
			return self.String
		
	def __str__(self):
		return self.string
	
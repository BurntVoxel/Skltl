# Python 3
def ReadMe():
	About = \
		"\n# OneFile: Compile CSS imports. \n" + \
		"# This script assembles CSS that has been sharded with imports. \n" + \
		"# Note that for now it is only meant for relative paths. \n" + \
		"# Remote paths are a work in progress. \n\n"
		# Eventually I'd like to be able to merge into the HTML file.
		# Maybe even gather JS and images too, but that's ambitious.
	print(About)

DefaultInput = "CSS/Skltl.css"
DefaultOutput = "Skltl.OneFile.css"


import os

def TrimImportPath(x):
	# Trimming "@import url('foo')" into "foo"
	x = x.strip().removeprefix("@import")
	x = x.strip().removeprefix("url(").removesuffix(");")
	x = x.strip(' "\'')
	return x

def JoinPath(Path, Line):
	# to my knowledge `os.path.join` just handles relative paths like `../foo` fine 
	x = os.path.join( os.path.dirname(Path), Line)
	return x

def ProcessFile(Path, depth):
	NewFile = ""
	# Copy the file one line at a time. 
	# Substitute (manageable) imports with the linked file, recursively.
	# Let's also indent imports.
	with open(Path) as File:
		def indent(x):
			return "  " * x
		for Line in File:
			# if this Line is an import, and is a relative path, process that path.
			if((Line.find("@import") >= 0) and (Line.find("://") == -1)):
				RelLink = TrimImportPath(Line)
				NewFile += ("\n"+ indent(depth) + "/*# Importing file " + RelLink + " #*/\n")
				linkedFile = JoinPath(Path,RelLink)
				NewFile += ProcessFile(linkedFile, depth+1)
			else:
				NewFile += indent(depth) + Line
		NewFile += ("\n" + indent(depth-1) + "/*# End of file " + os.path.basename(Path) + " #*/") 
	return NewFile + "\n"

def Main():
	ReadMe()
	PathIn = input("Enter path to the root file of CSS. \n(Blank defaults to "+DefaultInput+") \n>>>")
	if(PathIn == ""): 
		PathIn = os.path.join(os.path.dirname(__file__),DefaultInput)
	PathOut = input("Enter output filename. \n(Blank defaults to "+DefaultOutput+") \n>>>")
	print("\n")
	if(PathOut == ""):
		PathOut = os.path.join(os.path.dirname(__file__),DefaultOutput)
	NewFile = "/*# Compiled by OneFile.py. \n  # This CSS was originally composed of several files broken into imports.\n  # Here it is compiled into one file instead. #*/ \n"
	NewFile += ProcessFile(PathIn, 0)
	print(NewFile)
	with open(PathOut, 'w') as SaveFile: SaveFile.write(NewFile)
	print("/*# Processing finished. #*/")

Main()

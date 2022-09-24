import pypandoc
import easygui

print('please select an html file to convert to docx...')

inputfile = easygui.fileopenbox()
outputfile = easygui.filesavebox()

output = pypandoc.convert_file(inputfile, format='html', to='docx', outputfile=outputfile+'.docx', extra_args=['-RTS'])



print('your file has been saved as ' + outputfile)

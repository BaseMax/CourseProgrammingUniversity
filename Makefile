main:
	xelatex ./book.tex -no-aux -synctex=1 -interaction=nonstopmode --shell-escape %,tex
	rm ./book.aux
	rm ./book.out
	rm ./book.log
# Compilador diapostivas
pandoc -V lang=es --to=beamer --pdf-engine=lualatex  --standalone formato.yaml --output=Diapositivas/diapositivas.tex Diapositivas/diapositivas.md
pandoc -V lang=es --to=beamer --pdf-engine=lualatex formato.yaml --output=Diapositivas/diapositivas.pdf Diapositivas/diapositivas.md
# compilar documentacion
pandoc -V lang=es --pdf-engine=lualatex --output=Documentacion/documentacion.pdf README.md
pandoc -V lang=es --standalone --pdf-engine=lualatex --output=Documentacion/documentacion.tex README.md

# mv out.* ../Entregable/

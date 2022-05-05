## Problema de compilación de cualquier PDF

- Se tiene que ejecutar en linux

aparece algo así

```lua
❯ nvim compilador.sh
❯ ./compilador.sh
pdflatex not found. Please select a different --pdf-engine or install pdflatex -- see also /usr/share/doc/pandoc/README.Debian
pandoc: diapositivas.md: openBinaryFile: does not exist (No such file or directory)
```

Lo solucionamos de la siguiente manera, ejecutando el siguiente comando

```lua
❯ sudo apt-get install texlive-latex-base
```

y obtenemos la siguiente salida:

```lua
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:

  ... (many prompts)
  
Setting up liblwp-protocol-https-perl (6.10-1) ...
Setting up libwww-perl (6.52-1) ...
Setting up libxml-parser-perl:amd64 (2.46-2) ...
Setting up libxml-twig-perl (1:3.52-1) ...
Setting up libnet-dbus-perl (1.2.0-1+b1) ...
Processing triggers for mailcap (3.69) ...
Processing triggers for libc-bin (2.31-13+deb11u2) ...
Processing triggers for tex-common (6.16) ...
Running updmap-sys. This may take some time... done.
Running mktexlsr /var/lib/texmf ... done.
Building format(s) --all.
        This may take some time... done.
Processing triggers for libgdk-pixbuf-2.0-0:amd64 (2.42.2+dfsg-1) ...
```

También se recomienda instalar las fuentes extra, porque puede ocurrir un error como este

```lua
! Font OT1/ptm/m/n/10=ptmr7t at 10.0pt not loadable: Metric (TFM) file not found.
```

y para instalarla vamos a ejecutar el siguiente comando que ocupará alrededor de 500Mb

```lua
sudo apt-get install texlive-fonts-recommended
sudo apt-get install texlive-fonts-extra
```

Por último instala  los paquetes extra

```lua
sudo apt-get install texlive-latex-extra
```

Entonces ya podrás compilar un archivo `pdflatex` como en el siguiente ejemplo

```lua
pdflatex latex_source_name.tex
```

Ahora que viste todo lo anterior, puedes ejecutarlo todo con un simple paso con el siguiente comando.

```lua
sudo apt-get install texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra
```



## Instalación de open CV python

### Ruta incorrecta de instalación

Teniendo instalando Python

```lua
C:\Users\vaito>python --version
Python 3.11.0a6
```

Instalamos openCV mediante PIP mediante CMD

```lua
pip install opencv-python
```

Pero al tratar de instalarlo obtenemos un error.

```lua

C:\Users\vaito>
Collecting opencv-python
  Downloading opencv_python-4.5.5.64-cp36-abi3-win_amd64.whl (35.4 MB)
     |████████████████████████████████| 35.4 MB 2.2 MB/s
Collecting numpy>=1.19.3
  Downloading numpy-1.22.3.zip (11.5 MB)
     |████████████████████████████████| 11.5 MB 2.2 MB/s
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
    Preparing wheel metadata ... done
Building wheels for collected packages: numpy
  Building wheel for numpy (PEP 517) ... error
  ERROR: Command errored out with exit status 1:
   command: 'C:\Python311\python.exe' 'C:\Python311\Lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py' build_wheel 'C:\Users\vaito\AppData\Local\Temp\tmpmsgktqmg'
       cwd: C:\Users\vaito\AppData\Local\Temp\pip-install-kviswp2m\numpy_14e439ed3d964d61b0e5ac5f1ef0718e
  Complete output (204 lines):
  setup.py:66: RuntimeWarning: NumPy 1.22.3 may not yet support Python 3.11.
    warnings.warn(
  Running from numpy source directory.
  C:\Users\vaito\AppData\Local\Temp\pip-install-kviswp2m\numpy_14e439ed3d964d61b0e5ac5f1ef0718e\tools\cythonize.py:63: DeprecationWarning: The distutils package is 
   ...many prompts
    
  INFO: building library "npymath" sources
  error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
  ----------------------------------------
  ERROR: Failed building wheel for numpy
Failed to build numpy
ERROR: Could not build wheels for numpy which use PEP 517 and cannot be installed directly
WARNING: You are using pip version 21.2.4; however, version 22.0.4 is available.
You should consider upgrading via the 'C:\Python311\python.exe -m pip install --upgrade pip' command.

```

Instalar la actualización mediante CMD en modo administrador

```lua
pip install --upgrade pip --user
```

También tiene que instalar las Microsoft Visual C++ 14.0 or greater is required. Ello lo puede revisar el siguiente post

[stackoverflow](https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst)

Esta ruta incorrecta de instalación no me llevo a la solución

### Ruta correcta de instalación

La instalación es para Windows.

1. instalar las Microsoft Visual C++ 14.0

   [stackoverflow](https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst)

2. instalar Python 3.10

A fecha de 04/02/2022 no funciona bien numpy y por tanto openCV Python 3.11 o superior, por ello mejor 3.10.

[Link de python 3.10](https://www.python.org/downloads/release/python-3100/)

3. Instalar pip

Me gusta la explicación de un sitio web que te dice como debes instalarlo, y por ello es la que seguiremos del siguiente sitio:

[Link](https://phoenixnap.com/kb/install-pip-windows)

4. Instar Open-CV

Vamos a instalarlo de manera no oficial, esta es la manera no oficial, ya que no esta proporcionada  por open-CV, pero funciona bien.

Para instalarlo vamos a ejecutar el siguiente comando

```
pip install opencv-python
```

[Ver documentacion de este comando]([opencv-python · PyPI](https://pypi.org/project/opencv-python/))

y se instalará y mostrará el resultado deseado como se muestra a continuación:

```
C:\Users\vaito>pip install opencv-python
Collecting opencv-python
  Using cached opencv_python-4.5.5.64-cp36-abi3-win_amd64.whl (35.4 MB)
Collecting numpy>=1.14.5
  Downloading numpy-1.22.3-cp310-cp310-win_amd64.whl (14.7 MB)
     ---------------------------------------- 14.7/14.7 MB 2.3 MB/s eta 0:00:00
Installing collected packages: numpy, opencv-python
Successfully installed numpy-1.22.3 opencv-python-4.5.5.64
```

## Problema del lenguaje en español

Para lograrlo tenemos que poner lo siguiente

```

```

# Las imagenes no estan en el mismo lugar que el markdown

```
pandoc -f markdown-implicit_figures 
```


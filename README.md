```yaml
Campus: Ciudad Universitaria
Facultad: Ingeniería
Materia : Inteligencia Artificial
Semestre: 2022-2
Equipo: 1
Clave: 0406
Participantes: 
	- Barrera Peña Víctor Miguel
	- Espino De Horta Joaquín Gustavo
	
Profesor: Dr. Ismael Everardo Barcenas Patiño
Título : Proyecto 4
Subtítulo : Clasificador de imagenes
Fecha entrega: 26/05/2022

```

# Capítulo 0 Estructura del  repositorio

# Definición del problema

## Clasificación Bayesiana

#  

# Solución

## Pseudocódigo

## Explicación

# Experimentos

## Baja dificultad

### Problema 1

### Problema 2

### Problema 3

## Media dificultad

### Problema 1

### Problema 2

### Problema 3

## Alta dificultad

### Problema 1

### Problema 2

### Problema 3

## Sin solución

# Capítulo 1  Introducción 



# Capítulo 2 Desarrollo

## Idea de desarrollo del programa

## Casos de prueba

### Triviales (1 caso)

### Fáciles (3 casos)

### Media (3 casos)

### Difíciles ( 3 casos )

### Sin solución (1 caso)

### Código

## Explicación código

# Capítulo 3 Conclusión

## Barrera Peña Víctor Miguel

## Espino de Horta Joaquín Gustavo



# Anexo (teoría)

## Instalación de open CV python

Teniendo instalando Python

```
C:\Users\vaito>python --version
Python 3.11.0a6
```

Instalamos openCV mediante PIP mediante CMD

```
pip install opencv-python
```

Pero al tratar de instalarlo obtenemos un error.

```

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
  C:\Users\vaito\AppData\Local\Temp\pip-install-kviswp2m\numpy_14e439ed3d964d61b0e5ac5f1ef0718e\tools\cythonize.py:63: DeprecationWarning: The distutils package is deprecated and slated for removal in Python 3.12. Use setuptools or check PEP 632 for potential alternatives
    from distutils.version import LooseVersion
  Processing numpy/random\_bounded_integers.pxd.in
  Processing numpy/random\bit_generator.pyx
  Processing numpy/random\mtrand.pyx
  Processing numpy/random\_bounded_integers.pyx.in
  Processing numpy/random\_common.pyx
  Processing numpy/random\_generator.pyx
  Processing numpy/random\_mt19937.pyx
  Processing numpy/random\_pcg64.pyx
  Processing numpy/random\_philox.pyx
  Processing numpy/random\_sfc64.pyx
  Cythonizing sources
  INFO: blas_opt_info:
  INFO: blas_armpl_info:
  INFO: No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
  INFO: customize MSVCCompiler
  INFO:   libraries armpl_lp64_mp not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: blas_mkl_info:
  INFO:   libraries mkl_rt not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: blis_info:
  INFO:   libraries blis not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: openblas_info:
  INFO:   libraries openblas not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO: get_default_fcompiler: matching types: '['gnu', 'intelv', 'absoft', 'compaqv', 'intelev', 'gnu95', 'g95', 'intelvem', 'intelem', 'flang']'
  INFO: customize GnuFCompiler
  WARN: Could not locate executable g77
  WARN: Could not locate executable f77
  INFO: customize IntelVisualFCompiler
  WARN: Could not locate executable ifort
  WARN: Could not locate executable ifl
  INFO: customize AbsoftFCompiler
  WARN: Could not locate executable f90
  INFO: customize CompaqVisualFCompiler
  WARN: Could not locate executable DF
  INFO: customize IntelItaniumVisualFCompiler
  WARN: Could not locate executable efl
  INFO: customize Gnu95FCompiler
  WARN: Could not locate executable gfortran
  WARN: Could not locate executable f95
  INFO: customize G95FCompiler
  WARN: Could not locate executable g95
  INFO: customize IntelEM64VisualFCompiler
  INFO: customize IntelEM64TFCompiler
  WARN: Could not locate executable efort
  WARN: Could not locate executable efc
  INFO: customize PGroupFlangCompiler
  WARN: Could not locate executable flang
  WARN: don't know how to compile Fortran code on platform 'nt'
  INFO:   NOT AVAILABLE
  INFO:
  INFO: accelerate_info:
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_3_10_blas_threads_info:
  INFO: Setting PTATLAS=ATLAS
  INFO:   libraries tatlas not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_3_10_blas_info:
  INFO:   libraries satlas not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_blas_threads_info:
  INFO: Setting PTATLAS=ATLAS
  INFO:   libraries ptf77blas,ptcblas,atlas not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_blas_info:
  INFO:   libraries f77blas,cblas,atlas not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO:   NOT AVAILABLE
  INFO:
  C:\Users\vaito\AppData\Local\Temp\pip-install-kviswp2m\numpy_14e439ed3d964d61b0e5ac5f1ef0718e\numpy\distutils\system_info.py:2077: UserWarning:
      Optimized (vendor) Blas libraries are not found.
      Falls back to netlib Blas library which has worse performance.
      A better performance should be easily gained by switching
      Blas library.
    if self._calc_info(blas):
  INFO: blas_info:
  INFO:   libraries blas not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO:   NOT AVAILABLE
  INFO:
  C:\Users\vaito\AppData\Local\Temp\pip-install-kviswp2m\numpy_14e439ed3d964d61b0e5ac5f1ef0718e\numpy\distutils\system_info.py:2077: UserWarning:
      Blas (http://www.netlib.org/blas/) libraries not found.
      Directories to search for the libraries can be specified in the
      numpy/distutils/site.cfg file (section [blas]) or by setting
      the BLAS environment variable.
    if self._calc_info(blas):
  INFO: blas_src_info:
  INFO:   NOT AVAILABLE
  INFO:
  C:\Users\vaito\AppData\Local\Temp\pip-install-kviswp2m\numpy_14e439ed3d964d61b0e5ac5f1ef0718e\numpy\distutils\system_info.py:2077: UserWarning:
      Blas (http://www.netlib.org/blas/) sources not found.
      Directories to search for the sources can be specified in the
      numpy/distutils/site.cfg file (section [blas_src]) or by setting
      the BLAS_SRC environment variable.
    if self._calc_info(blas):
  INFO:   NOT AVAILABLE
  INFO:
  non-existing path in 'numpy\\distutils': 'site.cfg'
  INFO: lapack_opt_info:
  INFO: lapack_armpl_info:
  INFO:   libraries armpl_lp64_mp not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: lapack_mkl_info:
  INFO:   libraries mkl_rt not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: openblas_lapack_info:
  INFO:   libraries openblas not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: openblas_clapack_info:
  INFO:   libraries openblas,lapack not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: flame_info:
  INFO:   libraries flame not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_3_10_threads_info:
  INFO: Setting PTATLAS=ATLAS
  INFO:   libraries tatlas,tatlas not found in C:\Python311\lib
  INFO:   libraries tatlas,tatlas not found in C:\
  INFO:   libraries tatlas,tatlas not found in C:\Python311\libs
  INFO: <class 'numpy.distutils.system_info.atlas_3_10_threads_info'>
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_3_10_info:
  INFO:   libraries satlas,satlas not found in C:\Python311\lib
  INFO:   libraries satlas,satlas not found in C:\
  INFO:   libraries satlas,satlas not found in C:\Python311\libs
  INFO: <class 'numpy.distutils.system_info.atlas_3_10_info'>
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_threads_info:
  INFO: Setting PTATLAS=ATLAS
  INFO:   libraries ptf77blas,ptcblas,atlas not found in C:\Python311\lib
  INFO:   libraries ptf77blas,ptcblas,atlas not found in C:\
  INFO:   libraries ptf77blas,ptcblas,atlas not found in C:\Python311\libs
  INFO: <class 'numpy.distutils.system_info.atlas_threads_info'>
  INFO:   NOT AVAILABLE
  INFO:
  INFO: atlas_info:
  INFO:   libraries f77blas,cblas,atlas not found in C:\Python311\lib
  INFO:   libraries f77blas,cblas,atlas not found in C:\
  INFO:   libraries f77blas,cblas,atlas not found in C:\Python311\libs
  INFO: <class 'numpy.distutils.system_info.atlas_info'>
  INFO:   NOT AVAILABLE
  INFO:
  INFO: lapack_info:
  INFO:   libraries lapack not found in ['C:\\Python311\\lib', 'C:\\', 'C:\\Python311\\libs']
  INFO:   NOT AVAILABLE
  INFO:
  C:\Users\vaito\AppData\Local\Temp\pip-install-kviswp2m\numpy_14e439ed3d964d61b0e5ac5f1ef0718e\numpy\distutils\system_info.py:1902: UserWarning:
      Lapack (http://www.netlib.org/lapack/) libraries not found.
      Directories to search for the libraries can be specified in the
      numpy/distutils/site.cfg file (section [lapack]) or by setting
      the LAPACK environment variable.
    return getattr(self, '_calc_info_{}'.format(name))()
  INFO: lapack_src_info:
  INFO:   NOT AVAILABLE
  INFO:
  C:\Users\vaito\AppData\Local\Temp\pip-install-kviswp2m\numpy_14e439ed3d964d61b0e5ac5f1ef0718e\numpy\distutils\system_info.py:1902: UserWarning:
      Lapack (http://www.netlib.org/lapack/) sources not found.
      Directories to search for the sources can be specified in the
      numpy/distutils/site.cfg file (section [lapack_src]) or by setting
      the LAPACK_SRC environment variable.
    return getattr(self, '_calc_info_{}'.format(name))()
  INFO:   NOT AVAILABLE
  INFO:
  INFO: numpy_linalg_lapack_lite:
  INFO:   FOUND:
  INFO:     language = c
  INFO:     define_macros = [('HAVE_BLAS_ILP64', None), ('BLAS_SYMBOL_SUFFIX', '64_')]
  INFO:
  Warning: attempted relative import with no known parent package
  C:\Python311\Lib\distutils\dist.py:274: UserWarning: Unknown distribution option: 'define_macros'
    warnings.warn(msg)
  running bdist_wheel
  running build
  running config_cc
  INFO: unifing config_cc, config, build_clib, build_ext, build commands --compiler options
  running config_fc
  INFO: unifing config_fc, config, build_clib, build_ext, build commands --fcompiler options
  running build_src
  INFO: build_src
  INFO: building py_modules sources
  creating build
  creating build\src.win-amd64-3.11
  creating build\src.win-amd64-3.11\numpy
  creating build\src.win-amd64-3.11\numpy\distutils
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

```
pip install --upgrade pip --user
```

También tiene que instalar las Microsoft Visual C++ 14.0 or greater is required. Ello lo puede revisar el siguiente post

[stackoverflow](https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst)

Esta ruta incorrecta de instalación no me llevo a la solución

### Ruta correcta para la instalación de Open CV Python

La instalación es para Windows.

1. instalar las Microsoft Visual C++ 14.0

   [stackoverflow](https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst)

2. instalar python 3.10

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

# Referencias


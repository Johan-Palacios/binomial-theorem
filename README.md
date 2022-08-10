# binomial-theorem.py

## Teorema del Binomio
Este teorema expresa la enésima potencia de un binomio como un polinomio. El desarrollo del binomio posee singular importancia ya que aparece con mucha frecuencia en Matemáticas y posee diversas aplicaciones en otras áreas del conocimiento.

Este programa realizado en [Python](https://www.python.org/ "Python"), permite el cálculo de este teorema, con una gran facilidad y rápidez, esto gracias a la libreria de [Sympy](https://www.sympy.org/ "Sympy") para cálculos algébraicos avanzados.


### Preparación de entorno
- Python3
- PyTest
- Terminal (MS Powershell o Bash)

#### Creación de entorno virtual (VENV)

Crear el enorno virtual de python

`python3 -m venv teorema`

Activación del Entorno Virtual

**LINUX**

`source teorema/bin/activate`

**WINDOWS**
`teorema\Scripts\activate.bat`

    // Directorio de trabajo
    take src
    // Clonar el repositorio en src
    git clone https://github.com/Johan-Palacios/binomial-theorem
	
#### Instalación de dependencias

`python3 -m pip install -r requirements.txt`

Después de estos pasos, la instalación estaría completada, solo hay que ejecutar lo siquiente
#### Ejecutar tests
`pytest core/test_theorem.py`

![image](https://user-images.githubusercontent.com/77251405/183819103-40897d31-eb0d-4d71-b5ee-32d008bf8051.png)

#### Ejecutar Binomial-theorem.py

`python3 __main__.py`

![image](https://user-images.githubusercontent.com/77251405/183819300-afa97357-4356-4ae8-8e1a-af1eb8f78e29.png)

# binomial-theorem.py 🧮

## Teorema del Binomio 🗒️
Este teorema expresa la enésima potencia de un binomio como un polinomio. El desarrollo del binomio posee singular importancia ya que aparece con mucha frecuencia en Matemáticas y posee diversas aplicaciones en otras áreas del conocimiento.

Este programa realizado en [Python](https://www.python.org/ "Python"), permite el cálculo de este teorema, con una gran facilidad y rápidez, esto gracias a la libreria de [Sympy](https://www.sympy.org/ "Sympy") para cálculos algébraicos avanzados.

## Preview ✨

![image](https://user-images.githubusercontent.com/77251405/197453881-3695f9c2-05a1-4631-935a-92cc07a4419f.png)

### Preparación de entorno 🚀

- Python3
- PyTest
- Terminal (MS Powershell o Bash)

#### Clonar el repostorio

```bash
git clone https://github.com/Johan-Palacios/binomial-theorem.git
```

#### Creación de entorno virtual (VENV)

Crear el enorno virtual de python

```bash
python3 -m venv vev
```

Activación del Entorno Virtual

**LINUX**
```bash
source ./venv/bin/activate
```

**WINDOWS**

```bash
venv\Scripts\activate.bat
```


#### Instalación de dependencias

```bash
python3 -m pip install -r requirements.txt
```

#### Ejecutar tests 🔧

```bash
pytest core/test_theorem.py
```

![image](https://user-images.githubusercontent.com/77251405/183819103-40897d31-eb0d-4d71-b5ee-32d008bf8051.png)

#### Ejecutar Binomial-theorem.py

```bash
python3 __main__.py
```
Y listo ✅

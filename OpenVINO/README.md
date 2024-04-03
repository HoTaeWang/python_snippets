# OpenVINO

oneDNN developers guide (https://oneapi-src.github.io/oneDNN/index.html)

oneDNN on git-hub (https://github.com/oneapi-src/oneDNN)

oneDNN open spec (https://spec.oneapi.com/versions/latest/elements/oneDNN/source/index.html)


### Installation on the Windows
1) Install Python

2) Install Git

3) Install C++ REdistributable ( For Python > 3.8 )

4) Install the notebooks

5) Create a Virtual Environment

```
   python -m venv openvino_env
```

   When you use the Anaconda, you need to refer another markdown file, conda Guide


6) Activate the Environment

```
   openvino_env\Scripts\activate
```

7) Clone the Repository

```
   ### Note: Using the --depth=1 option for git clone reduces download size


   git clone --depth=1 https://github.com/openvinotoolkit/openvino_notebooks.git

   cd openvino_notebooks
```

8) Install the Packages

* This step installs OpenVINO and dependencies like Jupyter Lab. First, upgrade pip to the latest version.
  Then, install the required dependencies

```
  python -m pip install --upgrade pip wheel setuptools
  pip install -r requirements.txt
```

9) Launch the Jupyter Labs

* To launch all notebooks in Jupyter Lab (localhost only)

```
   jupyter lab notebooks
```

* To launch all notebooks available form any host

```
   jupyter lab notebooks --ip 0.0.0.0
```


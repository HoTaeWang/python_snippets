# Conda Guide for Anaconda

In Windows, these steps should be excuted inside an Anaconda Prompt

1) Clone the Repository

```
	git clone https://github.com/openvinotoolkit/openvino_notebooks.git
```

2) Create a Conda Environment with Python 3.10

```
	cd openvino_notebooks
	conda create -n openvino_env python=3.10
```

3) Activate the Environment

```
	conda activate openvino_env
```

4) Install the Packages

* Install OpenVINO, Jupyter and other required packages to run the notebooks

```
	# Upgrade pip to the latest version to ensure compatibility with all dependencies
	python -m pip install --upgrade pip==21.3
	pip install -r requirements.txt
```

5) (conda) Add the OpenVINO library to your PATH

* Checking path of the OpenVINO library

```
	python -c "import os,sys;print(os.path.dirname(sys.executable))"
```

6) (conda) Launch the Notebook

```
	# To launch a single notebook
	jupyter notebook <notebook_filename>

	# To launch all notebooks in Jupyter Lab
	jupyter lab notebooks
```


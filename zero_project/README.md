# Zero Project





## 5 Phases 

1. Inception
   Ready the tools. 
   Organize the project directory and virtual environment.
2. Elaboration, Part 1
   Define done.
   This is implemented as acceptance test cases.
3. Elaboration, Part 2
   Define components and some tests.
   This is implemented as unit test cases for components that need to be built
4. Construction
   Build the software
5. Transition. Final Cleanup
   make sure all tests pass and the documentation is readable.



## Inception Phase

1. Start the inception phase by creating the parent directory for the project
2. Then some commonly-used sub-directories (docs, notebooks, src, tests)
3. Check the *List of deliverable*s  (like README.md, pyproject.toml, and tox.ini)



#### Build a fresh, new virtual environment for the project.

```
`% conda create -n project_name --channel=conda-forge python=3.10`
```

#### Conda forge Documentation Tool

> `python -m pip install sphinx`

​	1) Sphinx installation

​		`$ conda install Sphinx    # Using Anaconda`

​		`$ pip3 install Sphinx     # Other cases`		

​     2) Sphinx Setting   (on the Root directory)

​		`$ mkdi`r docs
​        $ cd docs
​        $ sphinx-quickstart`

​      3) Sphinx Build

​     	`$ make html`



## Elaboration, part 1: define done

It helps to have a clear definition of "done".


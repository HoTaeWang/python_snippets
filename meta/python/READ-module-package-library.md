# Modules, libraries and packages
Modules and packages can easily be confused because of their similarities, but there are a few differences. Modules are similar to files, while packages are like directories that contain different files. Modules are generally written in a single file, but that's more of a practice than a definition. 

## Package
Packages are essentially a type of module. Any module that contains the  __path__ definition is a package. Packages, when viewed as a directory, can contain sub-packages and other modules. Modules, on the other hand, can contain classes, functions and data members just like any other Python file. 

## Library
Library is a term that's used interchangeably with imported packages. But in general practice, it refers to a collection of packages.

Despite the differences between modules, packages and libraries, you can import any of them using import statements.  

## PIP
Third-party package add-ons of Python can be found in the Python Package Index. To install packages that aren't a part of the standard library programmers use ‘pip’ (package installer for Python). It is installed with Python by default. To use pip, you need to be familiar with either the terminal if you're using a Mac or the command line interface if you're using Windows. 

Alternatively, you can also use the terminal window present inside your IDE. When you are using the command line or terminal, you must make sure that you are installing packages in the same Python interpreter that you are working with inside your IDE. 

Note: Package names as well as the command line or terminal are case-sensitive.

Once you have installed the package, you will be able to use the package directly inside your Python code. This is a one-time installation and the package will be present as a part of your Python interpreter until you choose to uninstall it.

The packages that you can install often have a number of classes, functions, sub-packages and members. These can be understood by using the package and finding examples that other programmers have posted on different websites. This will give you a better understanding of what functionality within that package needs more attention than others. 

## Python Package Index: pypi
Additionally, it is also a good practice to look up the documentation of the packages. In some cases, you can use the Python Package Index pypi website. In other cases, the packages are built and maintained by open-source communities and you can find their information on a standalone website created for it or on a version control system such as GitHub. Documentation in most of the popular Python libraries today is pretty elaborate and should have good examples to get you started.

## Sub-packages
If we are to assume that packages are similar to a folder or directory in our operating system, then the package can also contain other directories. Packages, both built-in and user-defined, can contain other folders within them that need to be accessed. These are named sub-packages. You use dot-notation to access sub-packages within a package you have imported. For example, in a package such as matplotlib, the contents that are used most commonly are present inside the subpackage pyplot. Pyplot eventually may consist of various functions and attributes.

The code for importing a sub-package is:

```
    import matplotlib.pyplot
```
To make it even more convenient, it is often imported using an alias. So more commonly, you will come across code such as:

'''
    import matplotlib.pyplot as plt
'''

You could use any other word as an alias instead of plt, but it is a common convention.
# Overview of the Projects
* The stages are inspired by the Extract-Transform-Load(ETL) architectural pattern.

## Overall architectural approach to creating a complete sequence of data analysis programs.
* Data acquisition
* Inspection of data
* Cleaning data; this includes validating, converting, standardizing, and saving intermediate results
* Summarizing, and modeling data
* Creating more sophisticated statistical models

## General data acquisition
* The failures of this phase in this effort often lead to complicated rework later. It's essential to recognize that data exists in these two essential forms:
	1) Python objects, usable in analytic programs
		Pillow to operate on images
		librosa can create objects representing audio data
	2) A serialization of a Python object.
		Text. Some kind of String (CSV, JSON, TOML, YAML, HTML, XML etc)
		Pickled Python Objects (Created by the pickle module)
		Binary formats.
* Some acquisition
	After acquiring new data, it's prudent to do a manual inspection. This is often done a few times at the start of application development. After that, inspection is only done to diagnose problems with the source data.

## Inspection
Data inspection needs to be done when starting development.



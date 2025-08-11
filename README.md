# strandings_from_space
Very high-resolution (VHR) satellite image pre-processing and annotation pipeline for stranded whale and dolphin (adaptable to any feature of interest), and a semi-automated multi-observer annotation comparison workflow.

strandings_from_space custon built user interface:
<p align="center">
  <img width="547" height="316" alt="stranding_from_space_annotation_pipeline" src="https://github.com/user-attachments/assets/015c1ca2-fbe5-4456-84d3-1ef660ca414b" />
</p>

Example semi-automated clustering output, useful to identify and compare features annotated by more than one observer (green square = 3 observers, yellow circle = 2 observers, blue triangle = 1 observer, this workflow is adaptable to any number of observer annotations and functionable for geolocated satellite data (latitude, longitude) and unknown reference aerial data (row, col)). Aerial image © Department of Conservation, New Zealand.
<img width="1548" height="895" alt="stewart_island_aerial_clustered" src="https://github.com/user-attachments/assets/da93e15b-e46f-465e-8cdf-517e8729f427" />

## Table of Contents
- [Purpose](#purpose)
- [Methodology](#methodology)
- [Repository structure](#repository-structure)
  - [‘compare_counts’](#‘compare_counts’)
  - [‘inputs’](#‘inputs’)
  - [‘outputs’](#‘outputs’)
  - [‘qgis’](#‘qgis’)
  - [‘temp_outputs’](#‘temp_outputs’)
  - [‘cetacean_strandings_from_space_comparing_counts.ipynb’](#‘cetacean_strandings_from_space_comparing_counts.ipynb’)
  - [‘compare_counts.yml’](#‘compare_counts.yml’)
  - [‘otb.yml’](#‘otb.yml’)
  - [‘otb_pansharpening.ipynb’](#‘otb_pansharpening.ipynb’)
  - [‘S4_attribute_training_document.pdf’](#‘S4_attribute_training_document.pdf’)
  - [‘strandings_from_space_pipeline.ipynb’](#‘strandings_from_space_pipeline.ipynb’)
  - [‘videos’](#‘videos’)
- [Getting started and requirements](#getting-started-and-requirements)
- [Licence](#licence)
- [Funding](#funding)
- [Citation](#citation)
- [Data](#Data)

## 1.	Purpose

## 2.	Methodology

## 3.	Repository structure 
### 3.1.	‘compare_counts’
3.1.1.	 'inputs' <br>
3.1.1.1  'aerial_ref' <br> 
3.1.1.2  'ground_ref' <br> 
3.1.1.3  'satellite' <br> 

3.1.2.	 'ouputs' <br>

3.1.2.	 'temp_ouputs' <br>

### 3.2.	‘inputs’

### 3.3.	‘outputs’

### 3.4.	‘qgis’

### 3.5.	‘temp_outputs’

### 3.6.	‘cetacean_strandings_from_space_comparing_counts.ipynb’

### 3.7.	‘compare_counts.yml’

### 3.8.	‘otb.yml’

### 3.9.	‘otb_pansharpening.ipynb’

### 3.10.	‘S4_attribute_training_document.pdf’

### 3.11.	‘strandings_from_space_pipeline.ipynb’

A visual representation of the steps within the code is available as pseudo code below: <br>

<img width="2223" height="3014" alt="Process_flow" src="https://github.com/user-attachments/assets/779e098b-2d86-40b7-87bb-6d992a2e81c6" /> <br>

### 3.12.	‘videos’

## 4.	Getting started and requirements <br>
4.1.	Clone the repository to your local drive by either: <br>
4.1.1.	 Visit https://github.com/PennyJClarke/strandings_from_space.git, select the dropdown arrow to the right of the green ‘Code’ button and selecting ‘Download ZIP’, extract to your desktop (the code automatically identifies and expects the repository to be located on the desktop) <br>

4.1.2.	Or, in your windows powershell, anaconda prompt window or equivalent, navigate to your desktop to clone the repository using (amend link to users Desktop): <br>
<pre>
<code id="code-block">cd C:\\Users\\Desktop</code> <button onclick="copyCode()"></button>
</pre>
followed by: <br>
<pre>
<code id="code-block">git clone https://github.com/PennyJClarke/strandings_from_space.git</code> <button onclick="copyCode()"></button>
</pre>

For examples of the code use, please view the associated publication at: (include link to published manuscript). All the data associated with this publication is available on the British Antarctic Survey Polar Data Centre: (provide link). <br>

## 5.	Licence <br>
MIT License <br>

Copyright (c) 2025 PennyJClarke <br>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: <br>

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. <br>

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## 6.	Funding <br>
Funding was provided the Natural Environmental Research Council (Project ID: NE/T00939X/1).

## 7. Citation <br>
To use this code or associated dataset, please cite:<br>

**Associated manuscipt:**<br>
Clarke et al. (2025 ) Odontocete strandings from space: Accurately counting individuals with very-high resolution optical and SAR satellite imagery. Remote Sensing of Environment.

**Dataset:**<br>
Clarke, P. J., Cubaynes, H. C., Bowler, E., Jackson, J. A., Attard, M. R. G., Stockin, K. A. & Carlyon, K. (2025). Odontocete strandings from space: point annotation dataset of stranded whale and dolphin species identified in very-high resolution optical and SAR satellite imagery along offshore islands of New Zealand and Tasmania between 2018-2023 (Version 1.0) [Data set]. NERC EDS UK Polar Data Centre.

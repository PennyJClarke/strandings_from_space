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
This study is a first step to sharing knowledge using openly accessible workflows to pre-process and annotate satellite imagery, to allow local stranding networks, governments and NGOs to implement strandings monitoring along their own coastlines. It is evident through this research that people living local to these coastlines are best placed to conduct research using satellites along their own coastline, to evaluate and implement what is important to them, for they have the insights to coordinate tasking with satellite image providers rapidly and are aware of realities on the ground. Here we share open-source process flows for image pre-processing and analysis using QGIS and Python, to work towards a globally scalable solution for analysing satellite imagery. This tool is designed for ecologists and conservation managers. 

Cetacean strandings offer significant conservation value for the assessment of ecosystems and serve as early warning of emerging concerns regarding animal, ocean, and human health. However stranding monitoring programmes are scarce or non-existent along minimally populated areas, coastlines with limited economic resources, geographically remote areas, complex coastlines and areas of geopolitical unrest. Very high-resolution (VHR) satellite imagery offers the prospect of improving monitoring in these regions. 

An important consideration for the scalability of VHR optical satellite imagery to monitor large expanses of remote and low to mid economically resourced coastlines, is increasing accessibility. This includes access to imagery, knowledge, sharing expertise, infrastructure and open access tools and protocols. The development of best practice open-source standardised workflows and training is recognised and recommended by the International Whaling Commission as important for the future utility of VHR satellite imagery to study cetaceans 

To facilitate reproducible analysis and annotation, a robust standardised open-source protocol for pre-processing and analysing VHR satellite imagery for stranded cetaceans was developed and used in QGIS 3.28. The standardised protocol was adapted from Cubaynes et al. (2023) and refined based on feedback from remote sensing and cetacean experts. A template for recording annotation metadata (e.g., confidence scores, satellite metadata, feature information, and environmental conditions) and an accompanying training document was co-developed, and reviewed by stranding experts and the international ‘Satellites to Study Whales’ community. This approach ensures that future stranding datasets can be collected and formatted under consistent data standards. The importance of open-source software was emphasised, to improve access and uptake in under-resourced regions. Therefore, as well as a user-interface centred pipeline in QGIS, a replicable version of the workflow was developed using Python 3.10, presented here. The strandings_from_space Python pipeline specifically offers a powerful future-facing tool given its ability to allow customisable script, which can be adapted to different user’s needs. The workflows are also applicable beyond the strandings and wildlife from space community, as it forms a framework supporting remote sensing applications, which require image annotation.

Pansharpening takes the panchromatic and multispectral images, and where the two rasters fully overlap, fuses them together to produce a multispectral image with the higher spatial resolution of the panchromatic image. Imagery can be acquired from satellite image providers at differing levels of pre-processing, depending on the data acquired it may be necessary to reproject the data, to achieve a more accurate flat two-dimensional representation of the Earth.

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
This research has been supported by the Natural Environment Research Council (NERC) through a SENSE CDT studentship (grant no. NE/T00939X/1). The research was further supported by additional funding provided through, the British Antarctic Survey (BAS) Innovation Voucher, Sentinel Hub and their #30MapChallenge competition, BAS Ecosystems, and the support and cooperation of Airbus and Maxar Technologies Ltd, for their rapid response and efforts to enable successful collection of the imagery analysed here.

## 7. Citation <br>
To use this code or associated dataset, please cite:<br>

**Associated manuscipt:**<br>
Clarke et al. (2025 ) Odontocete strandings from space: Accurately counting individuals with very-high resolution optical and SAR satellite imagery. Remote Sensing of Environment.

**Dataset:**<br>
Clarke, P. J., Cubaynes, H. C., Bowler, E., Jackson, J. A., Attard, M. R. G., Stockin, K. A. & Carlyon, K. (2025). Odontocete strandings from space: point annotation dataset of stranded whale and dolphin species identified in very-high resolution optical and SAR satellite imagery along offshore islands of New Zealand and Tasmania between 2018-2023 (Version 1.0) [Data set]. NERC EDS UK Polar Data Centre.

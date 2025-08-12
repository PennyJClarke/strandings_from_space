# strandings_from_space
Very high-resolution (VHR) satellite image pre-processing and annotation pipeline for stranded whale and dolphin (adaptable to any feature of interest), and a semi-automated multi-observer annotation comparison workflow for evaluating count congruence, for geolocated satellite imagery (latitude, longitude) and unknown reference aerial imagery (row, col).

strandings_from_space (strandings_from_space_pipeline.ipynb) custon built satellite image annotation user interface:
<p align="center">
  <img width="547" height="316" alt="stranding_from_space_annotation_pipeline" src="https://github.com/user-attachments/assets/015c1ca2-fbe5-4456-84d3-1ef660ca414b" />
</p>

Example semi-automated clustering output, useful evaluating count congruence between annotations made by more than one observer (green square = 3 observers, yellow circle = 2 observers, blue triangle = 1 observer). This workflow is adaptable to any number of observer annotations and functionable for geolocated satellite data (latitude, longitude) and unknown reference aerial data (row, col). Aerial image © Department of Conservation, New Zealand.
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
  - [‘strandings_from_space_pipeline.ipynb’](#‘strandings_from_space_pipeline.ipynb’)
  - [‘otb_pansharpening.ipynb’](#‘otb_pansharpening.ipynb’)
  - [‘cetacean_strandings_from_space_comparing_counts.ipynb’](#‘cetacean_strandings_from_space_comparing_counts.ipynb’)
- [Licence](#licence)
- [Funding](#funding)
- [Citation](#citation)
- [References](#References)

## 1. Purpose
Cetacean strandings offer significant conservation value for the assessment of ecosystems and serve as early warning of emerging concerns regarding animal, ocean, and human health. However stranding monitoring programmes are scarce or non-existent along minimally populated areas, coastlines with limited economic resources, geographically remote areas, complex coastlines and areas of geopolitical unrest. VHR satellite imagery offers the prospect of improving monitoring in these regions. 

An important consideration for the scalability of VHR satellite imagery to monitor large expanses of remote and low to mid economically resourced coastlines, is increasing accessibility. This includes access to imagery, knowledge, sharing expertise, infrastructure and open access tools and protocols. The development of best practice open-source standardised workflows and training is also recognised and recommended by the International Whaling Commission as important for the future utility of VHR satellite imagery to study cetaceans.

'strandings_from_space' shares openly accessible pipelines and workflows for satellite image pre-processing, annotation and analysis using Python and QGIS. The tools are designed for ecologists and conservation managers, to work towards a globally scalable solution for analysing satellite imagery, and to allow local stranding networks, governments and NGOs to implement strandings monitoring along their own coastlines. **The workflows are also applicable beyond the strandings and wildlife from space community, as it forms a framework supporting remote sensing applications, which require image annotation.**

## 2.	Methodology
The repository includes a robust standardised open-source protocol for pre-processing and analysing VHR satellite imagery for stranded cetaceans, developed in QGIS 3.28 (S2_QGIS_Strandings_from_Space_Pipeline.pdf). The standardised protocol was adapted from Cubaynes et al. (2023) and refined based on feedback from remote sensing and cetacean experts. A template for recording annotation metadata (e.g., confidence scores, satellite metadata, feature information, and environmental conditions) and an accompanying training document (S4_attribute_training_document.pdf) was co-developed, and reviewed by stranding experts and the international ‘Satellites to Study Whales’ community. This approach ensures that future stranding datasets can be collected and formatted under consistent data standards. The importance of open-source software was emphasised, to improve access and uptake in under-resourced regions. Therefore, as well as a user-interface centred pipeline in QGIS, a replicable version of the workflow was developed using Python 3.10, presented here (strandings_from_space_pipeline.ipynb). The strandings_from_space Python pipeline specifically offers a powerful future-facing tool given its ability to allow customisable script, which can be adapted to different user’s needs.

A visual representation of the steps within the python custom tool (strandings_from_space_pipeline.ipynb) and QGIS workflow (S2_QGIS_Strandings_from_Space_Pipeline.pdf) is available as pseudo code below: <br>

<img width="2223" height="3014" alt="Process_flow" src="https://github.com/user-attachments/assets/779e098b-2d86-40b7-87bb-6d992a2e81c6" /> <br>

The python custom tool (strandings_from_space_pipeline.ipynb) offers three methods to perform pansharpening. Pansharpening takes the panchromatic and multispectral satellite images, and where the two rasters fully overlap, fuses them together to produce a multispectral image with the higher spatial resolution (the distance on the ground represented per pixel) of the panchromatic image. Two pansharpening methods (GDAL and Miscrosoft) can be ran within the strandings_from_space_pipeline.ipynb and its associated environment, however, the third method (OTB) requires a seperate environment and workbook (otb_pansharpening.ipynb). Orfeo Toolbox (OTB), Bundle To Perfect Sensor tool, at present must be operated seperately for Windows OS systems. The method is included and recommended here given its valuable ability to preserve all multispectral bands in the pansharpening process, unlike the other methods. The seperate operation is offered as an intemediary solution until newer versions of Orfeo Toolbox are available with conda installation capabilities for Windows OS.

To compare observers’ annotations, which can be useful for evaluating count congruence and confidence in detections, a semi-automated hierarchical clustering approach can be performed using a python script (v3.12) adapted from Attard et al. (2025) availble here (cetacean_strandings_from_space_comparing_counts.ipynb). This workflow is adaptable to any number of observer annotations and functionable for geolocated satellite data (latitude, longitude) and unknown reference aerial data (row, col)).

## 3.	Repository structure 
### 3.1	‘compare_counts’
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1	 'inputs' <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1.1  'aerial_ref' <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1.2  'ground_ref' <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1.3  'satellite' <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.2	 'ouputs' <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.2	 'temp_ouputs' <br>
### 3.2	‘inputs’

### 3.3	‘outputs’

### 3.4	‘qgis’

### 3.5	‘temp_outputs’

### 3.6	‘cetacean_strandings_from_space_comparing_counts.ipynb’

### 3.7	‘compare_counts.yml’

### 3.8	‘otb.yml’

### 3.9	‘otb_pansharpening.ipynb’

### 3.10	‘S4_attribute_training_document.pdf’

### 3.11	‘strandings_from_space_pipeline.ipynb’

### 3.12	‘videos’

## 4.	Getting started and requirements <br>

### 4.1 Install Python distribution using Anaconda <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.1.	[Download Anaconda for your OS](https://www.anaconda.com/download) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.2.	Install it following [these instructions](https://docs.anaconda.com/anaconda/install/) <br>

### 4.2 Clone the strandings_from_space repository to your local drive by either: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.1.	 Visit https://github.com/PennyJClarke/strandings_from_space.git, select the dropdown arrow to the right of the green ‘Code’ button and selecting ‘Download ZIP’, extract to your desktop (the code automatically identifies and expects the repository to be located on the Desktop) <br>
<img width="236" height="203" alt="clone_env" src="https://github.com/user-attachments/assets/79dd94ed-f20d-4098-91cd-85e5130e2097" /> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.2.	Or, in your windows powershell, anaconda prompt window or equivalent, navigate to your desktop to clone the repository using (amend link to users Desktop): <br>
<pre>
<code id="code-block">cd C:\\Users\\Desktop</code> <button onclick="copyCode()"></button>
</pre>
followed by: <br>
<pre>
<code id="code-block">git clone https://github.com/PennyJClarke/strandings_from_space.git</code> <button onclick="copyCode()"></button>
</pre>
### 4.3 Create the environments
Make sure Anaconda is installed and the strandings_from_space Github repository is downloaded.<br>
Open the command line (e.g., Anaconda prompt on Windows, Terminal on Mac and Linux).<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.3.1 **Create an environment (sfs) to run the ‘strandings_from_space_pipeline.ipynb’** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.3.1.1 Run the following in the Anaconda prompt or Terminal window to create the environment named sfs: <br>
<pre>
<code id="code-block">conda create -n sfs python=3.10 gdal geopandas opencv matplotlib pandas numpy scikit-image ipython notebook shapely ipyleaflet leafmap rioxarray rasterio fiona libgdal-jp2openjpeg</code> <button onclick="copyCode()"></button>
</pre> <br>
If the above ran well and you see a 'Proceed' command, skip this guidance, however, if there are any issues installing packages, you may need to set a strict priority to use conda-forge channel for installation, in this case run the following prior to the creation of the sfs environment code:
<pre>
<code id="code-block">conda config --show channels</code> <button onclick="copyCode()"></button>
</pre> <br>
<pre>
<code id="code-block">conda config --show channel_priority</code> <button onclick="copyCode()"></button>
</pre> <br>
<pre>
<code id="code-block">conda config --add channels conda-forge</code> <button onclick="copyCode()"></button>
</pre> <br>
<pre>
<code id="code-block">conda config --set channel_priority strict</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.3.1.2 When prompted to 'Proceed' type y to proceed: <br>
<pre>
<code id="code-block">y</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.3.1.3 When prompted 'To activate this environment, use' type conda activate sfs to activate: <br>
<pre>
<code id="code-block">conda activate sfs</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.3.1.3 Once all packages are installed using conda-forge, install localtileserver using pip, it is important to ensure any packages that can be installed by pip only are ran after use of any conda channels: <br>
<pre>
<code id="code-block">pip install localtileserver</code> <button onclick="copyCode()"></button>
</pre> <br>
The guidance given to create sfs environment takes python version 3.10 and will upload the newest versions of all remaining packages. If there are any issues with the code operation, the environment could be created with the known functioning versions of packages: <br> 
<pre>
<code id="code-block">conda create -n sfs python=3.10 gdal=3.10.3 geopandas=1.1.0 opencv=4.11.0 matplotlib=3.10.3 pandas=2.3.0 numpy=2.2.6 scikit-image=0.25.2 ipython=8.37.0 notebook=7.4.3 shapely=2.1.1 ipyleaflet=0.20.0 leafmap=0.48.3 rioxarray=0.19.0 rasterio=1.4.3 fiona=1.10.1 libgdal-jp2openjpeg=3.10.3</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.3.1.4 Once the environment is set up, navigate to the location of the downloaded github repository for strandings_from_space (ensure to amend the below Desktop link with unique user_id): <br>
<pre>
<code id="code-block">cd C:\Users\user_id\Desktop\strandings_from_space</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.3.1.5 Open jupyter notebook to access the workbook and to run the code, type jupyter notebook: <br>
<pre>
<code id="code-block">jupyter notebook</code> <button onclick="copyCode()"></button>
</pre> <br>
This will open jupyter notebook in a web browser, the browser will populate with the list of files and directories contained within the strandings_from_space downloaded Github repository. To open the stranding_from_space pipeline, click the strandings_from_space_pipeline.ipynb.<br>

To return to the environment and run the code on another occasion, open Anaconda prompt and activate the sfs environment as per the command in 4.3.1.3 (in Linux / Mac if your default shell is not bash, first type bash. Activate the relevant environment by typing: 'source activate sfs'): <br>
<pre>
<code id="code-block">conda activate sfs</code> <button onclick="copyCode()"></button>
</pre> <br>
The environment will change from (base) to (sfs), then follow steps 4.3.1.4. and 4.3.1.5 to open the notebook. <br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1 **Create an environment (otb) to run the ‘otb_pansharpening.ipynb’** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.1 <br> [Download](https://www.orfeo-toolbox.org/packages/archives/OTB/) Orfeo Toolbox version Windows 8.0.1-Win64 <br>

Please note, OTB version 8.0.1-Win64 with Python 3.7, is currently the latest version that is operable for Windows. For operating systems Linux and Mac (which the tool is designed to work with), see the Orfeo Toolbox guidance for setting up a newer version (for the most up to date version you can download using this link: Download – Orfeo ToolBox (orfeo-toolbox.org)). <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.2 Unzip the folder ‘8.0.1-Win64’ directly into the ‘strandings_from_space’ folder within the repository you have cloned from GitHub, to your Desktop. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.3 <br> Open Anaconda Prompt and navigate to the ‘strandings_from_space’ folder within the repository you have cloned from GitHub to your Desktop, using the command ‘cd’ (amend the link to your specific user_id Desktop location):
<pre>
<code id="code-block">cd C:\Users\user_id\Desktop\strandings_from_space</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.4 Copy and paste the following command into the prompt window to access the otb.yml file to create an environment called ‘otb’ with the required packages to run the pansharpening code in the otb_pansharpening.ipynb workbook: <br>
<pre>
<code id="code-block">conda env create -f otb.yml</code> <button onclick="copyCode()"></button>
</pre> <br>
Else if this fail create an environment manually: create a new environment called ‘otb’ with python 3.7: <br>
<pre>
<code id="code-block">conda create -n otb python=3.7</code> <button onclick="copyCode()"></button>
</pre> <br>
Activate the new environment: <br> 
<pre>
<code id="code-block">conda activate otb</code> <button onclick="copyCode()"></button>
</pre> <br>
Install numpy: <br>
<pre>
<code id="code-block">conda install -c conda forge numpy</code> <button onclick="copyCode()"></button>
</pre> <br>
Install jupyter notebook (example uses jupyter as a command, if this fails to install amend jupyter to notebook 'conda install -c conda-forge notebook': <br>
<pre>
<code id="code-block">conda install -c conda-forge jupyter</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.5 Change the directory to the extracted OTB-8.0.1-Win64 directory (amend the link to your specific user_id Desktop location): <br>
<pre>
<code id="code-block">cd C:\Users\user_id\Desktop\strandings_from_space\OTB-8.0.1-Win64</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.6 Run the otbenv.bat file to set up the environment variables and paths required to use Orfeo Toolbox in Python: <br>
<pre>
<code id="code-block">otbenv.bat</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.7 Navigate back to the ‘strandings_from_space’ folder within the repository you have cloned from GitHub, using the command ‘cd’ (amend the link to your specific user_id Desktop location): <br>
<pre>
<code id="code-block">cd C:\Users\user_id\Desktop\strandings_from_space</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.8 Open jupyter notebook by typing ‘jupyter notebook’ in the prompt window, this should automatically open the jupyter notebook webpage: <br>
<pre>
<code id="code-block">jupyter notebook</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.5.1 **Create an environment (compare_counts) to run the ‘cetacean_strandings_from_space_comparing_counts.ipynb’** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.5.1.1 <br>

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

## 8. References <br>

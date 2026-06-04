# strandings_from_space
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20547057.svg)](https://doi.org/10.5281/zenodo.20547057) <br>

A very high-resolution (VHR) satellite image pre-processing and annotation pipeline for stranded whales and dolphins (adaptable to any feature of interest), and a semi-automated multi-observer annotation comparison workflow for evaluating count congruence, for annotations made in geolocated satellite imagery (latitude, longitude) and unknown reference aerial imagery (row, col).

Example strandings_from_space pipeline (strandings_from_space_pipeline.ipynb), a VHR satellite image annotation user interface, with custom attribute table that integrates dropdown entries of the required and desirable attributes for the strandings from space community, reviewed by stranding experts and the wider ‘Using Satellites to Study Whales’ community during a best practice workshop at the Society of Marine Mammalogy Conference 2024:
<p align="center">
  <img width="547" height="316" alt="stranding_from_space_annotation_pipeline" src="https://github.com/user-attachments/assets/015c1ca2-fbe5-4456-84d3-1ef660ca414b" />
</p>

Example semi-automated clustering output, useful for evaluating count congruence between annotations made by more than one observer (green square = 3 observers, yellow circle = 2 observers, blue triangle = 1 observer). This workflow is adaptable to any number of observer annotations and functionable for geolocated satellite data (latitude, longitude) and unknown reference aerial data (row, col). Aerial image © Department of Conservation, New Zealand.
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
  - [‘S3_attribute_training_document.pdf’](#‘S3_attribute_training_document.pdf’)
  - [‘strandings_from_space_pipeline.ipynb’](#‘strandings_from_space_pipeline.ipynb’)
  - [‘videos’](#‘videos’)
- [Getting started and requirements](#getting-started-and-requirements)
  - [‘strandings_from_space_pipeline.ipynb’](#‘strandings_from_space_pipeline.ipynb’)
  - [‘otb_pansharpening.ipynb’](#‘otb_pansharpening.ipynb’)
  - [‘cetacean_strandings_from_space_comparing_counts.ipynb’](#‘cetacean_strandings_from_space_comparing_counts.ipynb’)
- [Licence](#licence)
- [Funding](#funding)
- [Citation](#citation)
  - [‘Data’](#‘Data’)
- [References](#References)

## 1. Purpose
Cetacean strandings offer significant conservation value for the assessment of ecosystems and serve as early warning of emerging concerns regarding animal, ocean, and human health. However stranding monitoring programmes are scarce or non-existent along minimally populated areas, coastlines with limited economic resources, geographically remote areas, complex coastlines and areas of geopolitical unrest. VHR satellite imagery offers the prospect of improving monitoring in these regions. 

An important consideration for the scalability of VHR satellite imagery to monitor large expanses of remote and low to mid-resource coastlines, is increasing accessibility. This includes access to imagery, knowledge, sharing expertise, infrastructure, and open access tools and protocols. The development of best practice open-source standardised workflows and training is also recognised and recommended by the International Whaling Commission as important for the future utility of VHR satellite imagery to study cetaceans.

'strandings_from_space' shares openly accessible pipelines and workflows for satellite image pre-processing, annotation, and analysis using Python and QGIS. The tools are designed for ecologists and conservation managers, to work towards a globally scalable solution for analysing satellite imagery, and to allow local stranding networks, governments and NGOs to implement strandings monitoring along their own coastlines. **The workflows are also applicable beyond the strandings and wildlife from space community, as it forms a framework supporting remote sensing applications, which require image annotation. The custom attribute table dropdowns, can be adapted to new projects.**

## 2.	Methodology
The repository includes a robust standardised open-source protocol for pre-processing and analysing VHR satellite imagery for stranded cetaceans, initially developed in QGIS 3.28 (S1_QGIS_Strandings_from_Space_Pipeline.pdf). The standardised protocol was adapted from Cubaynes et al. (2023) and refined based on feedback from remote sensing and cetacean experts. A template for recording annotation metadata (S4_template_shapefile, e.g., confidence scores, satellite metadata, feature information, and environmental conditions) and an accompanying training document (S3_attribute_training_document.pdf) was co-developed, and reviewed by stranding experts and the international ‘Using Satellites to Study Whales’ community. This approach ensures that future stranding datasets can be collected and formatted under consistent data standards. The importance of open-source software was emphasised, to improve access and uptake in under-resourced regions. Therefore, as well as a user-interface centred pipeline in QGIS, a replicable version of the workflow was developed using Python 3.10, presented here (strandings_from_space_pipeline.ipynb). The strandings_from_space Python pipeline specifically offers a powerful future-facing tool given its ability to allow customisable script, which can be adapted to different user’s needs.

A visual representation of the steps within the python custom tool (strandings_from_space_pipeline.ipynb) and QGIS workflow (S1_QGIS_Strandings_from_Space_Pipeline.pdf) is available as pseudo code below: <br>

<img width="2481" height="3508" alt="Figure_1_updated_v1" src="https://github.com/user-attachments/assets/b4667ed5-ac05-4237-8cc7-1f03e9a50f2d" /> <br>

For full details each of the steps and more information on acquiring satellite imagery, view the associated MethodsX manuscript, Clarke et al., (2026): https://doi.org/10.1016/j.mex.2026.103949, and 'S1_QGIS_Strandings_from_Space_Pipeline' in either the 'qgis' folder in this repository (most up-to-date version: https://github.com/PennyJClarke/strandings_from_space) or in the supplemental materials of the associated MethodsX manuscript: https://doi.org/10.1016/j.mex.2026.103949. <br>

Due to licencing agreements, satellite imagery used in Clarke et al., (Under review): 'Odontocete strandings from space: Accurately counting individuals with very high-resolution optical and synthetic aperture radar satellite imagery' are not shared here or in the associated dataset (https://doi.org/10.5285/b26c3a3d-73c8-4500-9a23-696011c20a45), however, the full satellite imagery metadata (optical: GeoEYE-1, Worldview-2 (WV2) and Worldview-3 (WV3), Pleiades, and SAR: TerraSAR-X) associated with the data are provided in supplemental S1 of Clarke et al., (Under review). <br>

To test the 'strandings_from_space.ipynb' code and understand its capabilities, free data (not containing stranded cetaceans) can be downloaded from Vantor on the following links: <br>
[50 cm imagery](https://vantor.com/resources/sample-view-ready-or2a-stereo-tripoli/) <br>
[30 and 15 (HD) cm imagery](https://vantor.com/resources/samples-15-cm-hd-and-30-cm-native-imagery-or-solar-panel-dataset-or-germany/) <br>

The python custom tool (strandings_from_space_pipeline.ipynb) offers two methods to perform pansharpening. Pansharpening takes the panchromatic and multispectral satellite images, and where the two rasters fully overlap, fuses them together to produce a multispectral image with the higher spatial resolution (the distance on the ground represented per pixel) of the panchromatic image. GDAL pansharpening can be ran within the strandings_from_space_pipeline.ipynb and its associated environment, however, the Orfeo Toolbox (OTB) method requires a seperate environment and workbook (otb_pansharpening.ipynb). OTB, Bundle To Perfect Sensor tool, at present must be operated seperately for Windows OS systems. The method is included and recommended here given its valuable ability to preserve all multispectral bands in the pansharpening process, unlike the other methods. The seperate operation is offered as an intemediary solution until newer versions of Orfeo Toolbox are available with conda installation capabilities for Windows OS.

To compare observers’ annotations, which can be useful for evaluating count congruence and confidence in detections, a semi-automated hierarchical clustering approach can be performed using a python script (v3.12) adapted from Attard et al. (2025) availble here (cetacean_strandings_from_space_comparing_counts.ipynb). This workflow is adaptable to any number of observer annotations and functionable for geolocated satellite data (latitude, longitude) and unknown reference aerial data (row, col)). The workflow facilitates comparison of observer annotations to ground count values, to validate accuracy. The clustering applies Wards method to amass points within a user-defined distance threshold, by calculating pairwise distances between individual points to form each cluster, and iteratively merging pairs of clusters to minimise within cluster variance. To improve clustering accuracy, created clusters are further refined using a series of constraints, whereby clusters must not exceed the maximum number of observers and each unique observer must only occur once. The centroid of each cluster is computed and the furthest duplicate of an observer is removed and re-clustered within a distance threshold. Re-clustering ensures to exclude the current cluster and any existing clusters that exceed the maximum number of observers, and those already containing the unique observer, else a new cluster was created. <br>

## 3.	Repository structure 
### 3.1	‘compare_counts’ <br>
This folder is designed to load the inputs and recieve the outputs of the semi-automated clustering code associated with the 'cetacean_strandings_from_space_comparing_counts.ipynb' workbook. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1	 **'inputs'** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1.1  **'aerial_ref'** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1.1.1  **'counts'**: contains a .gitkeep file for the purposes of maintaining folder structure to run the code. ‘counts’ expects .csv format point annotations made by multiple observers per aerial image (each observers annotations are in a seperate .csv file), with the file naming convention e.g., ‘chatham_island_aerial_1.csv’, equal to chatham_island = location, aerial = sensor type, and 1 = observer. Annotations are expected to include id, pixel-based coordinates (row, col), feature type ‘stranded_cetacean', and certainty level ‘definite’, ‘likely’, and ‘possible’. See associated dataset for examples: https://doi.org/10.5285/b26c3a3d-73c8-4500-9a23-696011c20a45. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1.1.2  **'images'**: contains a .gitkeep file for the purposes of maintaining folder structure to run the code. ‘images’ expects .jpg format aerial imagery corresponding to the observer annotations, with the file naming convention e.g., ‘chatham_island_aerial.jpg’, equal to chatham_island = location and aerial = sensor type. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1.2  **'ground_ref'**: contains a .gitkeep file for the purposes of maintaining folder structure to run the code. 'ground_ref' expects .csv format of total ground counts ‘ref_value’, listed by sensor type ‘satellite’ per each respective image catalogue id ‘img_id’.See associated dataset for examples: https://doi.org/10.5285/b26c3a3d-73c8-4500-9a23-696011c20a45. <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1.3  **'satellite'** <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1.3.1  **'counts'**: contains a .gitkeep file for the purposes of maintaining folder structure to run the code. ‘counts’ expects .csv format point annotations made by multiple observers per satellite image (each observers annotations are in a seperate .csv file), with the file naming convention e.g., chatham-island_geoeye1_105001002F60AA00_20221014_213434_50_1.csv equal to ‘location_satellite_image-catalog-id_image-date(YYYYMMDD)_image-time(HHMMSS)_spatial-resolution_observer-id’. Annotations are expected as a minimum to include the required attributes and can be supplemented with the desirable attributes outlined in the standardised protocols (S3_attribute_training_document.pdf, included here) and should include georeferenced coordinates (longitude, latitude). See associated dataset for examples: https://doi.org/10.5285/b26c3a3d-73c8-4500-9a23-696011c20a45. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1.3.2  **'images'**: contains a .gitkeep file for the purposes of maintaining folder structure to run the code. ‘images’ expects .tif format satellite imagery corresponding to the observer annotations, with the file naming convention e.g., chatham-island_geoeye1_105001002F60AA00_20221014_213434_50.tif equal to ‘location_satellite_image-catalog-id_image-date(YYYYMMDD)_image-time(HHMMSS)_spatial-resolution’. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.2	 **'ouputs'** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1.3.2  **'clusters'**: contains a .gitkeep file for the purposes of maintaining folder structure to run the code. ‘clusters’ is a folder to receive .csv format point annotation outputs from the semi-automated clustering process, showing the median of all observer points within a cluster. The file naming convention will be the satellite or aerial count input .csv filename ending with ‘_predicted.csv’. Cluster file outputs for satellite imagery will contain the ‘id’ of each observer’s points contained within a cluster (ordered by observer [1, 2, 3]). The ‘label_count’ equal to the number of observer points per cluster. The breakdown of certainty of those observations per cluster ‘definite_count’, ‘likely_count’, and ‘possible_count’, the ‘majority_label’ by certainty, and the georeferenced coordinates (latitude, longitude). Cluster files for aerial imagery will contain the ‘label_count’ equal to the number of observer points per cluster, the breakdown of certainty of those observations per cluster ‘definite_count’, ‘likely_count’, and ‘possible_count’, the ‘majority_label’ by certainty and the pixel-based coordinates (row, col in columns ‘x’, ‘y’). <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.2	 **'temp_ouputs'** contains a .gitkeep file for the purposes of maintaining folder structure to run the code. This folder is to receive any temporary outputs as the clustering code processes steps to reach the final outcome. <br>
### 3.2	‘inputs’
This folder is designed to load the inputs associated with the satellite image pre-proceesing and image annotation pipeline, 'strandings_from_space.ipynb'. The folder contains a .gitkeep file for the purposes of maintaining folder structure to run the code. The folder expects the panchromatic and multispectral satellite image files and their associated metadata. For example, for Vantor imagery, load in the folder containing the panchromatic image and metadata '056117128010_01_P001_PAN' and multispectral image and metadata '056117128010_01_P001_MUL' seperately. <br>
### 3.3	‘outputs’
This folder is designed to receive the outputs associated with the satellite image pre-processing and image annotation pipeline, 'strandings_from_space.ipynb'. The folder contains a .gitkeep file for the purposes of maintaining folder structure to run the code. <br>
### 3.4	‘qgis’
This folder contains the robust standardised open-source protocol for pre-processing and analysing VHR satellite imagery for stranded cetaceans, developed in QGIS 3.28 (S1_QGIS_Strandings_from_Space_Pipeline.pdf). This is a replication of the python version shared here in 'strandings_from_space.ipynb'. The standardised protocol was adapted from Cubaynes et al. (2023) and refined based on feedback from remote sensing and cetacean experts. In addition, a template for recording annotation metadata (e.g., confidence scores, satellite metadata, feature information, and environmental conditions) and an accompanying training document was co-developed, and reviewed by stranding experts and the international ‘Using Satellites to Study Whales’ community. The template .shp and accompany files are available in this folder and the training document ‘S3_attribute_training_document.pdf’ is available in the main 'strandings_from_space' folder. Finally a .py script 'S2_png_creation.py' to extract image chips as .jpeg format from QGIS using the pyqgis console, is available. <br>
### 3.5	‘temp_outputs’
This folder is designed to receive the temporary outputs associated with the satellite image pre-processing and image annotation pipeline, 'strandings_from_space.ipynb'. The folder contains a .gitkeep file for the purposes of maintaining folder structure to run the code. <br>
### 3.6	‘cetacean_strandings_from_space_comparing_counts.ipynb’
This workflow allows semi-automated clustering of multi-observer annotations (expected in .csv format), useful for evaluating count congruence and confidence in observer detections. This workflow is adaptable to any number of observer annotations and functionable for geolocated satellite data (latitude, longitude) and unknown reference aerial data (row, col). The workflow facilitates comparison of observer annotations to ground count values, to validate accuracy (expected in .csv format). The workbook provides clear commenting throughout to guide the user on how to process their data. The associated dataset can be accessed for example of formatting and running the code: https://doi.org/10.5285/b26c3a3d-73c8-4500-9a23-696011c20a45. <br> 
### 3.7	‘compare_counts.yml’
Is a .yaml source file used to create the environment 'compare_counts' associated with the running of the semi-automated clustering workflow, ‘cetacean_strandings_from_space_comparing_counts.ipynb’. <br>
### 3.8	‘otb.yml’
Is a .yaml source file used to create the environment 'otb' associated with the running of Orfeo Toolbox 'Bundle to Perfect Sensor' pansharpening tool in the workbook, ‘otb_pansharpening.ipynb’. <br>
### 3.9	‘otb_pansharpening.ipynb’
Is a workbook to run Orfeo Toolbox 'Bundle to Perfect Sensor' pansharpening tool. The workbook provides clear commenting throughout to guide the user on how to process their data.<br>
### 3.10	‘S3_attribute_training_document.pdf’
Is a training guide to aid the strandings community to assess the certainty of stranded cetaceans detected in VHR optical satellite imagery. The document provides (1) a descriptive guide and (2) a visual guide for the standardised (required and optional) attributes for data annotation. The guide should be viewed by observers ahead of reviewing VHR satellite imagery for stranded cetaceans, to familiarise themselves with examples of stranded cetaceans and confounding features. The guide is associated with the annotation metadata template in the 'qgis' folder and the custom attribute table dropdowns in the ‘strandings_from_space_pipeline.ipynb’ tool. <br>
### 3.11	‘strandings_from_space_pipeline.ipynb’
This workbook is a custom open-source VHR satellite image pre-processing and image annotation pipeline. The workbook provides clear commenting throughout to guide the user on how to process their data. <br>
### 3.12	‘videos’
Contains a video providing a visual example of how to use the custom strandings_from_space satellite image annotation tool. This video is also embedded in the ‘strandings_from_space_pipeline.ipynb’ pipeline at the location when the tool is initiated. <br> 

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
If the above ran well and you see a 'Proceed' command, skip this guidance and move to step 4.3.1.2. However, if there are any issues installing packages, you may need to set a strict priority to use conda-forge channel for installation, in this case run the following prior to the creation of the sfs environment code:
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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.3.1.3 Once all packages are installed using conda-forge, install localtileserver using pip, it is important to ensure any packages that are installed by pip are ran after use of any conda channels: <br>
<pre>
<code id="code-block">pip install localtileserver</code> <button onclick="copyCode()"></button>
</pre> <br>
The guidance given to create the sfs environment takes python version 3.10 and will install the latest versions of all remaining packages. If there are any issues with the code operation, the environment could be created with the known functioning versions of packages: <br> 
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
The environment will change from (base) to (sfs), then follow steps 4.3.1.4 and 4.3.1.5 to open the notebook. <br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1 **Create an environment (otb) to run the ‘otb_pansharpening.ipynb’** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.1 [Download](https://www.orfeo-toolbox.org/packages/archives/OTB/) Orfeo Toolbox version Windows 8.0.1-Win64 <br>
Please note, OTB version 8.0.1-Win64 with Python 3.7, is currently the latest version that is operable for Windows. For operating systems Linux and Mac (which the tool is designed to work with), see the Orfeo Toolbox guidance for setting up a newer version (for the most up to date version you can download using this link: Download – Orfeo ToolBox (orfeo-toolbox.org)). <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.2 Unzip the folder ‘8.0.1-Win64’ directly into the ‘strandings_from_space’ folder within the repository you have cloned from GitHub, to your Desktop. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.3 Open Anaconda Prompt and navigate to the ‘strandings_from_space’ folder within the repository you have cloned from GitHub to your Desktop, using the command ‘cd’ (amend the link to your specific user_id Desktop location):
<pre>
<code id="code-block">cd C:\Users\user_id\Desktop\strandings_from_space</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.4 Copy and paste the following command into the prompt window to access the otb.yml file to create an environment called ‘otb’ with the required packages to run the pansharpening code in the otb_pansharpening.ipynb workbook: <br>
<pre>
<code id="code-block">conda env create -f otb.yml</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.5 Activate the otb environment: <br>
<pre>
<code id="code-block">conda activate otb</code> <button onclick="copyCode()"></button>
</pre> <br>
Proceed to 4.4.1.6, else if creating the environment fails, create manually: create a new environment called ‘otb’ with python 3.7: <br>
<pre>
<code id="code-block">conda create -n otb python=3.7</code> <button onclick="copyCode()"></button>
</pre> <br>
Activate the otb environment: <br> 
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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.6 Change the directory to the extracted OTB-8.0.1-Win64 directory (amend the link to your specific user_id Desktop location): <br>
<pre>
<code id="code-block">cd C:\Users\user_id\Desktop\strandings_from_space\OTB-8.0.1-Win64</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.7 Run the otbenv.bat file to set up the environment variables and paths required to use Orfeo Toolbox in Python: <br>
<pre>
<code id="code-block">otbenv.bat</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.8 Navigate back to the ‘strandings_from_space’ folder within the repository you have cloned from GitHub, using the command ‘cd’ (amend the link to your specific user_id Desktop location): <br>
<pre>
<code id="code-block">cd C:\Users\user_id\Desktop\strandings_from_space</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1.9 Open jupyter notebook by typing ‘jupyter notebook’ in the prompt window, this should automatically open the jupyter notebook webpage: <br>
<pre>
<code id="code-block">jupyter notebook</code> <button onclick="copyCode()"></button>
</pre> <br>
*Before opening jupyter notebook, a user can check otb is operating by typing ‘python’ into the Anaconda prompt window, this will open python and then type ‘import otbApplication’ if you receive no errors the import has worked correctly. Type 'exit()' to leave the python session and then return to typing 'jupyter notebook' to open the code.* <br>

If you receive an error message that notebooks cannot open, open the Anaconda Navigator app, under ‘All applications’ on ‘otb’ channel, locate ‘notebook’, and using the wheel icon in the top right of the application, click, remove application, then click install application and retry notebook, running using ‘Launch’. <br>
<img width="583" height="287" alt="sfs_4" src="https://github.com/user-attachments/assets/30c20db1-4751-40d6-b12e-d7b0a71d2895" /> <br>

This will open jupyter notebook in a web browser, the browser will populate with the list of files and directories contained within the strandings_from_space downloaded Github repository. To open the pansharpening workbook, click the otb_pansharpening.ipynb. <br>

To return to the environment and run the code on another occasion, open Anaconda prompt and activate the otb environment as per the command in 4.4.1.5 (in Linux / Mac if your default shell is not bash, first type bash. Activate the relevant environment by typing: 'source activate otb'): <br>
<pre>
<code id="code-block">conda activate otb</code> <button onclick="copyCode()"></button>
</pre> <br>
The environment will change from (base) to (otb), then follow steps 4.4.1.8 and 4.4.1.9 to open the notebook. <br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.5.1 **Create an environment (compare_counts) to run the ‘cetacean_strandings_from_space_comparing_counts.ipynb’** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.5.1.1 Open Anaconda Prompt and navigate to the ‘strandings_from_space’ folder within the repository you have cloned from GitHub to your Desktop, using the command ‘cd’ (amend the link to your specific user_id Desktop location):
<pre>
<code id="code-block">cd C:\Users\user_id\Desktop\strandings_from_space</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.5.1.2 Copy and paste the following command into the prompt window to access the comparing_counts.yml file to create an environment called ‘compare_counts’ with the required packages to run the semi-automated clustering code in the cetacean_strandings_from_space_comparing_counts.ipynb workbook: <br>
<pre>
<code id="code-block">conda env create -f comparing_counts.yml</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.5.1.3 Activate the compare_counts environment: <br>
<pre>
<code id="code-block">conda activate compare_counts</code> <button onclick="copyCode()"></button>
</pre> <br>
Proceed to 4.5.1.4, else if creating the environment fails, create manually: create a new environment called ‘compare_counts’ with python 3.12: <br>
<pre>
<code id="code-block">conda create -n compare_counts python=3.12 pandas matplotlib seaborn numpy pillow scikit-learn scipy rasterio pyproj scikit-image notebook</code> <button onclick="copyCode()"></button>
</pre> <br>
The guidance above to create the compare_counts environment takes python version 3.12 and will install the latest versions of all remaining packages. If there are any issues with the code operation, the environment could be created with the known functioning versions of packages: <br> 
<pre>
<code id="code-block">conda create -n compare_counts python=3.12 pandas=2.2.2 matplotlib=3.9.1.post1 seaborn=0.13.2 numpy=2.0.1 pillow=10.4.0 scikit-learn=1.5.2 scipy=1.14.1 rasterio=1.3.11 pyproj=3.6.1 scikit-image=0.24.0 notebook=7.2.1</code> <button onclick="copyCode()"></button>
</pre> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.5.1.4 Open jupyter notebook by typing ‘jupyter notebook’ in the prompt window, this should automatically open the jupyter notebook webpage: <br>
<pre>
<code id="code-block">jupyter notebook</code> <button onclick="copyCode()"></button>
</pre> <br>

This will open jupyter notebook in a web browser, the browser will populate with the list of files and directories contained within the strandings_from_space downloaded Github repository. To open the semi-automated clustering workflow, click the cetacean_strandings_from_space_comparing_counts.ipynb.<br>

To return to the environment and run the code on another occasion, open Anaconda prompt and activate the compare_counts environment as per the command in 4.5.1.3 (in Linux / Mac if your default shell is not bash, first type bash. Activate the relevant environment by typing: 'source activate compare_counts'): <br>
<pre>
<code id="code-block">conda activate compare_counts</code> <button onclick="copyCode()"></button>
</pre> <br>
The environment will change from (base) to (compare_counts), then follow steps 4.5.1.1 and 4.5.1.4 to open the notebook. <br>

For examples of the code use, please view the associated publications at: (include link to published manuscripts). All the data associated with this publication is available on the British Antarctic Survey Polar Data Centre: (provide link). <br>

## 5.	Licence <br>
MIT License <br>

Copyright (c) 2026 PennyJClarke <br>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: <br>

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. <br>

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. <br>

## 6.	Funding <br>
This research has been supported by the Natural Environment Research Council (NERC) through a SENSE CDT studentship (grant no. NE/T00939X/1). The research was further supported by additional funding provided through, the British Antarctic Survey (BAS) Innovation Voucher, Sentinel Hub and their #30MapChallenge competition, BAS Ecosystems, and the support and cooperation of Airbus and Vantor (formerly Maxar Technologies Ltd), for their rapid response and efforts to enable successful collection of the imagery analysed here.

## 7. Citation <br>
To use this code or associated dataset, please cite (see https://github.com/PennyJClarke/strandings_from_space for the most up-to-date citations):<br>

**Associated manuscripts:**<br>
Clarke, P. J., Cubaynes, H. C., Stockin, K. A., Bowler, E., Carlyon, K., Attard, M. R. G., Fretwell, P. F., Skachkova, A., de Vos, A., McConnell, K. M., Medina-López, E., Lopez Dubon, S., and Jackson, J. A. (2026). _Open-source satellite image pre-processing and annotation workflows: Stranded whale and dolphin case study_. MethodsX. https://doi.org/10.1016/j.mex.2026.103949 <br>
Clarke, P. J., Cubaynes, H. C., Stockin, K. A., Bowler, E., Carlyon, K., Attard, M. R. G., Fretwell, P. F., Skachkova, A., de Vos, A., McConnell, K. M., Medina-López, E., Lopez Dubon, S., and Jackson, J. A. (Under review). _Odontocete strandings from space: Accurately counting individuals with very-high resolution optical and SAR satellite imagery_. Ecological Informatics. 

### 7.1 Data <br>
**Dataset for use with the semi-automated clustering workflow 'cetacean_strandings_from_space_comparing_counts.ipynb':**<br>
Clarke, P. J., Cubaynes, H. C., Bowler, E., Jackson, J. A., Attard, M. R. G., Stockin, K. A. and Carlyon, K. (2025). _Point annotation dataset of stranded whale and dolphin species identified in very high-resolution optical and SAR satellite imagery along offshore islands of New Zealand and Tasmania between 2018-2023 (Version 1.0) [Data set]_. NERC EDS UK Polar Data Centre. https://doi.org/10.5285/b26c3a3d-73c8-4500-9a23-696011c20a45

## 8. References <br>
Attard, M. R. G., Phillips, R. A., Oppel, S., Bowler, E. and Fretwell, P. T. 2025. _Feasibility of using very high-resolution satellite imagery to monitor Tristan albatrosses Diomedea dabbenena on Gough Island_. Endangered Species Research, 56, 187-199. https://doi.org/10.3354/esr01396. <br>
Cubaynes, H. C., Clarke, P. J., Goetz, K. T., Aladrich, T., Fretwell, P. T., Leonard, K. E. and Khan, C. B. 2023. _Annotating very high-resolution satellite imagery: A whale case study_. MethodsX, 10. https://doi.org/10.1016/j.mex.2023.102040. <br>

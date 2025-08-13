# https://gis.stackexchange.com/questions/68803/qgis-save-raster-as-rendered-image

# before running this script ensure the only active layers in the QGIS project are the clipped bounding box images to export

# set working directory to your desktop
# the code automatically selects your desktop
# for another location please amend the file path for main_path below
# get user's home directory
home_directory = os.path.expanduser('~')

# append the desktop folder to the home directory
desktop_directory = os.path.join(home_directory, 'Desktop')

# set and store the desktop as the working directory
os.chdir(desktop_directory)
print(f"The current working directory is set to: {os.getcwd()}")
main_path = os.getcwd()

# confirm whether the main_path exists
if os.path.exists(main_path):
    print(main_path, 'is a correct path'),
else:
    print(main_path, 'is not a correct path')

# create a number of folders to host the inputs and outputs of the code run through this script
folders = [
    'strandings_from_space\\inputs',
    'strandings_from_space\\outputs',
    'strandings_from_space\\temp_outputs'
]

# check if the directory folder exists or not
# if the directory is not present, then create it
for folder in folders:
    os.makedirs(os.path.join(main_path, folder), exist_ok=True)

# set the working path directories required throughout
input_path = os.path.join(main_path,'strandings_from_space\\inputs\\')
output_path = os.path.join(main_path,'strandings_from_space\\outputs\\')
temp_output_path = os.path.join(main_path,'strandings_from_space\\temp_outputs\\')

print(input_path)
print(output_path)
print(temp_output_path)

# capture all the active layers - all clipped bounding box images
layers = iface.mapCanvas().layers()
print(layers)

# for layer in active layers access the each clipped bounding box image metadata
# get the layer renderer, how the layer is visually represented in the QGIS project, to maintain the visual appearance
# save the clipped image as a .png
for layer in layers:
    extent = layer.extent()
    width, height = layer.width(), layer.height()
    renderer = layer.renderer()
    provider=layer.dataProvider()
    crs = layer.crs().toWkt()

    pipe = QgsRasterPipe()
    pipe.set(provider.clone())
    pipe.set(renderer.clone())
    item = layer.name()
    out_file = output_path + item + '.png'
    file_writer = QgsRasterFileWriter(out_file)
    print(f'Clipped .png saved to: {out_file}')
    file_writer.writeRaster(pipe,
                        width,
                        height,
                        extent,
                        layer.crs())

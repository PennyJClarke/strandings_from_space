#https://gis.stackexchange.com/questions/68803/qgis-save-raster-as-rendered-image

layers = iface.mapCanvas().layers()
print(layers)

out_path = 'C:\\Users\\s0951644\\Desktop\\strandings_from_space\\outputs\\'

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
    file_writer = QgsRasterFileWriter(out_path + item + '.png')
    file_writer.writeRaster(pipe,
                        width,
                        height,
                        extent,
                        layer.crs())

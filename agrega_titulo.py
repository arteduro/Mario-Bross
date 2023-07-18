import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Ruta de la imagen que se va a mostrar
img_path = 'Mario Bross.jpg'

# Cargar la imagen con la función imread de Matplotlib
img = mpimg.imread(img_path)

# Mostrar la imagen utilizando la función imshow de Matplotlib
plt.imshow(img)

# Agregar un título a la imagen
plt.title('Mario Bross')

# Desactivar los ejes de coordenadas
plt.axis('off')

# Mostrar la imagen en la ventana de Matplotlib
plt.show()

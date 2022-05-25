import tkinter as tk

from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance

from constants import HEIGHT

class NewImg:
    """
        Создание нового изображения на Canvas
    """
    def __init__(self, canvas, img, x, y, resize = 0, action = 0, size = 0, belonging = None, brightness=1, name = ""):
        """
            canvas - ссылка на объект холста (Canvas) -> object;
            img - ссылка на изображение -> str;
            x, y - координаты -> int;
            resize - 0 не изменять размер, 1 изменять -> int;
            action -> 0 делить (уменьшать) 1 увеличивать (умножать) -> int;
            size -> кортеж или int (размер необходимого изображения)
            belonging -> Принадлежит объект к локации True или нет False
            brightness - яркость, 1 - по-умолчанию, как у исходного изображения
        """
        self.url_image = img
        self.canvas = canvas
        self.x = x
        self.y = y
        self.resize = resize
        self.action = action
        self.size = size
        self.belonging = belonging
        self.brightness = brightness
        self.name = name
        self.render_image = self.new_image(img, x, y, resize, action, size, brightness)

    def set_size(self, width, height):
        self.width  = width
        self.height  = height

    def resize_by_proportion(self, action, size):
        """
            Изменение размера по пропорции, где size целое число
        """
        if action:
            self.set_size(int(self.width * size), int(self.height * size))
        else:
            self.set_size(int(self.width // size), int(self.height // size))

    def resize_by_value(self, size):
        """
            Изменение размера по значению, где size - это картеж (width, height)
        """
        width, height = size
        self.set_size(int(self.width + width), int(self.height + height))

    def resize_image(self, action, size):
        """
            Если action равен 1, тогда изображение увеличивается (умножается)
            иначе уменьшается (делится).
            Если size является картежем, тогда изменение проиходит по ширине и высоте,
            иначе пропорционально. 
        """
        if type(size) == tuple:
            self.resize_by_value(size)
        else:
            self.resize_by_proportion(action, size)

        return self.img.resize((self.width, self.height))

    def get_image(self, img, resize, action, size, brightness):
        """
            Метод возвращает загруженное изображение, которое можно передавать на отрисовку в create_image.
            Получает ссылку на изображение img, если в аргумент resize придет 1,
              тогда передается action, где 1 (увеличение изображения), а 0 (уменьшение)
               и size - это множитель, делитель или кортеж.
            brightness - яркость.
        """
        if not hasattr(self, 'img'):
            self.img = Image.open(img)
            self.set_size(self.img.width, self.img.height)
            self.enhancer = ImageEnhance.Brightness(self.img)
        self.img = self.enhancer.enhance(brightness)
        if resize:
            self.img = self.resize_image(action, size)
        return ImageTk.PhotoImage(self.img)
            
    def new_image(self, img, x, y, resize = 0, action = 0, size = (), brightness = 1):
        """
            Метод создает изображение на Canvas и возвращает идентификатор изображения
        """
        self.photo = self.get_image(img, resize, action, size, brightness)
        return self.canvas.create_image(x, y, anchor = 'nw', image = self.photo)
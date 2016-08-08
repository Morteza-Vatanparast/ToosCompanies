import base64
import os
import random

from PIL import Image
from classes.public import CreateId
from config import Config


class UploadPic:
    def __init__(self, name=None, handler=None, folder='avatars', default='default.jpg'):
        self.name = name
        self.default = default
        self.__handler = handler
        self.folder = folder
        self.result = []
        self.status = False

    def upload(self, count=1):
        try:
            pics = self.__handler.request.files[self.name][:count]
            for pic in pics:
                try:
                    extension = os.path.splitext(pic['filename'])[1].lower()
                    upload_folder = os.path.join(Config().applications_root, 'static', 'images', self.folder)
                    if not os.path.exists(upload_folder):
                        os.makedirs(upload_folder)
                    photo_name = CreateId().create_int() + extension
                    full_name = os.path.join(upload_folder, photo_name)
                    output = open(full_name, 'wb')
                    output.write(pic['body'])
                    output.close()
                    self.status = True
                    self.result.append(photo_name)
                except:
                    pass
            return self.result
        except:
            return []

    def upload_from_cropper(self, count=1, base64_str=None, name_format='{name}.{ext}'):
        try:
            if base64_str is None:
                base64_str = []
            for _str in base64_str[:count]:
                try:
                    _str = base64.b64decode(_str.split(",")[1].strip())
                    _path_dir = os.path.join(Config().applications_root, "static", "images", "temp")
                    if not os.path.exists(_path_dir):
                        os.makedirs(_path_dir)
                    _path = os.path.join(Config().applications_root, "static", "images", "temp", "img_tmp")
                    f = open(_path, "wb")
                    f.write(_str)
                    f.close()

                    img = Image.open(_path)
                    if img:
                        file_name = name_format.format(
                            name=str(random.randint(1155551918949, 91555519189459)),
                            ext=img.format.lower()
                        )
                        __folder = os.path.join(Config().applications_root, "static", "images", self.folder)
                        if not os.path.exists(__folder):
                            os.makedirs(__folder)
                        img.save(os.path.join(__folder, file_name))
                        self.result.append(file_name)
                except:
                    pass
            return self.result
        except:
            return []
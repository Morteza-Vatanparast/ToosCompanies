import os

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

    def upload(self):
        try:
            pics = self.__handler.request.files[self.name]
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

import os
import json



class Loader(object):

    def __init__(self):
        # ../
        proj_dir = os.path.dirname(os.path.abspath(__file__))
        self.training_dir = os.path.join(proj_dir, 'training_data')

    def seek_author_dir(self, last_name):
        training_dir = os.walk(self.training_dir, topdown=True)
        root, dirs, files = next(training_dir)
    
        for d in dirs:
            file_parts = d.split(' ')
            final_part = file_parts[len(file_parts) - 1]
            if final_part == last_name:
                return os.path.join(root, d)


    def load_author(self, last_name):
        author_dir = self.seek_author_dir(last_name)

        poems = []

        for file in os.listdir(author_dir):
            path = os.path.join(author_dir, file)
            with open(path, 'r') as content_file:
                content = content_file.read()
                poems.append(json.loads(content))

        return poems

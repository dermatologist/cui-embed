from pkg_resources import resource_filename
import os
import urllib.request
import zipfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec

class Cuimodel(object):

    def __init__(self):
        super().__init__()
        self.model_directory = resource_filename('cui_embed', 'model')

    def model(self):
        model_exists = os.path.exists(os.path.join(self.model_directory, 'cui2vec_gensim.bin'))
        if model_exists is not True:
            url = 'https://ndownloader.figshare.com/files/10959626'
            print('No model found. Downloading model...')
            urllib.request.urlretrieve(url, os.path.join(self.model_directory, 'cui2vec_pretrained.csv.zip'))
            print('This may take some time')
            print('Unzipping model...')
            with zipfile.ZipFile(os.path.join(self.model_directory, 'cui2vec_pretrained.csv.zip'), "r") as zip_ref:
                zip_ref.extractall(self.model_directory)
            print('Processing model...')
            with open(os.path.join(self.model_directory, 'cui2vec_pretrained.csv'), 'r') as f:
                with open(os.path.join(self.model_directory, "cui2vec_g.txt"), 'w') as f1:
                    next(f)  # skip header line
                    count = 0
                    for line in f:
                        line = '"'.join(line.split()).replace('"', '')
                        line = ",".join(line.split()).replace(',', ' ')
                        line = line + ' \n'
                        f1.write(line)
                        count += 1
            print('Converting model ...')
            glove2word2vec(os.path.join(self.model_directory, "cui2vec_g.txt"), os.path.join(self.model_directory, "cui2vec_w.txt"))
            wv_from_text = KeyedVectors.load_word2vec_format(os.path.join(self.model_directory, 'cui2vec_w.txt'), unicode_errors='ignore')
            wv_from_text.save_word2vec_format(os.path.join(self.model_directory, 'cui2vec_gensim.bin'), binary=True)
            print('Model processing completed ..')
        return KeyedVectors.load_word2vec_format(os.path.join(self.model_directory, 'cui2vec_gensim.bin'), unicode_errors='ignore', binary=True)

@staticmethod
def model(self):
    cm = Cuimodel()
    return cm.model()
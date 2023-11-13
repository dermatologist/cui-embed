import os
import urllib.request
import zipfile
import tempfile
from gensim.models import KeyedVectors, FastText
from gensim.scripts.glove2word2vec import glove2word2vec

class Cuimodel(object):

    def __init__(self, model="cui"):
        super().__init__()
        self.model_directory = tempfile.gettempdir()
        self.model_type = model
        if model == "cui":
            self.model_url = 'https://ndownloader.figshare.com/files/10959626'
            self.model_name = 'cui2vec_gensim.bin'
            self.model_text = 'cui2vec_g.txt'
        elif model == "loinc":
            self.model_url = "https://github.com/elleros/DSHealth2019_loinc_embeddings/raw/master/Data/loinc_s200_w5_c5_sg_wv.txt"
            self.model_name = 'loinc2vec_gensim.bin'
            self.model_text = 'loinc2vec_g.txt'
        elif model == "clinical":
            self.model_url = "https://huggingface.co/garyw/clinical-embeddings-300d-ft-cr/resolve/main/ft_oa_corp_300d.bin?download=true"
            self.model_name = ['ft_oa_corp_300d.bin', 'ft_oa_corp_300d.bin.wv.vectors.npy']
            self.model_text = ''
        else:
            raise ValueError("Model not found")

    def load_model(self):
        if self.model_type == "cui":
            url = self.model_url
            print('No model found. Downloading model...')
            urllib.request.urlretrieve(url, os.path.join(self.model_directory, 'cui2vec_pretrained.csv.zip'))
            print('This may take some time')
            print('Unzipping model...')
            with zipfile.ZipFile(os.path.join(self.model_directory, 'cui2vec_pretrained.csv.zip'), "r") as zip_ref:
                zip_ref.extractall(self.model_directory)
            print('Processing model...')
            with open(os.path.join(self.model_directory, 'cui2vec_pretrained.csv'), 'r') as f:
                with open(os.path.join(self.model_directory, self.model_text), 'w') as f1:
                    next(f)  # skip header line
                    count = 0
                    for line in f:
                        line = '"'.join(line.split()).replace('"', '')
                        line = ",".join(line.split()).replace(',', ' ')
                        line = line + ' \n'
                        f1.write(line)
                        count += 1
            print('Converting model ...')
            glove2word2vec(os.path.join(self.model_directory, self.model_text), os.path.join(
                self.model_directory, self.model_text))
        elif self.model_type == "loinc":
            url = self.model_url
            print('No model found. Downloading model...')
            urllib.request.urlretrieve(url, os.path.join(
                self.model_directory, self.model_text))
            print('This may take some time')
            wv_from_text = KeyedVectors.load_word2vec_format(os.path.join(
                self.model_directory, self.model_text), unicode_errors='ignore')
            wv_from_text.save_word2vec_format(os.path.join(
                self.model_directory, self.model_name), binary=True)
            print('Model processing completed ..')

        if self.model_type == "clinical":
            url = self.model_url
            print('No model found. Downloading model...')
            for _model in self.model_name:
                urllib.request.urlretrieve(url, os.path.join(
                    self.model_directory, _model))
            print('This may take some time')


    def model(self):
        model_exists = os.path.exists(self.model_directory)
        if model_exists is not True:
            self.load_model()
        if self.model_type != "clinical":
            return KeyedVectors.load_word2vec_format(os.path.join(self.model_directory, self.model_name), unicode_errors='ignore', binary=True)
        else:
            return FastText.load(os.path.join(self.model_directory, self.model_name[0]))

@staticmethod
def model(self):
    cm = Cuimodel()
    return cm.model()
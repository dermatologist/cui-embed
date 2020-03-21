# cui-embed

This is a gensim wrapper for the clinical (CUI) embeddings for the model [here](https://github.com/beamandrew/cui2vec)

* This does not include data/model.
* Model is downloaded on first use


### Install

```
pip install https://github.com/dermatologist/cui-embed/releases/download/1.0.0/cui_embed-1.0.0-py3-none-any.whl
```
### Use

```
from cui_embed import Cuimodel
cm = Cuimodel()
m = cm.model()
print(m.most_similar_cosmul(['C0002268'])
    
```

# cui-embed

This is a gensim wrapper for the clinical (CUI) embeddings for the model [here](https://github.com/beamandrew/cui2vec)

* This does not include data/model.
* Model is downloaded on first use

## Usage example

```
from cui_embed import Cuimodel
cm = Cuimodel()
m = cm.model()
print(m.most_similar_cosmul(['C0002268'])
    
```
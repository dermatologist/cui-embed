# cui-embed

This is a gensim wrapper for the Concept Unique Identifier (CUI) embeddings from the model presented [here](https://github.com/beamandrew/cui2vec). The paper describing the model creation is [here](https://arxiv.org/abs/1804.01486). This can be used with [pyomop](https://github.com/dermatologist/pyomop) for efficient electronic phenotyping from [OHDSI](https://www.ohdsi.org/) CDM databases. 

You can use [cui-cdm](https://github.com/E-Health/cui-cdm) for mapping CUI to OHDSI OMOP concepts and [umlsjs](https://github.com/dermatologist/umlsjs) for accessing UMLS REST APIs for CUI and other terminology management.

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
print(m.most_similar_cosmul(['C0002268']))
    
```

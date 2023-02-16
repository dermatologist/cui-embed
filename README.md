# cui-embed

## Update 2/16/2023
* Added support for LOINC embedding from [this repo](https://github.com/elleros/DSHealth2019_loinc_embeddings). Please cite [the paper](https://arxiv.org/abs/1907.09600) in the above repo if you use LOINC embedding.

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
# CUI embedding
from cui_embed import Cuimodel
cm = Cuimodel('cui')
m = cm.model()
print(m.most_similar_cosmul(['C0002268']))

# LOINC embedding
lm = Cuimodel('loinc')
lm = cm.model()
print(lm.most_similar_cosmul(['2324-2']))

```

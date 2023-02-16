import pytest

def test_cui_model():
    from cui_embed import Cuimodel
    cm = Cuimodel('cui')
    m = cm.model()
    # 'C0002268'
    assert len(m.most_similar_cosmul(['C0002268'])) > 0


def test_loinc_model():
    from cui_embed import Cuimodel
    cm = Cuimodel('loinc')
    m = cm.model()
    # LOINC Code 2324-2 Gamma glutamyl transferase
    assert len(m.most_similar_cosmul(['2324-2'])) > 0
    print(m.most_similar_cosmul(['2324-2']))

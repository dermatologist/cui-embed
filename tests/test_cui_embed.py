import pytest

def test_cui_model():
    from cui_embed import Cuimodel
    cm = Cuimodel()
    m = cm.model()
    # 'C0002268'
    assert len(m.most_similar_cosmul(['C0002268'])) > 0


def test_loinc_model():
    from cui_embed import Cuimodel
    cm = Cuimodel('loinc')
    m = cm.model()
    # '38483-4'
    assert len(m.most_similar_cosmul(['38483-4'])) > 0

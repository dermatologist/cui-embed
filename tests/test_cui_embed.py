import pytest

def test_model():
    from cui_embed import Cuimodel
    cm = Cuimodel()
    m = cm.model()
    # 'C0002268'
    assert len(m.most_similar_cosmul(['C0002268'])) > 0

import pytest
from bda_tools import generators


def test_caching_generator_basic():
    g = (x for x in range(10))
    cg = generators.Caching_Generator(g)
    assert cg.cache == []
    for item in cg:
        assert isinstance(item, int)
    print(cg.cache)
    assert cg.cache == [x for x in range(10)]
    for item, thing in zip(cg, [x for x in range(10)]):
        assert item == thing


def test_caching_generator_take():
    g = (x for x in range(10))
    cg = generators.Caching_Generator(g)
    assert cg.cache == []
    assert cg() == 0
    assert cg.cache == [0]
    assert cg() == 1
    assert cg.cache == [0,1]


def test_caching_generator_index():
    g = (x for x in range(10))
    cg = generators.Caching_Generator(g)
    for _ in cg:
        pass
    assert cg[2] == 2
    assert cg[5] == 5
    with pytest.raises(IndexError):
        assert cg[11]

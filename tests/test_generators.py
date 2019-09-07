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

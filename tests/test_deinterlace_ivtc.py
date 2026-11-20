import pytest
from media import deinterlace_ivtc as mod

CASES = [
    ("field", 'm.field_order(2, 1) == "top"'),
    ("comb", 'm.comb_score([1, 3, 2]) == 3'),
    ("motion", 'm.motion_threshold(0.2, 2) == approx(0.4)'),
    ("cadence", 'm.cadence_index(7, 5) == 2'),
    ("static", 'm.static_protect(3, [1, 3]) is True'),
    ("timestamp", 'm.timestamp_map(5, 24, 1) == approx(5 / 24)'),
    ("depth", 'm.bit_depth(0.5, 10) == approx(511.5)'),
    ("reset", 'm.reset_on_cut(True, [1, 2]) is True'),
    ("pair", 'm.field_pair(3, 1) == (6, 7)'),
    ("gpu", 'm.gpu_cpu_match("top", "top") is True'),
    ("order", 'm.denoise_order("di", "dn") == ("di", "dn")'),
    ("drop", 'm.drop_field(1, 0) is True'),
    ("duration", 'm.field_duration(50) == approx(0.01)'),
    ("blend", 'm.blend_fields(2, 4, 0.5) == approx(3.0)'),
    ("cut", 'm.scene_cut_score(0.5, 0.3) is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})

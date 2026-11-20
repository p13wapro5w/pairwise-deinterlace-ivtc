import math

def field_order(first, second):
    """场序判定。"""
    raise NotImplementedError("TODO: field_order")

def comb_score(lines):
    """梳齿评分。"""
    raise NotImplementedError("TODO: comb_score")

def motion_threshold(luma, base):
    """动检阈值。"""
    raise NotImplementedError("TODO: motion_threshold")

def cadence_index(frame, pattern):
    """cadence 相位。"""
    raise NotImplementedError("TODO: cadence_index")

def static_protect(layer, static_layers):
    """静态保护。"""
    raise NotImplementedError("TODO: static_protect")

def timestamp_map(frame, fps_num, fps_den):
    """素材时基。"""
    raise NotImplementedError("TODO: timestamp_map")

def bit_depth(value, bits):
    """位深映射。"""
    raise NotImplementedError("TODO: bit_depth")

def reset_on_cut(cut, history):
    """切镜重置。"""
    raise NotImplementedError("TODO: reset_on_cut")

def field_pair(frame, order):
    """场配对。"""
    raise NotImplementedError("TODO: field_pair")

def gpu_cpu_match(gpu_order, cpu_order):
    """预览导出一致。"""
    raise NotImplementedError("TODO: gpu_cpu_match")

def denoise_order(deinterlace, denoise):
    """降噪顺序。"""
    raise NotImplementedError("TODO: denoise_order")

def drop_field(field_index, quality):
    """降级丢场。"""
    raise NotImplementedError("TODO: drop_field")

def field_duration(fps):
    """场时长。"""
    raise NotImplementedError("TODO: field_duration")

def blend_fields(top, bottom, alpha):
    """场混合。"""
    raise NotImplementedError("TODO: blend_fields")

def scene_cut_score(delta, threshold):
    """场景切换。"""
    raise NotImplementedError("TODO: scene_cut_score")

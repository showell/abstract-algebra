def enhanced_type(obj):
    return getattr(obj, "enhanced_type", None) or type(obj)

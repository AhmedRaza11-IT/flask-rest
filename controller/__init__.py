import os,glob
__all__ = [
    os.path.basename(f)[:-3]
    for f in glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
    if os.path.isfile(f) and not f.endswith('__init__.py')
]

# __all__=["user_cont","product_cont"]

import scrapbook
import scrapbook.encoders

# NOTE this is supposed to be in the upstream
def load(encoder):
    return scrapbook.encoders.registry.register(encoder)

__all__ = [
    load
]

"""Shared material lookups for the item icon renderers (Blender side, needs bpy nodes only).

base_image(mat) returns the image that actually feeds the Principled BSDF "Base Color" input.
Eurobound-o2yv: the old lookup took the first image texture node in the list, which silently
renders a normal map or roughness map as the colour when a GLB lists that node first.
"""


def _principled(mat):
    for n in mat.node_tree.nodes:
        if n.type == "BSDF_PRINCIPLED":
            return n
    return None


def _image_upstream(sock):
    """Breadth-first walk from an input socket back through any intermediate nodes (mix, colour
    correction, hue/sat, ...) to the nearest Image Texture node that has an image."""
    seen, queue = set(), [sock]
    while queue:
        s = queue.pop(0)
        for link in s.links:
            node = link.from_node
            if node.name in seen:
                continue
            seen.add(node.name)
            if node.type == "TEX_IMAGE" and node.image:
                return node.image
            queue.extend(node.inputs)
    return None


def base_image(mat):
    if not (mat and mat.use_nodes):
        return None
    bsdf = _principled(mat)
    if bsdf is not None:
        img = _image_upstream(bsdf.inputs["Base Color"])
        if img is not None:
            return img
    for n in mat.node_tree.nodes:           # nothing linked into Base Color: the old behaviour
        if n.type == "TEX_IMAGE" and n.image:
            print("WARNING base_image: material %r has no image linked to Base Color; "
                  "falling back to the first image node %r" % (mat.name, n.image.name))
            return n.image
    return None

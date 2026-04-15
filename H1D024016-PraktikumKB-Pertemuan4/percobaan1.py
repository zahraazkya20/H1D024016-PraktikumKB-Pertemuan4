# PERCOBAAN 1

# FAKTA: parent(OrangTua, Anak)
data_parent = [
    ("alya", "bima"),
    ("alya", "satria"),
    ("bima", "david"),
    ("bima", "emma"),
    ("satria", "yunita"),
    ("satria", "grace")
]

# ATURAN: Sibling (Saudara Kandung)
# X dan Y adalah saudara jika memiliki orang tua (Z) yang sama dan X != Y [cite: 124, 127]
def get_siblings(target):
    parents = [p for p, c in data_parent if c == target]
    siblings = set()
    for p in parents:
        children = [c for parent, c in data_parent if parent == p and c != target]
        siblings.update(children)
    return list(siblings)

# ATURAN: Grandparent (Kakek/Nenek)
# X adalah kakek/nenek Y jika X orang tua Z, dan Z orang tua Y [cite: 135, 137]
def get_grandparents(target_cucu):
    results = []
    # Cari orang tua dari si cucu
    parents = [p for p, c in data_parent if c == target_cucu]
    for p in parents:
        # Cari orang tua dari si orang tua (Kakek/Nenek)
        grandparents = [gp for gp, child in data_parent if child == p]
        results.extend(grandparents)
    return results

# ATURAN: Ancestor (Leluhur) - rekursif
# X adalah leluhur Y jika X orang tua Y, atau X orang tua Z dan Z leluhur Y
def get_ancestors(target, visited=None):
    if visited is None:
        visited = set()
    results = []
    parents = [p for p, c in data_parent if c == target]
    for p in parents:
        if p not in visited:
            visited.add(p)
            results.append(p)
            results.extend(get_ancestors(p, visited))
    return results

# ATURAN: Children (Anak)
# Siapa saja anak dari target
def get_children(target):
    return [c for p, c in data_parent if p == target]

# Uji Coba Query
print(f"Saudara Bima: {get_siblings('bima')}")         # Output: ['satria']
print(f"Kakek/Nenek Emma: {get_grandparents('emma')}") # Output: ['alya']
print(f"Anak Alya: {get_children('alya')}")            # Output: ['bima', 'satria']
print(f"Leluhur Grace: {get_ancestors('grace')}")      # Output: ['satria', 'alya']
print(f"Apakah Bima dan Satria saudara? {'satria' in get_siblings('bima')}")  # Output: True
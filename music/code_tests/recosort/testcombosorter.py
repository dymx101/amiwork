from recommendationsorters.combosorter import ComboSorter

cs = ComboSorter()
cs.set_relevant_fields(["a","b","c"])
print cs._list_field_combos()
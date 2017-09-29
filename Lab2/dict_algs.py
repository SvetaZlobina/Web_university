ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12
    }, {
        "name": "petja",
        "age": 10
    }],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21
    }, {
        "name": "pavel",
        "age": 21
    }],
}

emps = [ivan, darja]


def find_children(emps_in):
    for elem in emps_in:
        children_arr = elem.get("children")
        for child in children_arr:
            if child.get("age") > 18:
                print(elem.get("name"))
                break

find_children(emps)

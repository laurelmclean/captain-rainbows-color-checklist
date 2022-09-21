# As a user, I want to be able to create, read, update, and destroy items in a checklist.

# As a user, I want to be able to mark off colors so I can know that it's already represented.

# As a user, I want to be able to see everything in my list at once so I know what is in my list.

checklist = list()
# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    item = checklist[index]
    return item

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    

test()

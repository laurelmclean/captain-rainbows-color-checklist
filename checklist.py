# As a user, I want to be able to create, read, update, and destroy items in a checklist.

# As a user, I want to be able to mark off colors so I can know that it's already represented.

# As a user, I want to be able to see everything in my list at once so I know what is in my list.

checklist = []
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)

def create(item):
    checklist.append(item)
#from collections import deque

def loop_size(node):
    #passed = deque()
    passed = {}
    i = 0
    '''
    while node not in passed:
        #if node is None:
        #    return 0
        #elif node not in passed:
        #passed.append(node)
        passed[node]=i
        node = node.next
        i += 1

    length = 0
    for past_node in passed:
        if past_node is node:
            return len(passed)-length
        else:
            length += 1
    '''
    #return len(passed) - passed.index(node)

    while node not in passed:
        passed[node]=i
        node = node.next
        i += 1

    return i - passed[node]


# ----------------------------- smart one ------------------------------

def loop_size(node):
    turtle, rabbit = node.next, node.next.next
    
    # Find a point in the loop.  Any point will do!
    # Since the rabbit moves faster than the turtle
    # and the kata guarantees a loop, the rabbit will
    # eventually catch up with the turtle.
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next
  
    # The turtle and rabbit are now on the same node,
    # but we know that node is in a loop.  So now we
    # keep the turtle motionless and move the rabbit
    # until it finds the turtle again, counting the
    # nodes the rabbit visits in the mean time.
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    # voila
    return count
answer yarn

// Swapping in singly
Linked
List

void
swappingNodes(Node * head, Node
x, Node * y)
{
// if both
nodes
are
same
if (x == y)
return;

// Search
for y(keep track of previous of node y and Current node y )
Node * prevY = NULL, *currentY = *head;
while (currentY & & currentY != y)
    {
        prevY = currentY;
    currentY = currentY->next;
    }

    // Search
    for x(keep track of previous of node x and Current node x )
    Node * prevX = NULL, *currentX = *head;
    while (currentX & & currentX != x)
        {
            prevX = currentX;
        currentX = currentX->next;
        }

        // If
        either
        x or y is not present in the
        list
        if (currentX == NULL | | currentY == NULL)
            return;

        // If
        x is not head
        of
        linked
        list
        if (prevX != NULL) prevX->next = currentY;
        else // Else make y as new head
        *head = currentY;

        // If
        y is not head
        of
        linked
        list
        if (prevY != NULL)
            prevY->next = currentX;
        else // Else make x as new head
        *head = currentX;

        // Swap
        next
        pointers
        Node * temp = currentY->next;
        currentY->next = currentX->next;
        currentX->next = temp;
        }

        // swapping
        nodes in doubly
        linked
        list

        void
        swapingNodes(struct
        Node * x, struct
        Node * y){
        if (x->prev != NULL){
        x->prev->next = y;
        }
        else {
        head = y;
        }

        if (y->next != NULL){
        y->next->prev = x;
        }

        x->next = y->next;
        y->prev = x->prev;
        y->next = x;
        x->prev = y;
        }

        swapping
        node in singly
        linked
        list
        takes
        more
        time.
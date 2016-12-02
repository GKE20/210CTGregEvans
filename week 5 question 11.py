def remove_node(self,value): #Removing value from the list
    n = self.head
    while int(n.value)!=value: #finding value by traversing the list
        n = n.next
        if n.next== None:
                print('The value is does not exist') #Value is non existent in the list
                break
    if n.prev !=None:
            n.prev.next = n.next #Confirming that after the deleted node the 
    else:                        #pointers will point to the next element
            l.head = n.next
    if n.next !=None:
            n.next.prev = n.prev
    else:
            l.trail = n.prev
            

            

def delete_node_at_pos(self, pos):
    if self.head:
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return




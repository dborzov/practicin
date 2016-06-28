# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        if root is None:
            return '[]'
        output = []
        cur = [root]
        while len(cur)!=0:
            for each in cur:
                output.append(str(each.val) if not each is None else 'null')
            new_cur = []
            for each in cur:
               if each is None:
                    continue
               new_cur.append(each.left)
               new_cur.append(each.right)
            cur = new_cur
        return "[" + ",".join(output) + "]"


    def deserialize(self, data):
        if data=='[]':
            return None
        output = data.rstrip("]")[1:].split(",")
        def getter(idx):
            if idx < len(output):
                return output[idx]
            return 'null'
        root = TreeNode(output[0])
        cur = [root]
        pos = 0
        while pos < len(output):
            if len(cur)==0:
                break
            new_cur = []
            for each in cur:
                pos += 1
                if getter(pos) !='null':
                    left_node = TreeNode(int(output[pos]))
                    each.left = left_node
                    new_cur.append(left_node)
                pos += 1
                if getter(pos) !='null':
                    right_node = TreeNode(int(output[pos]))
                    each.right = right_node
                    new_cur.append(right_node)
            cur = new_cur
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

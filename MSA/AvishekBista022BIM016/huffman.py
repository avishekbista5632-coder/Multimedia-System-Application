import heapq
from collections import Counter

class Node:
   def __init__(self, char, freq):
       self.char = char
       self.freq = freq
       self.left = None
       self.right = None

   def __lt__(self, other):
       return self.freq < other.freq

def build_huffman_tree(text):
   frequency = Counter(text)
   heap = [Node(char, freq) for char, freq in frequency.items()]
   heapq.heapify(heap)

   while len(heap) > 1:
       left = heapq.heappop(heap)
       right = heapq.heappop(heap)

       merged = Node(None, left.freq + right.freq)
       merged.left = left
       merged.right = right

       heapq.heappush(heap, merged)

   return heap[0]

def generate_codes(node, prefix="", codebook={}):
   if node:
       if node.char:
           codebook[node.char] = prefix
       generate_codes(node.left, prefix + "0", codebook)
       generate_codes(node.right, prefix + "1", codebook)
   return codebook
text = "huffman"
tree = build_huffman_tree(text)
codes = generate_codes(tree)

print("Huffman Codes:", codes)
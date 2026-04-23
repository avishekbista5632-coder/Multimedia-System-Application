def rle_encode(data):
   encoding = ""
   i = 0

   while i < len(data):
       count = 1
       while i + 1 < len(data) and data[i] == data[i + 1]:
           i += 1
           count += 1
       encoding += data[i] + str(count)
       i += 1

   return encoding
data = "AAAABBBCCDAA"
print("Encoded:", rle_encode(data))

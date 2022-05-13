# linked list
import pprint
import hashlib
import json


class Block:
    id = None
    history = None
    paren_id = None
    parent_hash = None


block_A = Block()
block_A.id = 1
block_A.history = 'Nelson likes cat'

block_B = Block()
block_B.id = 2
block_B.history = 'Marie likes dog'
block_B.parent_id = block_A.id
block_B.parent_hash = hashlib.sha256(json.dumps(block_A.__dict__).encode('utf-8')).hexdigest()

block_C = Block()
block_C.id = 3
block_C.history = 'Sky hates dog'
block_C.parent_id = block_B.id
block_C.parent_hash = hashlib.sha256(json.dumps(block_B.__dict__).encode('utf-8')).hexdigest()

print('\n1) Block details:')
pprint.pprint(block_B.__dict__)

print('\n2) Block details + json.dumps:')
pprint.pprint(json.dumps(block_B.__dict__))

print('\n3) Block details + json.dumps and UTF-8 encoded:')
pprint.pprint(json.dumps(block_B.__dict__).encode('utf-8'))

print('\n4) Block details + json.dumps and UTF-8 encoded + hashlib:')
pprint.pprint(hashlib.sha256(json.dumps(block_B.__dict__).encode('utf-8')))

print('\n5) Block details + json.dumps and UTF-8 encoded + hashlib + hexdigest:')
pprint.pprint(hashlib.sha256(json.dumps(block_B.__dict__).encode('utf-8')).hexdigest())

# altering block
block_A.history = 'Nelson hates cat'

print('\nBlock C after altering block A:')
altered = block_C.parent_hash
print(altered)

block_B.parent_hash = hashlib.sha256(json.dumps(block_A.__dict__).encode('utf-8')).hexdigest()
block_C.parent_hash = hashlib.sha256(json.dumps(block_B.__dict__).encode('utf-8')).hexdigest()

print('\nBlock C prior alteration of block A:')
original = block_C.parent_hash
print(original)

# TEST
if altered == original:
    print('\nBlocks are identical')
else:
    print("\nBlock hashes don't match.")

# Proof of work



# Adding block D
print('\nAdding new block:')
block_D = Block()
block_D.id = 4
block_D.history = 'Sky loves turtle'
block_D.parent_id = block_C.id

block_serialized = json.dumps(block_D.__dict__).encode('utf-8')
print('Hash input:', block_serialized)

payload = block_serialized
for i in range(10000000):
    nonce = str(i).encode('utf-8')
    result = hashlib.sha256(payload + nonce).hexdigest()
    if result[0:5] == '00000':
        # reward[miner_id] += 1
        print('Answer:', i)
        print('Hash output:', result)
        break


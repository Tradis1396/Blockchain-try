from flask import Flask, request
import json

import hashlib as hash
import datetime as date


app = Flask(__name__)


@app.route('/')
def index():
    return "Flask server"


global data_recieved


@app.route('/postData', methods=['POST'])
def postdata():
    # data_recieved = request.get_json()
    data_recieved = "new data"
    # print(data_recieved, "data recieved")
    print(data_recieved)

    # do something with this data variable that contains the data from the node server
    return json.dumps({"newdata": "data sent"})


if __name__ == "__main__":
    app.run(port=5000)

# print(data_recieved)


# class Block:

#     def __init__(self, index, timeStamp, data_recieved, previousHash=0):
#         self.index = index
#         self.timeStamp = timeStamp
#         self.data = data_recieved
#         self.previousHash = previousHash
#         self.currentHash = self.hashing()

#     def hashing(self):
#         SHA = hash.sha256()
#         SHA.update((str(self.index) + str(self.timeStamp) +
#                     str(self.data) + str(self.previousHash)).encode('utf-8'))
#         return SHA.hexdigest()

# def outsidevar(self):
#     self.variable = data_recieved

# for i in range(len(self.data)):
#     self.data[i]
#     block_declined = Block(i, date.datetime.now(), self.data[i])


# if(data_recieved != None):
# def block_next(old_block):
#     new_index = old_block.index + 1
#     new_timeStamp = date.datetime.now()
#     new_data = "data"
#     new_hash = old_block.currentHash
#     return Block(new_index, new_timeStamp, new_data, new_hash)


# print(Block(0, date.datetime.now(), "gene", 0))

# print(Block.mapping())
# block = Block.block_declined
# print(block)
# blockArray = [block]
# last_block = blockArray[0]
# Block.block_next(last_block)
# blockArray.append(Block.block_next(last_block))
# print(blockArray[0].currentHash)
# print(blockArray[1].previousHash)

# print(Block.block_next(last_block))
# print(len(blockArray))

# def mapfun(Array):
#     for x in range(len(Array)-1):
#         Array[x+1].previousHash = Array[x].currentHash
#         print(Array[x+1].previousHash)
#         print(Array[x+1].currentHash)

# mapfun(blockArray)

# def mapping():
#     result = map(mapfun(blockArray), blockArray)
# mapping()

# print(data, "data,data")

import SHA256 from "crypto-js/sha256";

class Block {
  index: string;
  timestamp: string;
  data: any;
  previousHash: any;
  hash: any;
  constructor(index, timestamp, data, previousHash = "") {
    this.index = index;
    this.timestamp = timestamp;
    this.data = data;
    this.previousHash = previousHash;
    this.hash = this.calculateHash();
  }

  calculateHash() {
    return SHA256(
      this.index,
      this.timestamp,
      JSON.stringify(this.data),
      this.previousHash
    ).toString();
  }

  block = new Block(0, "21/2/12", "newdata", "0");
}
console.log(this.block);

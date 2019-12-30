"use strict";
exports.__esModule = true;
var crypto_js_1 = require("crypto-js");
var Block = /** @class */ (function () {
    function Block(index, timestamp, data, previousHash) {
        if (previousHash === void 0) { previousHash = ""; }
        this.block = new Block(0, "21/2/12", "newdata", "0");
        this.index = index;
        this.timestamp = timestamp;
        this.data = data;
        this.previousHash = previousHash;
        this.hash = this.calculateHash;
    }
    Block.prototype.calculateHash = function () {
        return crypto_js_1["default"](this.index, this.timestamp, JSON.stringify(this.data), this.previousHash).toString();
    };
    return Block;
}());
console.log(this.block);

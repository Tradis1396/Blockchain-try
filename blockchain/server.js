const express = require("express");
const app = express();
const cors = require("cors");

app.use(cors());
app.use(bodyParser.json());
/////////////////////////python blockchain server/////////////////////////

app.get("/postdatatoFlask", async function(req, res) {
    var options = {
      method: "POST",
      uri: "http://localhost:5000/postData",
      body: shuffledArray,
      json: true // Automatically stringifies the body to JSON
    };
    console.log(req.body);
    var returndata;
    var sendrequest = await request(options)
      .then(function(parsedBody) {
        console.log(parsedBody); // parsedBody contains the data sent back from the Flask server
        returndata = parsedBody; // do something with this data, here I'm assigning it to a variable.
      })
      .catch(function(err) {
        console.log(err);
      });
  
    res.send(returndata);
  });
  
  app.listen(3000);
  
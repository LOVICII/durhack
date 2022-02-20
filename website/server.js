const express = require('express')
const app = express()
const path = require('path')
const url = "http://127.0.0.1:8080/"
const dataset = require("./dataset.json")
app.use(express.json())
app.use(express.static('./'))

app.get("/", function(req, res){

})

app.get("/imgfile", function(req, res){
    console.log("get imgfile")
    id = req.query.id;
    filename = dataset[id]["filename"];
    const options = {
        root: path.join(__dirname, "imgs", "original")
    };
    console.log(filename, options)
    res.sendFile(filename, options, function (err) {
        if (err) {
          console.log(err);
        } else {
          console.log('Sent');
        }
    })
})

app.get("/imgfilecolour", function(req, res){
    console.log("get imgfile")
    id = req.query.id;
    filename = dataset[id]["filename"];
    const options = {
        root: path.join(__dirname, "imgs", "coloured")
    };
    console.log(filename, options)
    res.sendFile(filename, options, function (err) {
        if (err) {
          console.log(err);
        } else {
          console.log('Sent');
        }
    })
})

app.get("/imginfo", function(req, res){
    console.log("get info")
    // console.log(req.query)
    id = req.query.id;
    info = dataset[id]["info"];
    res.json(info);
})

app.listen(8080)
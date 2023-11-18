var fs = require('fs');
var mqtt = require('mqtt')
//var client  = mqtt.connect('mqtt://test.mosquitto.org')
var client  = mqtt.connect('mqtt://test.mosquitto.org')
//var client  = mqtt.connect('mqtt://demo.thingsboard.io',{'username':'gLNt6D4GDSzrjC9c5r3Y'})

client.on('connect', function () {
    client.subscribe("babusha")
})

client.on('message', function (topic, message) {
    // message is Buffer
    fs.writeFile('tempu.txt', message, function(err, data){
        if (err) console.log(err);
        console.log("Successfully Written to File.");
    });
    console.log(message.toString())
    client.end()
  })

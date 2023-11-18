var mqtt = require('mqtt')
var client  = mqtt.connect('mqtt://test.mosquitto.org')
var fs = require('fs');

client.on('connect', function () {

fs.readFile('testfile.txt', 'utf-8' ,function(err, buf) {
	var x=buf.toString()
	client.publish("babusha",x)
	console.log(x);
});

	console.log("published");

})


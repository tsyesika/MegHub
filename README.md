#Intro 

MegHub is designed to be a very flexiable notification system which takes in many inputs and displays to many output.
This tool handles the status of notifications, if a output (client) allows for achnologement it will be sent to the server
and the server will mark the item as achnologed and identify your other devices.

I wrote this because I have found all of the notification systems are spread all over the place and it's difficult to be able to get
a unified system across all devices I might want. 

#Inputs

An input simply is a small amount of code which checks for some form of notification e.g.

- Facebook message/status/event
- Twitter/Identica tweet/dent or private message.
- Youtube video being uploaded.
- Server going down
- New email (maybe with specific filters applied?)
- RSS update
etc...

#Outputs

These are very basic ways of displaying notifications, some can be dedicated programs or just regular existing methods e.g.

- SMS gateway
- Email
- Curses CLI program
- Website of some description
- Tweet?
etc...

#Config
To configure this you need to modify the configuration file, inputs usually take some kind of input themselves be it facebook credentials, servers to check, etc... then you need to specify some information if they're active, how often to run them (in seconds).

e.g. 

    input_filters = { 
        "server-status":{
	    	"active":True,
			"inputs":[
				"gilman.megworld.co.uk", "silvernitrate.megworld.co.uk",
				"schiff.megworld.co.uk","bariumchloride.megworld.co.uk",
				"ninhydrin.megworld.co.uk"
			],
		"frequency":5,
		"type":"monitor"
	    }   
    }



That will specify a input filter which takes in an input of server status (up or down). This works by the ping command. The active says it will be run (if you set this to false it will not be run). The inputs are the servers you wish to monitor (in this case a group of MegNet nodes). The frequency is how often it will be run, in this case it's every 5 seconds. 

Type is a strange one, it's there basically so the server is better at handling the achnologements. The choices currently are:

- Monitor: this is for inputs which once achnologed you don't want them to notify you again until the input has been run and not produced a notification. (i.e. in this above case you won't be notified the server is down after you've achnologed the notification until the server has come back up).
- Manual: this is when you manually have to inform the server to send you notifications again
- Event: this is quite common, this would be things like a new youtube video has been uploaded by <x>, a new email has come in which matches <x> crteria, <x>'s birthday. (different events).
- Time: This will just ignore notifications for a specific amount of time (this is given using "ignore-time" on the filter in the config).

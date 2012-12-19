# Bind to address
bind_address = "127.0.0.1"

# Port to bind to
bind_port = 7272

# Filters
input_filters = {
	"server-status":{
		"active":True,
		"inputs":["gilman.megworld.co.uk", "silvernitrate.megworld.co.uk", "schiff.megworld.co.uk",
			"bariumchloride.megworld.co.uk", "ninhydrin.megworld.co.uk"],
		"frequency":5, # in seconds
		"type":"monitor"
	}
}

output_filters = {}

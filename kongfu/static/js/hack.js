var plam = [], fingers = []
var gestureType, gesturePosition = None
var empty = false

function getLeapData() {
	url = '/kongfu/getLeapData/'
	data = new Object()
	gesturePosition = None
	$.ajax({
		type : 'post',
		dataType : 'json',
		url : url,
		async : true,
		data :  data,

		success : function(response){
			b = response
			if(b.hand == undefined) {
				empty = true

			}
			else if(b.gesture.length == 0) { // not Leap Motion
				Leap(b)
				empty = false
			}
			else {
				Leap(b)
				empty = false
				gesturePosition = 0
				gestureType = b.gesture[0].type

				for(var i = 0; i < fingerIds.length; ++i) {
					if(fingerIds[i] == b.gesture[0].pointableId) {
						gesturePosition = i
						break
					}
				}
			//	after()
				console.log("sssss", plam[1])
			}
		},

		error : function(response){
			console.log("Oops, Penta !")
		}
	})
}


function Leap(data) {
	plam = data.hand[0].palmPosition

	fingerIds = []
	fingerData = data.hand[0].finger
	fingers = []
	for(var i = 0; i < fingerData.length; ++i) {		
		fingers.push(fingerData[i].tipPostion)
		fingerIds.push(parseInt(fingerData[i].fingerId))
	}
} 


/*$(function() {
	setInterval(getLeapData, 100)
})*/

var plam = [], fingers = []
var gestureType, gesturePosition
var empty = false

function getLeapData() {
	url = '/kongfu/getLeapData/'
	data = new Object()
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
				gestureType = data.gesture[0].type
				for(var i = 0; i < fingerIds.length; ++i) {
					if(fingerIds[i] == data.gesture[0].pointableId) {
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
	plamDatas = data.hand[0].palm_position.toString()
	plamData = plamDatas.substring(1, plamDatas.length - 1).split(',')
	palm = []
	for(var i = 0; i < 3; ++i) {
		plam.push(parseFloat(plamData[i]))
	}

	fingerIds = []
	fingerData = data.hand[0].finger
	fingers = []
	for(var i = 0; i < fingerData.length; ++i) {
		res = []
		for(var i = 0; i < 3; ++i) {
			tmp = fingerData[i].toString()
			res.push(parseFloat(tmp.substring(1, tmp.length - 1).split(',')))
		}
		fingers.push(res)
		fingerIds.push(parseInt(fingerData[i].fingerId))
	}
} 

$(function() {
	setInterval(getLeapData, 100)
})

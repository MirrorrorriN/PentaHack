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
			$('leapData').html(b.hand)
		},

		error : function(response){
			console.log("Oops, Penta !")
		}
	})
}
 
$(function() {
	setInterval(getLeapData, 200);
})
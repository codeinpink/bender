
<script>
$('#save').click(saveFile);

function saveFile()
{
	$.ajax({
	url: '/saveFile',
	type: 'POST',
	contentType: "application/json",
	data: JSON.stringify(constructJsonRequest()),
	success: function(value)
	{
		alert("Success");
	},
	error: "submitting package creation request email."
	});
	
}

function constructJsonRequest()
{
	var jsObject =
	{
    	code: $("#code").val(),
    	filename: $("#filename").val(),

    };

    return jsObject;
	
}


</script>
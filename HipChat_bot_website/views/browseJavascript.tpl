<script>
function loadFiles(filenames)
{

	for(current in filenames)
	{
			var panel = '<div class="panel panel-default"><div class="panel-heading">' +
									'<h3 class="panel-title">' + filenames[current]['filename'] + '</h3></div><div class="panel panel-body">' +
									filenames[current]['code'] + '</div></div>';
			$('#plugins').append('<div class="col-sm-4">' + panel + '</div>');
	}

}


</script>

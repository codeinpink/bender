<script>
function loadFiles(filenames)
{
	
	for(current in filenames)
	{
		$("#test").append('<tr><td>'+filenames[current]['filename']
			+'</td>'+'<td>'+filenames[current]['code']+'</td></tr>');

	}
	
}


</script>
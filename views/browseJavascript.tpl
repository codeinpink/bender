<script>
function loadFiles(filenames) {
	for(current in filenames) {
		var code = '';
		filenames[current]['code'].forEach(function(line) {
			code = code + '<code>' + line + '</code><br>';
		});

		var panel = '<div class="panel panel-default"><div class="panel-heading">' +
								'<h3 class="panel-title">' + filenames[current]['filename'] + '</h3></div><div class="panel panel-body">' +
								'<code>' + code + '</code></div></div>';
		$('#plugins').append('<div class="col-sm-6">' + panel + '</div>');
	}
}
</script>

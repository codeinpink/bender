% include("head.tpl", title="Browse")
</head>

<body onload= "loadFiles({{filename}});">
	% include("nav.tpl")
	<div class="container">
	  <div class="row">
			<table class="table table-hover" id="test">
			<tr>
				<th>File Name</th>
				<th>Code</th>
			</tr>
			</table>

			% include("browseJavascript.tpl")
			% include("footer.tpl")
		</div>
	</div>
</body>
</html>

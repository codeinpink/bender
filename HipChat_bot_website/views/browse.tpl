% include("head.tpl", title="Browse")
</head>

<body onload= "loadFiles({{filename}});">
	% include("nav.tpl")
	<div class="container">
	  <div class="row" id="plugins">
			% include("browseJavascript.tpl")
			% include("footer.tpl")
		</div>
	</div>
</body>
</html>

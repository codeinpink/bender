% include("head.tpl", title="Browse")
</head>

<body onload= "loadFiles({{filename}});">
% include("nav.tpl")

<table class="table table-hover" id="test">
<tr>
	<th>File Name</th>
	<th>Code</th>
</tr>

</table>


% include("browseJavascript.tpl")
% include("footer.tpl")
</body>
</html>
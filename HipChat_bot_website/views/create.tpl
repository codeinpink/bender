% include("head.tpl", title="Create")
% include("create_css.tpl")
</head>
<body>
% include("nav.tpl")

<form>
  <div class="form-group">
    <label for="filename">File Name</label>
    <input type="filename" class="form-control" id="filename" placeholder="File Name">
  </div>
  <div class="form-group">
    <label for="code">Code</label>
    <textarea class="form-control" id="code" rows="3"></textarea>
  </div>
  <button type="submit" id="save" class="btn btn-default">Submit</button>
</form>

% include("createFormJavascript.tpl")
% include("footer.tpl")

</body>
</html>
% include("head.tpl", title="Create")
% include("create_css.tpl")
</head>
<body style="background: url(http://media2.giphy.com/media/7xkxbhryQO7hm/giphy.gif) repeat; color: white;">
  % include("nav.tpl")
  <div class="container">
    <div class="row">
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
    </div>
  </div>
</body>
</html>

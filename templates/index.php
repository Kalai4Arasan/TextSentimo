<html>  
	<head>
		<link href="https://fonts.googleapis.com/css2?family=Inconsolata:wght@700&display=swap" rel="stylesheet">
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
	</head>
   <body style="font-family: 'Inconsolata', monospace;">  
      <div style="margin-top:5%;"  class="row">
		<div class="col-sm-3 col-md-3">
		
		</div>
		<div class="col-sm-6 col-md-6">
			<div style="border-radius:40px 0 40px 0;" class="card text-center border-success">
			  <div style="border-radius:40px 0 0 0;" class="card-header bg-primary text-white">
				<h3 class="card-title">Text Sentiment Analysis</h3>
			  </div>
			  <div class="card-body">
				<form  action = "http://localhost:5000/predict" method = "POST">    
					<div class="form-group">
						<input  style="margin-left:32%;margin-right:32%;width:40%;" id="Text" class="form-control" placeholder="Enter Your Comment..." type ="text" name ="textData"> 
					  </div>
					<input class="btn btn-primary" type = "submit" value="Submit">
				 </form> 
				<h5 class="text-success">
				{% if session['output'] %}
					{{session['output']}}
				{% endif %}
				</h5>
			  </div>
			  <div class="card-footer text-muted">
				<h5>©TeamMaster</h5>
			  </div>
			</div>
		</div>
		<div class="col-sm-3 col-md-3">
		
		</div>
	  </div>
	  {% if session['output'] %}
		{{session.pop('output')}}
	  {% endif %}
   </body>
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>   
</html>  
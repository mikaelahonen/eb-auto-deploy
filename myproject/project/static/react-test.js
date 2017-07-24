var ReactTest = React.createClass({ 
	
	getInitialState: function(){
		return {
			value: this.props.color,
			time: this.props.time
		}
	},
	handleChange(event){
		this.setState({
			value: "Väri on " + event.target.value
		});
	},
	handleTime(event){
		$.ajax({
			url: '/gym/ajax/fetch-time/',
			dataType: 'json',
			cache: false,
			success: function(data) {
				console.log("Ajax Ok");
				console.log(data);
				this.setState({time: data.time});
			}.bind(this),
			error: function(xhr, status, err){
				console.error("Ajax error", status, err.toString());
			}.bind(this)
		});
	},
	render: function(){
		return (
			<div>
				<div className="col-sm-6">
					<div className="well">
						<h1>React test </h1>
						<p>Enter color.</p>
						<input type="text" onChange={this.handleChange} />
					</div>
				</div>
				<div className="col-sm-6">
					<pre>{this.state.value}</pre>
				</div>
				
				<legend></legend>
				
				<div className="col-sm-12">
					<p>Time: {this.state.time}</p>
					<div className="btn btn-success" onClick={this.handleTime}>Fetch time</div>
				</div>
				<br />
				<br />
				<br />
				<br />
			</div>
			
		);
	}
});


ReactDOM.render(
	React.createElement(ReactTest, window.props), 
	window.reactId
)
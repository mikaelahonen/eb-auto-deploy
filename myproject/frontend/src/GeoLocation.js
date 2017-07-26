import React, { Component } from 'react';

class GeoLocation extends Component {
	
	state = {
		lat: 0,
		lon: 0,
		acc: "-"
	}
	
	componentWillMount(){
		var geoSuccess = function(pos){
			console.log("Geolocation success");
			this.setState({
				lat: pos.coords.latitude,
				lon: pos.coords.longitude,
				acc: pos.coords.accuracy
			});
		}.bind(this);
		navigator.geolocation.getCurrentPosition(geoSuccess);
	}
	
	render(){
		var coord = 0;
		if (this.props.coord == "lat"){
			coord = this.state.lat;
		} else if (this.props.coord == "lon"){
			coord = this.state.lon;
		} else if (this.props.coord == "acc"){
			coord = this.state.acc + " km";
		}
		return <div>{coord}</div>
	}
}

export default GeoLocation;
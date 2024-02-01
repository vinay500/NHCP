// index chart data

function chartCircle() {
	// ______________Chart-circle
	if ($('.chart-circle').length) {
		$('.chart-circle').each(function() {
			let $this = $(this);
			$this.circleProgress({
				fill: {
					color:  myVarVal || "#38cab3",
				},
				size: $this.height(),
				startAngle: -Math.PI / 4 * 2,
				emptyFill: 'transparent',
				lineCap: 'round'
			});
		});
	}	
}

// Project Budget chart //
function statistics1() {
	setTimeout(()=>{
		var options1 = {
			series: [{
				name: 'Total Orders',
				data: [44, 42, 57, 86, 58, 55, 70, 43, 23, 54, 77, 34],
			},{
				name: 'Total Sales',
				data: [34, 22, 37, 56, 21, 35, 60, 34, 56, 78, 89,53],
			}],
			chart: {
				type: 'bar',
				height: 280
			},
			grid: {
				borderColor: '#f2f6f7',
			},
			colors: [ myVarVal || "#38cab3","#e4e7ed"],
			plotOptions: {
				bar: {
					colors: {
						ranges: [{
							from: -100,
							to: -46,
							color: '#ebeff5'
						}, {
							from: -45,
							to: 0,
							color: '#ebeff5'
			}]
			},
			columnWidth: '40%',
		}
	},
	dataLabels: {
		enabled: false,
	},
	stroke: {
		show: true,
		width: 4,
		colors: ['transparent']
	},
	legend: {
		show: true,
		position:'top',
	},
	yaxis: {
		title: {
			text: 'Growth',
			style: {
				color: '#adb5be',
				fontSize: '14px',
				fontFamily: 'poppins, sans-serif',
				fontWeight: 600,
				cssClass: 'apexcharts-yaxis-label',
			},
		},
		labels: {
			formatter: function (y) {
				return y.toFixed(0) + "";
			}
		}
	},
	xaxis: {
		type: 'month',
		categories: ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'sep', 'oct', 'nov', 'dec'],
		axisBorder: {
			show: true,
			color: 'rgba(119, 119, 142, 0.05)',
			offsetX: 0,
			offsetY: 0,
		},
		axisTicks: {
			show: true,
			borderType: 'solid',
			color: 'rgba(119, 119, 142, 0.05)',
			width: 6,
			offsetX: 0,
			offsetY: 0
		},
		labels: {
			rotate: -90
		}
	}
		};
		document.getElementById('statistics1').innerHTML = ''; 
		var chart1 = new ApexCharts(document.querySelector("#statistics1"), options1);
		chart1.render();
	}, 300);
}


//Visitors chart
function viewers() {
	setTimeout(()=>{
		var options2 = {
			series: [{
				name: 'Male',
				data: [51, 44, 55, 42, 58,50, 62],
			},{
				name: 'Female',
				data: [56, 58, 38, 50, 64,45, 55]
			}],
			chart: {
			height: 315,
			type: 'line',
			toolbar: {
				show: false,
				},
				background: 'none',
				fill:"#fff",
			},
			grid: {
			borderColor: '#f2f6f7',
			},
			colors: [ myVarVal || "#38cab3", "#e4e7ed"],
			background: 'transparent',
			dataLabels: {
			enabled: false
			},
			stroke: {
			curve: 'smooth',
			width:2
			},
			xaxis: {
			type: 'day',
			categories: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
			},
			dataLabels: {
			enabled: false,
			},
			legend: {
			show: true,
			position:'top',
			},
		xaxis: {
			show:false,
			axisBorder: {
						show: false,
						color: 'rgba(119, 119, 142, 0.05)',
						offsetX: 0,
						offsetY: 0,
					},
					axisTicks: {
						show: false,
						borderType: 'solid',
						color: 'rgba(119, 119, 142, 0.05)',
						width: 6,
						offsetX: 0,
						offsetY: 0
					},
			labels: {
				rotate: -90,
			}
		},
		yaxis: {
			show:false,
			axisBorder: {
				show: false,
			},
			axisTicks: {
				show: false,
			}
		},
			tooltip: {
			x: {
				format: 'dd/MM/yy HH:mm'
			},
			},
		};
		document.getElementById('Viewers').innerHTML = ''
		var chart2 = new ApexCharts(document.querySelector("#Viewers"), options2);
		chart2.render();
	}, 300);
}
// index chart data end


// index1 chart data
//Sales Activity
function statistics2() {
	setTimeout(() => {
		var options = {
			series: [{
				name: "Sales",
				data: [32, 15, 63, 51, 136, 62, 99, 42, 178, 76, 32, 180]
			}],
			chart: {
				height: 280,
				type: 'line',
				zoom: {
					enabled: false
				},
				dropShadow: {
					enabled: true,
					enabledOnSeries: undefined,
					top: 5,
					left: 0,
					blur: 3,
					color: '#000',
					opacity: 0.1
				},
			},
			dataLabels: {
				enabled: false
			},
			legend: {
				position: "top",
				horizontalAlign: "left",
				offsetX: -15,
				fontWeight: "bold",
			},
			stroke: {
				curve: 'smooth',
				width: '3'
			},
			grid: {
				borderColor: '#f2f6f7',
			},
			colors: [myVarVal || "#1fc5db"],
			yaxis: {
				title: {
					text: 'Growth',
					style: {
						color: '#adb5be',
						fontSize: '14px',
						fontFamily: 'poppins, sans-serif',
						fontWeight: 600,
						cssClass: 'apexcharts-yaxis-label',
					},
				},
				labels: {
					formatter: function (y) {
						return y.toFixed(0) + "";
					}
				}
			},
			xaxis: {
				type: 'number',
				categories: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
				axisBorder: {
					show: true,
					color: 'rgba(119, 119, 142, 0.05)',
					offsetX: 0,
					offsetY: 0,
				},
				axisTicks: {
					show: true,
					borderType: 'solid',
					color: 'rgba(119, 119, 142, 0.05)',
					width: 6,
					offsetX: 0,
					offsetY: 0
				},
				labels: {
					rotate: -90
				}
			}
		};
		document.getElementById('statistics2').innerHTML = ''
		var chart = new ApexCharts(document.querySelector("#statistics2"), options);
		chart.render();
	}, 300);
}


// Budget Chart
function budget() {
	setTimeout(() => {
		var options = {
			series: [{
				name: 'This Week',
				data: [44, 42, 57, 86, 58, 55, 70],
			}, {
				name: 'Last Week',
				data: [-34, -22, -37, -56, -21, -35, -60],
			}],
			chart: {
				stacked: true,
				type: 'bar',
				height: 250,
			},
			grid: {
				borderColor: '#f2f6f7',
			},
			colors: [myVarVal || "#38cab3", "#e4e7ed"],
			plotOptions: {
				bar: {
					endingShape: 'rounded',
					colors: {
						ranges: [{
							from: -100,
							to: -46,
							color: '#ebeff5'
						}, {
							from: -45,
							to: 0,
							color: '#ebeff5'
						}]
					},
					columnWidth: '25%',
				}
			},
			dataLabels: {
				enabled: false,
			},
			legend: {
				show: true,
				position: 'top',
			},
			yaxis: {
				title: {
					style: {
						color: '#adb5be',
						fontSize: '14px',
						fontFamily: 'poppins, sans-serif',
						fontWeight: 600,
						cssClass: 'apexcharts-yaxis-label',
					},
				},
				labels: {
					formatter: function (y) {
						return y.toFixed(0) + "";
					}
				}
			},
			xaxis: {
				type: 'day',
				categories: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'sat'],
				axisBorder: {
					show: true,
					color: 'rgba(119, 119, 142, 0.05)',
					offsetX: 0,
					offsetY: 0,
				},
				axisTicks: {
					show: true,
					borderType: 'solid',
					color: 'rgba(119, 119, 142, 0.05)',
					width: 6,
					offsetX: 0,
					offsetY: 0
				},
				labels: {
					rotate: -90
				}
			}
		};
		document.getElementById('budget').innerHTML = ''
		var chart = new ApexCharts(document.querySelector("#budget"), options);
		chart.render();
	}, 300);
}


//Visitors chart
function viewers1() {
	setTimeout(() => {
		var options = {
			series: [{
				name: 'Male',
				data: [51, 44, 55, 42, 58, 50, 62],
			}, {
				name: 'Female',
				data: [56, 58, 38, 50, 64, 45, 55]
			}],
			chart: {
				height: 270,
				type: 'line',
				toolbar: {
					show: false,
				},
				background: 'none',
				fill: "#fff",
			},
			grid: {
				borderColor: '#f2f6f7',
			},
			colors: [myVarVal || "#1fc5db", "#e4e7ed"],
			background: 'transparent',
			dataLabels: {
				enabled: false
			},
			stroke: {
				curve: 'straight',
				width: 2
			},
			xaxis: {
				type: 'day',
				categories: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
			},
			dataLabels: {
				enabled: false,
			},
			legend: {
				show: true,
				position: 'top',
			},
			xaxis: {
				show: false,
				axisBorder: {
					show: false,
					color: 'rgba(119, 119, 142, 0.05)',
					offsetX: 0,
					offsetY: 0,
				},
				axisTicks: {
					show: false,
					borderType: 'solid',
					color: 'rgba(119, 119, 142, 0.05)',
					width: 6,
					offsetX: 0,
					offsetY: 0
				},
				labels: {
					rotate: -90,
				}
			},
			yaxis: {
				show: false,
				axisBorder: {
					show: false,
				},
				axisTicks: {
					show: false,
				}
			},
			tooltip: {
				x: {
					format: 'dd/MM/yy HH:mm'
				},
			},
		};
		document.getElementById('Viewers1').innerHTML = ''
		var chart = new ApexCharts(document.querySelector("#Viewers1"), options);
		chart.render();
	}, 300);
}
// index1 chart data end


// index2 chart data
function statistics3() {
	setTimeout(()=>{
		var options = {
			series: [{
			name: 'active',
			data: [44, 42, 57, 86, 58, 55, 70, 43, 23, 54, 77, 34],
			},{
				name: 'inactive',
			data: [-34, -22, -37, -56, -21, -35, -60, -34, -56, -78, -89,-53],
		}],
			chart: {
			stacked: true,
			type: 'bar',
			height: 350,
		},
		grid: {
				borderColor: '#f2f6f7',
			},
		colors: [ myVarVal || "#38cab3","#e4e7ed"],
		plotOptions: {
			bar: {
			endingShape: 'rounded',
			colors: {
				ranges: [{
				from: -100,
				to: -46,
				color: '#ebeff5'
				}, {
				from: -45,
				to: 0,
				color: '#ebeff5'
				}]
			},
			columnWidth: '25%',
			}
		},
		dataLabels: {
			enabled: false,
		},
		legend: {
			show: true,
			position:'top',
		},
		yaxis: {
			title: {
			text: 'Growth',
				style: {
					color: '	#adb5be',
					fontSize: '14px',
					fontFamily: 'poppins, sans-serif',
					fontWeight: 600,
					cssClass: 'apexcharts-yaxis-label',
				},
			},
			labels: {
			formatter: function (y) {
				return y.toFixed(0) + "";
			}
			}
		},
		xaxis: {
			type: 'month',
			categories: ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'sep', 'oct', 'nov', 'dec'],
			axisBorder: {
						show: true,
						color: 'rgba(119, 119, 142, 0.05)',
						offsetX: 0,
						offsetY: 0,
					},
					axisTicks: {
						show: true,
						borderType: 'solid',
						color: 'rgba(119, 119, 142, 0.05)',
						width: 6,
						offsetX: 0,
						offsetY: 0
					},
			labels: {
			rotate: -90
			}
		}
		};
		document.getElementById('statistics3').innerHTML = ''
		var chart = new ApexCharts(document.querySelector("#statistics3"), options);	
		chart.render();
	}, 300);	
}	

//Visitors chart
function viewers2() {
	setTimeout(()=>{
		var options = {
			series: [{
			name: 'Male',
			data: [44, 42, 57, 86, 58, 55, 70],
			color:['#766df9']
			},{
				name: 'Female',
				data: [34, 22, 47, 56, 21, 35, 60],
				color:['#ebeff5']}
			],
			chart: {
			type: 'bar',
			stacked: true,
			height: 330
		},
		grid: {
			borderColor: '#eff2f6',
		},
		colors: [ myVarVal || "#38cab3","#e4e7ed"],
		plotOptions: {
			bar: {
			horizontal: false,
			columnWidth: '30%',
			},
		},
		
		dataLabels: {
			enabled: false
		},
		stroke: {
			show: true,
			width: 2,
			colors: ['transparent']
		},
		states: {
			hover: {
			filter: {
				type: 'none'
			}
			}
		},yaxis: {
			title: {
				style: {
					color: '	#adb5be',
					fontSize: '14px',
					fontFamily: 'poppins, sans-serif',
					fontWeight: 600,
					cssClass: 'apexcharts-yaxis-label',
				},
			},
			labels: {
			formatter: function (y) {
				return y.toFixed(0) + "";
			}
			}
		},
		xaxis: {
			categories: ['Mon','Tue', 'Web', 'Thu', 'Fri', 'Sat', 'Sun'],
			axisBorder: {
				show: true,
				color: 'rgba(119, 119, 142, 0.05)',
				offsetX: 0,
				offsetY: 0,
			},
			axisTicks: {
				show: true,
				borderType: 'solid',
				color: 'rgba(119, 119, 142, 0.05)',
				width: 6,
				offsetX: 0,
				offsetY: 0
			},
		},
		fill: {
			opacity: 1
		},
		legend: {
			position: "top"	
			},
		};
			document.getElementById('Viewers2').innerHTML = ''
		var chart = new ApexCharts(document.querySelector("#Viewers2"), options);
		chart.render();
	}, 300);	
}
// index2 cgart data end
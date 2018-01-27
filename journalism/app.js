var svgWidth = 1000;
var svgHeight = 600;

var margin = { top: 60, right: 50, bottom: 60, left: 120 };

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

var svg = d3.select(".chart")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var chart = svg.append("g");

d3.select(".chart")
    .append("div")
    .attr("class","tooltip")
    .style("opacity", 0);

d3.csv("data.csv", function(error, data) {
    if (error) throw error;
    data.forEach(function(data) {
        data.population = +data.population;
        data.vet_population = +data.vet_population;
        data.depressed = +data.depressed;
        data.vet_percent = +data.vet_percent;
        data.depressed = +data.depressed;
});

var yLinearScale = d3.scaleLinear()
    .range([height, 0]);

var xLinearScale = d3.scaleLinear()
    .range([0, width]);

var bottomAxis = d3.axisBottom(xLinearScale);
var leftAxis = d3.axisLeft(yLinearScale);

xLinearScale.domain([-1000, d3.max(data, function(d) {
    return +d.vet_population;
})]);
yLinearScale.domain([0, d3.max(data, function(d) {
    return +d.population;
})]);

var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80,-60])
    .html(function(data) {
        var state = data.state_name;
        var population = +data.population;
        var vet_pop = +data.vet_percent;
        var depress = +data.depressed;
        return (state + "<br> Population: " + population + "<br> Veteran Population: " + vet_pop + "%" + "<br> State Depression: " + depress + "%");
    });

chart.call(toolTip);

chart.selectAll("circle")
    .data(data)
    .enter().append("circle")
        .attr("cx", function(data, index) {
            // console.log(data.population);
            return xLinearScale(data.vet_population);
        })
        .attr("cy", function(data, index) {
            return yLinearScale(data.population)
        })
        .attr("r","15")
        .attr("fill", "#2884DA").style("opacity",.6)
        .on("click", function(data) {
            toolTip.show(data);
        })
        .on("mouseout", function(data, index) {
            toolTip.hide(data);
        });

chart.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);
chart.append("g")
    .call(leftAxis);

chart.append("text")
    .attr("transform","rotate(-90)")
    .attr("y", 0 -margin.left + 5)
    .attr("x", 0 -(height/2))
    .attr("dy","1em")
    .attr("class","axisText")
    .text("State Population (2014 ACS)");

chart.append("text")
    .attr("transform", "translate(" + (width/2) + "," + (height + margin.top ) + ")")
    .attr("class","axisText")
    .text("Veteran Population (2014 ACS)");
});

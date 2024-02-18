<script>
    import {onMount} from 'svelte'
    import * as d3 from 'd3';

    let data;

    onMount(async () => {
        data = await d3.json('https://raw.githubusercontent.com/jww2145/dev-fest-2024/main/data-exploration/clusters.json').then(function(data){
            var container = d3.select("#chart");
            var svg = container.append("svg"); 
            var width = +container.node().getBoundingClientRect().width;  

            svg.attr("width", width);

            var height = 300;
            svg.attr("height", height);

            var xExtent = d3.extent(data, d => +d[2]); 

            var xScale = d3.scaleLinear()
                .domain(xExtent)
                .range([25, width-25]);

              // Create groups for each cluster
            var groups = svg.selectAll("g")
                .data([0])
                .enter()
                .append("g")
                .attr("transform", d => 
                    `translate(50, ${(d * 60) + 50})`
                );
              // Add circles
        groups.selectAll("circle")
            .data(data)
            .enter()
            .append("circle")
            .attr("cy", 50) 
            .attr("r", 10)    
            .attr("fill", "steelblue")
            .attr("cx", d => xScale(+d[2]));  
            
        // Add text  
        groups.selectAll("text")
            .data(data)
            .enter()
            .append("text")
            .text(d => d[0])
            .attr("x", d => xScale(+d[2]))
            .attr("y", 65);
                })    
    })
</script>

<div id="chart"></div>


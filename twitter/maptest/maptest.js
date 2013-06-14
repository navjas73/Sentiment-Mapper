var po = org.polymaps;

// Compute noniles.
var quantile = pv.Scale.quantile()
    .quantiles(9)
    .domain(pv.values(maptest))
    .range(0, 8);

// Instantiate a new map
var map = po.map()

    // Use scalar vector graphics by 
    .container(document.getElementById("map").appendChild(po.svg("svg")))
    .center({lat: 39, lon: -96})
    .zoom(4)
    .zoomRange([3, 7])
    .add(po.interact());

// Add cloudmade map image
map.add(po.image()
    .url(po.url("http://{S}tile.cloudmade.com"
    + "/1a1b06b230af4efdbb989ea99e9841af" // reg key 
    + "/20760/256/{Z}/{X}/{Y}.png")
    .hosts(["a.", "b.", "c.", ""])));

// tile by county 
map.add(po.geoJson()
    .url("http://polymaps.appspot.com/county/{Z}/{X}/{Y}.json")
    .on("load", load)
    .id("county"));

map.add(po.geoJson()
    .url("http://polymaps.appspot.com/state/{Z}/{X}/{Y}.json")
    .id("state"));

map.add(po.compass()
    .pan("none"));

// load data from maptest-data
function load(e) {
  for (var i = 0; i < e.features.length; i++) {
    var feature = e.features[i];
    if (feature.data.id.substring(9) == "000") continue; // skip bogus counties
    var d = maptest[feature.data.id.substring(7)];
    feature.element.setAttribute("class", "q" + quantile(d) + "-" + 9);
    feature.element.appendChild(po.svg("title").appendChild(
        document.createTextNode(feature.data.properties.name + ": " + d + "%"))
        .parentNode);
  }
}

map.container().setAttribute("class", "Blues");


function addCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

//validation function that prevents non-numerical characters being input in input field
function isValid(el, evnt) { 
    var charC = (evnt.which) ? evnt.which : evnt.keyCode; 
    if (charC == 46) { 
        if (el.value.indexOf('.') === -1) { 
            return true; 
        } else { 
            return false; 
        } 
    } else { 
        if (charC > 31 && (charC < 48 || charC > 57)) 
            return false; 
    } 
    return true; 
} 



//resets map back to load state
function resetMap() {
    removeGrids();
    $('.layer-checks input').prop("checked", false);
    $('.legends,.nitr_grid_switch,.regress_grid_switch,#export-file').hide();
    $('#hexbin_size,#coeff').val('')
    map.fitBounds([[-92.75,42.4],[-86.86,47]], {padding: {top: 100, bottom: 0, left: 200, right: 200} });
    map.setLayoutProperty('nitrate_wells', 'visibility', 'none');
    map.setLayoutProperty('cancer_tracts', 'visibility', 'visible');
    $('.cancer_tracts_switch input').prop( "checked", true );
    $('.tract-legend').show();
    $('.reset-btn').addClass('disabled');
}




var tract_canrate = [],
    well_nitrate = [],
    reds = ['#fef0d9','#fdcc8a','#fc8d59','#e34a33','#b30000'],
    orPu = ['#e66101','#fdb863','#f7f7f7','#b2abd2','#5e3c99'],
    blues = ['#ffffcc','#a1dab4','#41b6c4','#2c7fb8','#253494'],
    devs = ['< -2 Std. Dev.', '-2 Std. Dev. - -1 Std. Dev.', '-1 Std. Dev. - 1 Std. Dev.', '1 Std. Dev. - 2 Std. Dev.', '> 2 Std. Dev.'];


//get geojson data for tracts, wells and the state border
$.ajax({
    type: 'GET',
    async: false,
    url: 'trailsx.geojson',
    data: { get_param: 'value' },
    dataType: 'json',
    success: function (data) {
        traildata = data;
/*
        $.each(data.features, function(k, v) {
            tract_canrate.push(v.properties.canrate);
        })
*/
     }
});

mapbox_path = "mapbox://mfriesenwisc.";

mapboxgl.accessToken = 'pk.eyJ1IjoibWZyaWVzZW53aXNjIiwiYSI6ImNqenhjcjAzYjBlc3QzbmtpODI1YXZxNmgifQ.Zz-z-Ykof8NbNaQOdR6ouQ';
var map = new mapboxgl.Map({
  container: 'map', // container id
  style: 'mapbox://styles/mfriesenwisc/ckn6sea6s0ikw17p90rswvxf7',
  zoom: 3
});
map.fitBounds([[-121.79,45.32],[-121.59,45.42]]);
/* map.fitBounds([[-121.79,45.32],[-121.59,45.46]], {padding: {top: 100, bottom: 0, left: 200, right: 200} }); */

var nav = new mapboxgl.NavigationControl({showCompass:false});
map.addControl(nav,'top-left');
var hoveredStateId = null;

/*
$(".reset-btn").on("click",function() {
    resetMap();
})
*/


map.on('load',function() {
    var maplayers = map.getStyle().layers;
    
/*
    // Find the index of the first symbol layer in the map style;
    var firstSymbolId;
    for (var i = 0; i < maplayers.length; i++) {
        if (maplayers[i].type === 'symbol') {
            firstSymbolId = maplayers[i].id;
            break;
        }
    }

    
*/
    
    
    //add geojson data as source for map layers
    map.addSource('trails', {
        'type': 'geojson',
        'data': traildata,
        'generateId': true
    });


    //add different map layers

    map.addLayer({
        'id': 'trails',
        'type': 'line',
        'source': 'trails',
        'layout': {
            'line-join': 'round',
            'line-cap': 'round'
        },
        'paint': {
            'line-color': 'forestgreen',
            'line-width': 1
        }
    })
    

    // make a pointer cursor
    map.getCanvas().style.cursor = 'default';
   

    //Code for layer toggle
    $(".layer-checks").show();
    $(".layer-checks input").on("change",function(e) {
        var thisLayer = $(this).data("layer");
        var thisLegend = $(this).data("legend");
        var thisHide = $(this).data("others");
        if (thisHide=='hide') {
            $('.legends').hide();
            $.each(layers,function(k,v) {
               map.setLayoutProperty(v, 'visibility', 'none'); 
            })
            $('.layer-checks input').prop("checked", false);
            $('.'+thisLayer+'_switch input').prop("checked", true);
            map.setLayoutProperty(thisLayer, 'visibility', 'visible');
        }
        if (e.target.checked) {
            $("."+thisLegend+"-legend").show();
        } else {
            $("."+thisLegend+"-legend").hide();
        }
        
        map.setLayoutProperty(
            thisLayer,
            'visibility',
            e.target.checked ? 'visible' : 'none'
        );
    })







})
        

         
    
    


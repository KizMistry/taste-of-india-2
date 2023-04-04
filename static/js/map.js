function initMap() {
  // Specify the location using latitude and longitude coordinates
  var location = {lat: 53.480759, lng: -2.257652};
  
  // Create a new Google Map centered on the location
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    center: location
  });
  
  // Add a marker at the location
  var marker = new google.maps.Marker({
    position: location,
    map: map,
    title: 'Indian Restaurant'
  });
}
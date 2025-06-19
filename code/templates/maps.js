//variáveis
let map;
let marker;

//função principal que inicializa o mapa
window.initMap = function () {
  const centro = { lat: -11.1811, lng: -40.5097 };
  
  //iniciando o mapa com centro, zoom e tipo satellite
  map = new google.maps.Map(document.getElementById("map"), {
    center: centro,
    zoom: 18,
    mapTypeId: "satellite",
  });

  //evento de clique para capturar coordenadas no mapa
  map.addListener("click", (e) => {
    const lat = e.latLng.lat();
    const lng = e.latLng.lng();

    //se já houver marcador, remove para não acumular
    if (marker !== null && marker !== undefined) {
      marker.setMap(null);
    }

    //cria um novo marcador no local clicado
    marker = new google.maps.Marker({
      position: { lat, lng },
      map: map,
    });

    alert(`Latitude: ${lat}\nLongitude: ${lng}`);
  });
};

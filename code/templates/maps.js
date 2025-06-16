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

    //envia as coordenadas para o backend Flask via fetch
    fetch('http://localhost:5000/coordenadas', {
      method: 'POST',                            //método POST para enviar dados
      headers: { 'Content-Type': 'application/json' }, //informando que é JSON
      body: JSON.stringify({ lat: lat, lng: lng })     //convertendo coordenadas para texto JSON
    })
    .then(response => response.json())// espera resposta do Flask e converte para JSON
    .then(data => {
      console.log('Servidor respondeu:', data);// imprime a resposta no console
    })
    .catch(error => {
      console.error('Erro ao enviar coordenadas:', error);// mostra erro caso ocorra
    });
  });
};

//variáveis
let map;
let marker;

//funcao principal
async function initMap() {
    //carrega as bibliotecas necessárias
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    //configuração inicial do mapa
    const centro = { lat: -20.5208, lng: -43.6919 };
    map = new Map(document.getElementById("map"), {
        center: centro,
        zoom: 18,
        mapTypeId: "satellite",
        mapId: "YOUR_MAP_ID"
    });

    //evento de clique no mapa
    map.addListener("click", async (event) => {
        const coords = {
            lat: event.latLng.lat(),
            lng: event.latLng.lng()
        };

        //remove o marcador anterior
        if (marker) {
            marker.map = null;
        }

        //cria um novo marcador
        marker = new AdvancedMarkerElement({
            position: coords,
            map: map,
            title: "Local selecionado"
        });

        console.log("Coordenadas capturadas:", coords);

        //passando para o servidor
        try {
            const response = await fetch("http://localhost:5000/receber-coordenadas", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(coords)
            });

            if (!response.ok) {
                throw new Error(`Erro HTTP: ${response.status}`);
            }

            const data = await response.json();
            console.log("Resposta do Flask:", data);
        } catch (error) {
            console.error("Falha ao enviar coordenadas:", error);
        }
    });
}

// api do maps
(function loadGoogleMaps() {
    const script = document.createElement("script");
    script.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyBXFUNhy2LRJkGIiHF1QgiFckX1bKjFeoM&loading=async&libraries=marker&callback=initMap`;
    script.async = true;
    script.defer = true;
    dxocument.head.appendChild(script);
})();
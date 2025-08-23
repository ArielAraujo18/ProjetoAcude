let map;
let marker;
let pontos = []; // armazenar os 4 pontos
let polygon = null;
let marcadores = []; // guardar os marcadores atuais

async function initMap() {
    console.log("Mapa inicializado, chamando carregarCoordenadas()");
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    const centro = { lat: -6.702437, lng: -36.944493 };
    map = new Map(document.getElementById("map"), {
        center: centro,
        zoom: 18,
        mapTypeId: "satellite",
        mapId: "YOUR_MAP_ID"
    });
     //Atualiza automaticamente a cada 5 segundos
    setInterval(atualizarCoordenadas, 5000);
    //Atualiza uma vez imediatamente
    atualizarCoordenadas();

    carregarCoordenadas();
    map.addListener("click", async (event) => {
        const lat = event.latLng.lat();
        const lng = event.latLng.lng();
        const coords = { lat, lng };

        // marca ponto no mapa
        new AdvancedMarkerElement({
            position: coords,
            map: map,
            title: `Ponto ${pontos.length + 1}`
        });

        // adiciona ponto
        pontos.push(coords);
        

        // quando tiver 4 pontos, desenhar polígono e verificar ponto
        if (pontos.length === 4) {
            console.log("4 pontos definidos:", pontos);

            enviarPontosAoFlask(pontos);

            //desenhar polígono visual
            if (polygon) polygon.setMap(null);
            polygon = new google.maps.Polygon({
                paths: pontos,
                strokeColor: "#FF0000",
                strokeOpacity: 0.8,
                strokeWeight: 2,
                fillColor: "#FF0000",
                fillOpacity: 0.35,
                map: map
            });

            alert("4 pontos definidos.");
        }

        // se clicar depois de 4 pontos
        if (pontos.length > 4) {
            const pontoTeste = coords;

            // converte para UTM
            const pt = utm.fromLatLon(pontoTeste.lat, pontoTeste.lng);
            const polygonUTM = pontos.slice(0, 4).map(p => {
                const pUTM = utm.fromLatLon(p.lat, p.lng);
                return [pUTM.easting, pUTM.northing];
            });

            const dentro = pointInPolygon([pt.easting, pt.northing], polygonUTM);

            if (dentro) {
                alert("Ponto está DENTRO do polígono.");
            } else {
                alert("Ponto está FORA do polígono.");
            }

            // limpa tudo
            pontos = [];
            if (polygon) polygon.setMap(null);
        }
    });
}

// carrega Google Maps
(function loadGoogleMaps() {
    const script = document.createElement("script");
    script.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyBXFUNhy2LRJkGIiHF1QgiFckX1bKjFeoM&loading=async&libraries=geometry,marker&callback=initMap`;
    script.async = true;
    script.defer = true;
    document.head.appendChild(script);
})();

function enviarPontosAoFlask(pontos) {
    fetch('http://localhost:5000/receber-coordenadas', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ pontos: pontos })
    })
    .then(res => res.json())
    .then(data => {
        console.log("Resposta do Flask:", data);
        alert("Pontos enviados com sucesso!");
    })
    .catch(err => {
        console.error("Erro ao enviar pontos:", err);
        alert("Erro ao enviar pontos.");
    });
}

async function carregarCoordenadas() {
    try {
        const res = await fetch("http://localhost:5001/receber-coordenadas");
        const data = await res.json();

        if (Array.isArray(data) && data.length > 0) {
            console.log("Pontos recebidos do Flask:", data);

            data.forEach((p, i) => {
                new google.maps.marker.AdvancedMarkerElement({
                    position: { lat: p.lat, lng: p.lng },
                    map: map,
                    title: `Ponto ${i + 1}`
                });
            });

            if (data.length >= 3) {
                const polygon = new google.maps.Polygon({
                    paths: data,
                    strokeColor: "#FF0000",
                    strokeOpacity: 0.8,
                    strokeWeight: 2,
                    fillColor: "#FF0000",
                    fillOpacity: 0.35,
                    map: map
                });
            }

            map.setCenter(data[0]);
        } else {
            console.warn("Nenhum ponto retornado do Flask.");
        }
    } catch (err) {
        console.error("Erro ao carregar coordenadas:", err);
    }
}

async function atualizarCoordenadas() {
    try {
        const res = await fetch("http://localhost:5001/receber-coordenadas");
        const data = await res.json();

        if (Array.isArray(data) && data.length > 0) {
            console.log("Coordenadas recebidas:", data);

            // Remove marcadores antigos
            marcadores.forEach(m => m.setMap(null));
            marcadores = [];

            // Cria novos marcadores
            data.forEach((p, i) => {
                const marker = new google.maps.marker.AdvancedMarkerElement({
                    position: { lat: p.lat, lng: p.lng },
                    map: map,
                    title: `Ponto ${i + 1}`
                });
                marcadores.push(marker);
            });

            // Remove polígono antigo
            if (polygon) polygon.setMap(null);

            // Desenha polígono se houver 3 ou mais pontos
            if (data.length >= 3) {
                polygon = new google.maps.Polygon({
                    paths: data,
                    strokeColor: "#FF0000",
                    strokeOpacity: 0.8,
                    strokeWeight: 2,
                    fillColor: "#FF0000",
                    fillOpacity: 0.35,
                    map: map
                });
            }

            // Centraliza no primeiro ponto
            map.setCenter(data[0]);
        }
    } catch (err) {
        console.error("Erro ao atualizar coordenadas:", err);
    }
}
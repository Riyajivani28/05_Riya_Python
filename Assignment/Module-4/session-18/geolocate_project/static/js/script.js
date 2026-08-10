/**
 * GeoLocate Hub - Dynamic Maps JavaScript Helper
 * Supports Google Maps API & automatic fallback to Leaflet.js (OpenStreetMap) when no API key is provided.
 */

// Helper to check if Google Maps JS API is loaded and working
function isGoogleMapsAvailable() {
    return typeof google !== 'undefined' && typeof google.maps !== 'undefined' && typeof google.maps.Map === 'function';
}

/**
 * Initializes Live Search Map (Google Maps or Leaflet Fallback)
 */
function initLiveMap(lat, lng, query, address) {
    const mapElement = document.getElementById('liveMap');
    if (!mapElement) return;

    lat = parseFloat(lat);
    lng = parseFloat(lng);

    if (isGoogleMapsAvailable()) {
        const searchLoc = { lat: lat, lng: lng };
        const map = new google.maps.Map(mapElement, {
            center: searchLoc,
            zoom: 15,
            mapTypeId: 'roadmap',
            zoomControl: true,
            streetViewControl: true,
            fullscreenControl: true
        });

        const marker = new google.maps.Marker({
            position: searchLoc,
            map: map,
            title: query,
            animation: google.maps.Animation.DROP
        });

        const infoContent = `
            <div style="padding: 8px; max-width: 250px;">
                <h6 style="margin: 0 0 6px 0; font-weight: 700; color: #0f172a;">${query}</h6>
                <p style="margin: 0 0 6px 0; font-size: 13px; color: #475569;"><i class="bi bi-geo-alt-fill text-primary me-1"></i>${address}</p>
                <span style="background: #dbeafe; color: #2563eb; font-weight: 600; padding: 2px 6px; border-radius: 4px; font-size: 11px;">
                    Lat: ${lat.toFixed(4)}, Lng: ${lng.toFixed(4)}
                </span>
            </div>
        `;
        const infoWindow = new google.maps.InfoWindow({ content: infoContent });
        marker.addListener('click', () => infoWindow.open(map, marker));
        infoWindow.open(map, marker);
    } else if (typeof L !== 'undefined') {
        mapElement.innerHTML = '';
        const map = L.map('liveMap').setView([lat, lng], 15);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);

        const marker = L.marker([lat, lng]).addTo(map);
        const popupContent = `
            <div style="padding: 4px; max-width: 220px;">
                <h6 style="margin: 0 0 4px 0; font-weight: 700; color: #0f172a;">${query}</h6>
                <p style="margin: 0 0 4px 0; font-size: 12px; color: #475569;">${address}</p>
                <small style="color: #2563eb; font-weight: 600;">Lat: ${lat.toFixed(4)}, Lng: ${lng.toFixed(4)}</small>
            </div>
        `;
        marker.bindPopup(popupContent).openPopup();
    }
}

/**
 * Initializes Single Restaurant Location Map
 */
function initRestaurantMap(lat, lng, name, address) {
    const mapElement = document.getElementById('restaurantMap');
    if (!mapElement) return;

    lat = parseFloat(lat);
    lng = parseFloat(lng);

    if (isGoogleMapsAvailable()) {
        const loc = { lat: lat, lng: lng };
        const map = new google.maps.Map(mapElement, {
            center: loc,
            zoom: 15,
            mapTypeId: 'roadmap'
        });

        const marker = new google.maps.Marker({
            position: loc,
            map: map,
            title: name,
            animation: google.maps.Animation.DROP
        });

        const infoContent = `
            <div style="padding: 8px; max-width: 240px;">
                <h6 style="margin: 0 0 6px 0; font-weight: 700;">${name}</h6>
                <p style="margin: 0; font-size: 13px; color: #475569;">${address}</p>
            </div>
        `;
        const infoWindow = new google.maps.InfoWindow({ content: infoContent });
        marker.addListener('click', () => infoWindow.open(map, marker));
        infoWindow.open(map, marker);
    } else if (typeof L !== 'undefined') {
        mapElement.innerHTML = '';
        const map = L.map('restaurantMap').setView([lat, lng], 15);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; OpenStreetMap'
        }).addTo(map);

        const marker = L.marker([lat, lng]).addTo(map);
        marker.bindPopup(`
            <div style="padding: 4px;">
                <h6 style="margin: 0 0 4px 0; font-weight: 700;">${name}</h6>
                <p style="margin: 0; font-size: 12px; color: #475569;">${address}</p>
            </div>
        `).openPopup();
    }
}

/**
 * Initializes Nearby Cafes Map (User Marker + Cafe Markers)
 */
function initCafeMap(userLat, userLng, userAddress, cafes) {
    const mapElement = document.getElementById('cafeMap');
    if (!mapElement) return;

    userLat = parseFloat(userLat);
    userLng = parseFloat(userLng);

    if (isGoogleMapsAvailable()) {
        const userLoc = { lat: userLat, lng: userLng };
        const map = new google.maps.Map(mapElement, {
            center: userLoc,
            zoom: 14,
            mapTypeId: 'roadmap'
        });

        const bounds = new google.maps.LatLngBounds();

        const userMarker = new google.maps.Marker({
            position: userLoc,
            map: map,
            title: 'Your Location',
            icon: 'https://maps.google.com/mapfiles/ms/icons/blue-dot.png',
            animation: google.maps.Animation.DROP
        });

        const userInfoWindow = new google.maps.InfoWindow({
            content: `<div style="padding: 6px;"><strong style="color: #2563eb;">📍 Your Search Location</strong><br/><span style="font-size: 12px;">${userAddress}</span></div>`
        });
        userMarker.addListener('click', () => userInfoWindow.open(map, userMarker));
        bounds.extend(userLoc);

        cafes.forEach((cafe, index) => {
            const cafeLoc = { lat: parseFloat(cafe.lat), lng: parseFloat(cafe.lng) };
            const cafeMarker = new google.maps.Marker({
                position: cafeLoc,
                map: map,
                title: cafe.name,
                icon: 'https://maps.google.com/mapfiles/ms/icons/red-dot.png',
                label: { text: `${index + 1}`, color: 'white', fontWeight: 'bold' }
            });

            const infoWindow = new google.maps.InfoWindow({
                content: `
                    <div style="padding: 6px; max-width: 200px;">
                        <h6 style="margin: 0 0 4px 0; font-weight: 700;">#${index + 1} ${cafe.name}</h6>
                        <p style="margin: 0 0 4px 0; font-size: 12px;">${cafe.address}</p>
                        <span style="background: #dbeafe; color: #2563eb; font-weight: 600; padding: 2px 6px; border-radius: 4px; font-size: 11px;">⚡ ${cafe.distance} km away</span>
                    </div>
                `
            });
            cafeMarker.addListener('click', () => infoWindow.open(map, cafeMarker));
            bounds.extend(cafeLoc);
        });

        if (cafes.length > 0) map.fitBounds(bounds);

    } else if (typeof L !== 'undefined') {
        mapElement.innerHTML = '';
        const map = L.map('cafeMap').setView([userLat, userLng], 14);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; OpenStreetMap'
        }).addTo(map);

        // Custom Leaflet Markers with HTML/CSS icons
        const blueIcon = L.divIcon({
            className: 'custom-leaflet-icon',
            html: `<div style="background-color:#2563eb; width:28px; height:28px; border-radius:50%; border:3px solid white; box-shadow:0 2px 5px rgba(0,0,0,0.3); display:flex; align-items:center; justify-content:center; color:white; font-size:14px;"><i class="bi bi-person-fill"></i></div>`,
            iconSize: [28, 28],
            iconAnchor: [14, 14]
        });

        const userMarker = L.marker([userLat, userLng], { icon: blueIcon }).addTo(map);
        userMarker.bindPopup(`
            <div style="padding: 4px;">
                <strong style="color: #2563eb;">📍 Your Search Location</strong><br/>
                <span style="font-size: 12px;">${userAddress}</span>
            </div>
        `).openPopup();

        const latLngGroup = [[userLat, userLng]];

        cafes.forEach((cafe, index) => {
            const cLat = parseFloat(cafe.lat);
            const cLng = parseFloat(cafe.lng);
            latLngGroup.push([cLat, cLng]);

            const redIcon = L.divIcon({
                className: 'custom-leaflet-icon',
                html: `<div style="background-color:#dc2626; width:26px; height:26px; border-radius:50%; border:2px solid white; box-shadow:0 2px 5px rgba(0,0,0,0.3); display:flex; align-items:center; justify-content:center; color:white; font-weight:bold; font-size:12px;">${index + 1}</div>`,
                iconSize: [26, 26],
                iconAnchor: [13, 13]
            });

            const cafeMarker = L.marker([cLat, cLng], { icon: redIcon }).addTo(map);
            cafeMarker.bindPopup(`
                <div style="padding: 6px; max-width: 200px;">
                    <h6 style="margin: 0 0 4px 0; font-weight: 700;">#${index + 1} ${cafe.name}</h6>
                    <p style="margin: 0 0 4px 0; font-size: 12px; color: #475569;">${cafe.address}</p>
                    <span style="background: #dbeafe; color: #2563eb; font-weight: 600; padding: 2px 6px; border-radius: 4px; font-size: 11px;">⚡ ${cafe.distance} km away</span>
                </div>
            `);
        });

        if (latLngGroup.length > 1) {
            map.fitBounds(latLngGroup, { padding: [30, 30] });
        }
    }
}

/**
 * Initializes Pickup Points Map (User Marker + Pickup Markers)
 */
function initPickupMap(userLat, userLng, userAddress, pickupPoints) {
    const mapElement = document.getElementById('pickupMap');
    if (!mapElement) return;

    userLat = parseFloat(userLat);
    userLng = parseFloat(userLng);

    if (isGoogleMapsAvailable()) {
        const userLoc = { lat: userLat, lng: userLng };
        const map = new google.maps.Map(mapElement, {
            center: userLoc,
            zoom: 13,
            mapTypeId: 'roadmap'
        });

        const bounds = new google.maps.LatLngBounds();

        const userMarker = new google.maps.Marker({
            position: userLoc,
            map: map,
            title: 'Your Address',
            icon: 'https://maps.google.com/mapfiles/ms/icons/blue-dot.png',
            animation: google.maps.Animation.DROP
        });

        const userInfoWindow = new google.maps.InfoWindow({
            content: `<div style="padding: 6px;"><strong style="color: #2563eb;">📍 Your Search Address</strong><br/><span style="font-size: 12px;">${userAddress}</span></div>`
        });
        userMarker.addListener('click', () => userInfoWindow.open(map, userMarker));
        bounds.extend(userLoc);

        pickupPoints.forEach((pt, index) => {
            const ptLoc = { lat: parseFloat(pt.lat), lng: parseFloat(pt.lng) };
            const isNearest = pt.is_nearest;
            const ptMarker = new google.maps.Marker({
                position: ptLoc,
                map: map,
                title: pt.name,
                icon: isNearest ? 'https://maps.google.com/mapfiles/ms/icons/green-dot.png' : 'https://maps.google.com/mapfiles/ms/icons/purple-dot.png',
                label: { text: `${index + 1}`, color: 'white', fontWeight: 'bold' }
            });

            const badgeHtml = isNearest 
                ? `<span style="background: #dcfce7; color: #15803d; font-weight: 700; padding: 2px 6px; border-radius: 4px; font-size: 11px;">★ Nearest Pickup Point</span>`
                : `<span style="background: #f1f5f9; color: #475569; font-weight: 600; padding: 2px 6px; border-radius: 4px; font-size: 11px;">${pt.distance} km away</span>`;

            const infoWindow = new google.maps.InfoWindow({
                content: `
                    <div style="padding: 6px; max-width: 220px;">
                        <h6 style="margin: 0 0 4px 0; font-weight: 700;">#${index + 1} ${pt.name}</h6>
                        <p style="margin: 0 0 6px 0; font-size: 12px; color: #475569;">${pt.address}, ${pt.city}</p>
                        ${badgeHtml}
                    </div>
                `
            });
            ptMarker.addListener('click', () => infoWindow.open(map, ptMarker));
            bounds.extend(ptLoc);
        });

        if (pickupPoints.length > 0) map.fitBounds(bounds);

    } else if (typeof L !== 'undefined') {
        mapElement.innerHTML = '';
        const map = L.map('pickupMap').setView([userLat, userLng], 13);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; OpenStreetMap'
        }).addTo(map);

        const blueIcon = L.divIcon({
            className: 'custom-leaflet-icon',
            html: `<div style="background-color:#2563eb; width:28px; height:28px; border-radius:50%; border:3px solid white; box-shadow:0 2px 5px rgba(0,0,0,0.3); display:flex; align-items:center; justify-content:center; color:white; font-size:14px;"><i class="bi bi-person-fill"></i></div>`,
            iconSize: [28, 28],
            iconAnchor: [14, 14]
        });

        const userMarker = L.marker([userLat, userLng], { icon: blueIcon }).addTo(map);
        userMarker.bindPopup(`
            <div style="padding: 4px;">
                <strong style="color: #2563eb;">📍 Your Search Address</strong><br/>
                <span style="font-size: 12px;">${userAddress}</span>
            </div>
        `).openPopup();

        const latLngGroup = [[userLat, userLng]];

        pickupPoints.forEach((pt, index) => {
            const pLat = parseFloat(pt.lat);
            const pLng = parseFloat(pt.lng);
            latLngGroup.push([pLat, pLng]);

            const isNearest = pt.is_nearest;
            const bgColor = isNearest ? '#16a34a' : '#9333ea';

            const ptIcon = L.divIcon({
                className: 'custom-leaflet-icon',
                html: `<div style="background-color:${bgColor}; width:26px; height:26px; border-radius:50%; border:2px solid white; box-shadow:0 2px 5px rgba(0,0,0,0.3); display:flex; align-items:center; justify-content:center; color:white; font-weight:bold; font-size:12px;">${index + 1}</div>`,
                iconSize: [26, 26],
                iconAnchor: [13, 13]
            });

            const ptMarker = L.marker([pLat, pLng], { icon: ptIcon }).addTo(map);

            const badgeHtml = isNearest 
                ? `<span style="background: #dcfce7; color: #15803d; font-weight: 700; padding: 2px 6px; border-radius: 4px; font-size: 11px;">★ Nearest Pickup Point</span>`
                : `<span style="background: #f1f5f9; color: #475569; font-weight: 600; padding: 2px 6px; border-radius: 4px; font-size: 11px;">${pt.distance} km away</span>`;

            ptMarker.bindPopup(`
                <div style="padding: 6px; max-width: 220px;">
                    <h6 style="margin: 0 0 4px 0; font-weight: 700;">#${index + 1} ${pt.name}</h6>
                    <p style="margin: 0 0 6px 0; font-size: 12px; color: #475569;">${pt.address}, ${pt.city}</p>
                    ${badgeHtml}
                </div>
            `);
        });

        if (latLngGroup.length > 1) {
            map.fitBounds(latLngGroup, { padding: [30, 30] });
        }
    }
}

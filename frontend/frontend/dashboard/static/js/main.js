document.addEventListener('DOMContentLoaded', function () {
    if (document.getElementById('load-clientes')) {
        document.getElementById('load-clientes').addEventListener('click', loadClientes);
    }
    if (document.getElementById('load-servicios')) {
        document.getElementById('load-servicios').addEventListener('click', loadServicios);
    }
    if (document.getElementById('load-ventas')) {
        document.getElementById('load-ventas').addEventListener('click', loadVentas);
    }
    if (document.getElementById('load-catalogo')) {
        document.getElementById('load-catalogo').addEventListener('click', loadCatalogo);
    }
});

function loadClientes() {
    fetch('http://localhost:9020/clientes_proveedores/clientes/')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('clientes-table-body');
            tableBody.innerHTML = '';
            data.forEach(cliente => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${cliente.id}</td>
                    <td>${cliente.nombre}</td>
                    <td>${cliente.correo}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error:', error));
}

function loadServicios() {
    fetch('http://localhost:9020/servicios_categorias/servicios/')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('servicios-table-body');
            tableBody.innerHTML = '';
            data.forEach(servicio => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${servicio.id}</td>
                    <td>${servicio.nombre}</td>
                    <td>${servicio.descripcion}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error:', error));
}

function loadVentas() {
    fetch('http://localhost:9020/ventas_cotizaciones/ventas/')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('ventas-table-body');
            tableBody.innerHTML = '';
            data.forEach(venta => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${venta.id}</td>
                    <td>${venta.producto}</td>
                    <td>${venta.cantidad}</td>
                    <td>${venta.precio}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error:', error));
}

function loadCatalogo() {
    fetch('http://localhost:9020/catalogo/')
        .then(response => response.json())
        .then(data => {
            const catalogoDiv = document.getElementById('catalogo');
            catalogoDiv.innerHTML = '';
            data.forEach(item => {
                const card = document.createElement('div');
                card.className = 'card';
                card.innerHTML = `
                    <img src="${item.imagen_url}" class="card-img-top" alt="${item.nombre}">
                    <div class="card-body">
                        <h5 class="card-title">${item.nombre}</h5>
                        <p class="card-text">${item.descripcion}</p>
                        <button class="btn btn-primary" onclick="addToCart(${item.id})">Agregar al Carrito</button>
                    </div>
                `;
                catalogoDiv.appendChild(card);
            });
        })
        .catch(error => console.error('Error:', error));
}

function addToCart(itemId) {
    // Lógica para agregar el item al carrito
    console.log('Item agregado al carrito:', itemId);
}
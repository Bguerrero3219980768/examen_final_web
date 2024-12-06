const API_URL = "http://127.0.0.1:8000/api";

// Función para obtener y mostrar hospitales
async function cargarHospitales() {
    const response = await fetch(`${API_URL}/hospitales/`);
    const hospitales = await response.json();
    const listaHospitales = document.getElementById("lista-hospitales");

    hospitales.forEach(hospital => {
        const li = document.createElement("li");
        li.textContent = `${hospital.nombre} - ${hospital.direccion}`;
        listaHospitales.appendChild(li);
    });
}

// Función para obtener y mostrar médicos
async function cargarMedicos() {
    const response = await fetch(`${API_URL}/medicos/`);
    const medicos = await response.json();
    const listaMedicos = document.getElementById("lista-medicos");

    medicos.forEach(medico => {
        const li = document.createElement("li");
        li.innerHTML = `<a href="detalle_medico.html?id=${medico.id}">${medico.nombre}</a> - ${medico.especialidad}`;
        listaMedicos.appendChild(li);
    });
}

// Carga inicial
cargarHospitales();
cargarMedicos();

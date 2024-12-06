const API_URL = "http://127.0.0.1:8000/api";

// Obtener ID del médico desde la URL
const params = new URLSearchParams(window.location.search);
const medicoId = params.get("id");

// Cargar detalle del médico y sus pacientes
async function cargarDetalleMedico() {
    const response = await fetch(`${API_URL}/medicos/${medicoId}/`);
    const medico = await response.json();

    document.getElementById("medico-detalle").innerHTML = `
        <h2>${medico.nombre}</h2>
        <p>Especialidad: ${medico.especialidad}</p>
        <p>Hospital: ${medico.hospital}</p>
    `;

    const responsePacientes = await fetch(`${API_URL}/pacientes/?medico=${medicoId}`);
    const pacientes = await responsePacientes.json();

    const listaPacientes = document.getElementById("lista-pacientes");
    pacientes.forEach(paciente => {
        const li = document.createElement("li");
        li.textContent = `${paciente.nombre} - ${paciente.enfermedad_diagnosticada}`;
        listaPacientes.appendChild(li);
    });
}

cargarDetalleMedico();

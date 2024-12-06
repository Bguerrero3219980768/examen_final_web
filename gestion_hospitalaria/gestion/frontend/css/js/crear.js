const API_URL = "http://127.0.0.1:8000/api";

document.getElementById("form-nuevo-paciente").addEventListener("submit", async function (event) {
    event.preventDefault();

    const paciente = {
        nombre: document.getElementById("nombre").value,
        edad: document.getElementById("edad").value,
        enfermedad_diagnosticada: document.getElementById("enfermedad").value,
        medico: document.getElementById("medico").value
    };

    const response = await fetch(`${API_URL}/pacientes/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(paciente)
    });

    if (response.ok) {
        alert("Paciente creado exitosamente");
        window.location.href = "index.html";
    } else {
        alert("Error al crear paciente");
    }
});

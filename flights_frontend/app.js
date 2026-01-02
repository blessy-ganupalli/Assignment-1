const searchForm = document.getElementById("searchForm");
if (searchForm) {
    searchForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const source = document.getElementById("source").value;
        const destination = document.getElementById("destination").value;
        const date = document.getElementById("date").value;

        localStorage.setItem("searchData", JSON.stringify({ source, destination, date }));
        window.location.href = "results.html";
    });
}

const table = document.getElementById("flightTable");
if (table) {
    const flights = [
        { flight_id: "A1", airline: "Indigo", price: 4500, seats: 10 },
        { flight_id: "A2", airline: "Air India", price: 5200, seats: 5 }
    ];

    flights.forEach(f => {
        table.innerHTML += `
            <tr>
                <td>${f.flight_id}</td>
                <td>${f.airline}</td>
                <td>${f.price}</td>
                <td>${f.seats}</td>
                <td><button onclick="book('${f.flight_id}')">Book</button></td>
            </tr>
        `;
    });
}

function book(flightId) {
    localStorage.setItem("flight_id", flightId);
    window.location.href = "booking.html";
}

const bookingForm = document.getElementById("bookingForm");
if (bookingForm) {
    document.getElementById("flight_id").value = localStorage.getItem("flight_id");

    bookingForm.addEventListener("submit", function (e) {
        e.preventDefault();
        window.location.href = "success.html";
    });
}

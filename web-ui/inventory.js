const params = new URLSearchParams(window.location.search);
const userId = params.get("user_id");
const name = params.get("name") || "Player";

document.getElementById(
  "greeting"
).textContent = `Hello, ${name}! Your Inventory:`;

// Update fetch URL using userId
fetch(`http://localhost:5000/inventory/${userId}`)
  .then((res) => {
    if (!res.ok) throw new Error("Fetch failed");
    return res.json();
  })
  .then((items) => {
    const tbody = document.querySelector("#inventory-table tbody");
    if (items.length === 0) {
      tbody.innerHTML = '<tr><td colspan="3">No items collected yet.</td></tr>';
    } else {
      items.forEach(([item, rarity, time]) => {
        const row = `<tr><td>${item}</td><td>${rarity}</td><td>${new Date(
          time
        ).toLocaleString()}</td></tr>`;
        tbody.innerHTML += row;
      });
    }
  })
  .catch((err) => {
    console.error(err);
    document.getElementById("greeting").textContent =
      "Failed to load inventory";
  });
